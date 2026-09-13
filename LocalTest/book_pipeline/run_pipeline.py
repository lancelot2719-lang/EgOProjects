#!/usr/bin/env python3
"""
Полностью автоматический пайплайн анализа книги (или папки книг) через
локальные модели в LM Studio: нарезка -> Extractor -> Validator ->
Synthesizer -> Distiller. Без участия человека: скрипт сам переключает
модели в LM Studio между этапами (через `lms`) и сам зовёт LM Studio API.

ТРЕБОВАНИЯ
- LM Studio, сервер запущен (`lms server start`), утилита `lms` в PATH.
- Папка prompts/ с 4 файлами: extractor.txt, validator.txt, synthesizer.txt,
  distiller.txt (шаблоны с плейсхолдерами {{TITLE}}, {{AUTHOR}}, {{TEXT}},
  {{PART_NUM}}, {{PART_TOTAL}}, {{EXTRACTOR_OUTPUT}}, {{ALL_VALIDATED_RESULTS}},
  {{SYNTHESIZER_OUTPUT}}).
- Только стандартный Python, ничего ставить не нужно.

ПРИМЕР — одна книга:
    python run_pipeline.py --book "Автор - Название.txt" --prompts prompts --out-root out

ПРИМЕР — вся папка книг подряд, без участия:
    python run_pipeline.py --book books/ --prompts prompts --out-root out

Имя файла книги вида "Автор - Название.txt" автоматически даёт Title/Author
для промтов. Если тире нет — всё имя файла идёт как Title.

Можно прервать (Ctrl+C / выключить ПК) и запустить снова с тем же --out-root:
по умолчанию включён --resume, уже готовые части и этапы пересчитываться не будут.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime


# ---------- утилиты ----------

def log(msg: str, log_file: str | None = None):
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line, flush=True)
    if log_file:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(line + "\n")


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, text: str):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def sanitize(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip() or "book"


def is_ready(path: str) -> bool:
    return os.path.isfile(path) and os.path.getsize(path) > 0


# ---------- нарезка книги на части (та же логика, что в split_book.py) ----------

def split_into_paragraphs(text: str) -> list[str]:
    paras = re.split(r"\n\s*\n", text)
    return [p.strip() for p in paras if p.strip()]


def pack_paragraphs(paragraphs: list[str], max_chars: int) -> list[str]:
    parts, current, current_len = [], [], 0
    for para in paragraphs:
        para_len = len(para) + 2
        if current and current_len + para_len > max_chars:
            parts.append("\n\n".join(current))
            current, current_len = [], 0
        if para_len > max_chars:
            sentences = re.split(r"(?<=[.!?…])\s+", para)
            buf, buf_len = [], 0
            for sent in sentences:
                s_len = len(sent) + 1
                if buf and buf_len + s_len > max_chars:
                    parts.append(" ".join(buf))
                    buf, buf_len = [], 0
                buf.append(sent)
                buf_len += s_len
            if buf:
                current, current_len = [" ".join(buf)], len(" ".join(buf))
            continue
        current.append(para)
        current_len += para_len
    if current:
        parts.append("\n\n".join(current))
    return parts


def split_book(book_path: str, parts_dir: str, target_tokens: int, chars_per_token: float) -> list[str]:
    max_chars = int(target_tokens * chars_per_token)
    text = read_file(book_path)
    paragraphs = split_into_paragraphs(text)
    parts = pack_paragraphs(paragraphs, max_chars)
    os.makedirs(parts_dir, exist_ok=True)
    paths = []
    for i, part in enumerate(parts, start=1):
        p = os.path.join(parts_dir, f"part{i:03d}.txt")
        write_file(p, part)
        paths.append(p)
    return paths


# ---------- управление LM Studio ----------

def lms_switch_model(lms_path: str, model: str, identifier: str, context_length: int,
                      gpu: str, log_file: str, wait_timeout: int = 180):
    log(f"Переключаю модель LM Studio -> {model} (identifier={identifier}, context={context_length})", log_file)
    try:
        subprocess.run([lms_path, "unload", "--all"], check=False,
                        capture_output=True, text=True, timeout=60)
        load_cmd = [lms_path, "load", model, f"--identifier={identifier}",
                    f"--context-length={context_length}", f"--gpu={gpu}"]
        log(f"Команда: {' '.join(load_cmd)}", log_file)
        result = subprocess.run(load_cmd, check=False, capture_output=True, text=True, timeout=wait_timeout)
        if result.stdout.strip():
            log(f"lms load stdout: {result.stdout.strip()}", log_file)
        if result.returncode != 0:
            log(f"lms load вернул код {result.returncode}: {result.stderr.strip()}", log_file)
    except FileNotFoundError:
        log(f"ОШИБКА: команда '{lms_path}' не найдена. Укажи полный путь через --lms-path "
            f"или добавь LM Studio CLI в PATH.", log_file)
        raise
    except subprocess.TimeoutExpired:
        log("ОШИБКА: загрузка модели не уложилась в таймаут.", log_file)
        raise

    # даём модели немного времени до полной готовности и проверяем lms ps
    deadline = time.time() + 30
    while time.time() < deadline:
        try:
            ps = subprocess.run([lms_path, "ps"], capture_output=True, text=True, timeout=20)
            if identifier in (ps.stdout or ""):
                log(f"Модель '{identifier}' загружена и готова.", log_file)
                return
        except Exception:
            pass
        time.sleep(3)
    log(f"Внимание: не удалось подтвердить готовность '{identifier}' через lms ps, продолжаю всё равно.", log_file)


# ---------- вызов LM Studio API ----------

def resolve_var_value(value: str) -> str:
    if any(ch in value for ch in "*?[]"):
        paths = sorted(glob.glob(value))
        if not paths:
            return ""
        return "\n\n".join(f"--- {os.path.basename(p)} ---\n{read_file(p)}" for p in paths)
    if os.path.isfile(value):
        return read_file(value)
    return value


def render_template(prompt_path: str, variables: dict) -> str:
    template = read_file(prompt_path)
    for name, value in variables.items():
        template = template.replace("{{" + name + "}}", resolve_var_value(str(value)))
    return template


def call_llm(base_url: str, model: str, prompt_text: str, max_tokens: int, temperature: float,
             timeout: int, retries: int, retry_delay: int, log_file: str) -> str:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt_text}],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }
    req_data = json.dumps(payload).encode("utf-8")

    last_err = None
    for attempt in range(1, retries + 2):
        req = urllib.request.Request(
            base_url.rstrip("/") + "/chat/completions",
            data=req_data, headers={"Content-Type": "application/json"}, method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                body = json.loads(resp.read().decode("utf-8"))
            return body["choices"][0]["message"]["content"]
        except Exception as e:
            last_err = e
            log(f"Попытка {attempt}/{retries + 1} не удалась: {e}", log_file)
            if attempt <= retries:
                time.sleep(retry_delay)
    raise RuntimeError(f"Не удалось получить ответ от модели '{model}': {last_err}")


# ---------- обработка одной книги ----------

def title_author_from_name(name: str, forced_title: str | None, forced_author: str | None):
    if forced_title:
        return forced_title, (forced_author or "")
    if " - " in name:
        author, title = name.split(" - ", 1)
        return title.strip(), author.strip()
    return name.strip(), ""


def process_book(job: dict, args):
    """job = {"kind": "book", "path": <txt файл книги>}
           или {"kind": "parts", "path": <папка с готовыми part*.txt>}"""
    kind = job["kind"]
    source_path = job["path"]

    if kind == "parts":
        name = os.path.basename(os.path.normpath(source_path))
    else:
        name = os.path.splitext(os.path.basename(source_path))[0]
    title, author = title_author_from_name(name, args.title, args.author)

    book_dir = os.path.join(args.out_root, sanitize(name))
    parts_dir = os.path.join(book_dir, "parts")
    out_dir = os.path.join(book_dir, "out")
    log_file = os.path.join(book_dir, "pipeline.log")
    os.makedirs(out_dir, exist_ok=True)

    log(f"=== КНИГА: {title}" + (f" ({author})" if author else "") + f" === [{source_path}]", log_file)

    if kind == "parts":
        part_paths = sorted(glob.glob(os.path.join(source_path, "part*.txt")))
        if not part_paths:
            log(f"ОШИБКА: в {source_path} не найдено файлов part*.txt", log_file)
            return False
        log(f"Использую {len(part_paths)} готовых частей из {source_path} напрямую, без пересборки.", log_file)
    else:
        existing_parts = sorted(glob.glob(os.path.join(parts_dir, "part*.txt")))
        if existing_parts and args.resume:
            part_paths = existing_parts
            log(f"Найдено {len(part_paths)} уже нарезанных частей, использую их (--resume).", log_file)
        else:
            part_paths = split_book(source_path, parts_dir, args.target_tokens, args.chars_per_token)
            log(f"Книга нарезана на {len(part_paths)} частей.", log_file)

    part_total = len(part_paths)
    prompts = {name: os.path.join(args.prompts, f"{name}.txt")
               for name in ("extractor", "validator", "synthesizer", "distiller")}
    for name, p in prompts.items():
        if not os.path.isfile(p):
            log(f"ОШИБКА: не найден шаблон промта {p}", log_file)
            return False

    failed = []

    # --- Extractor: модель грузится один раз на все части ---
    lms_switch_model(args.lms_path, args.extractor_model, "extractor",
                      args.extractor_context, args.gpu, log_file)
    for i, part_path in enumerate(part_paths, start=1):
        out_path = os.path.join(out_dir, f"part{i:03d}_extractor.md")
        if args.resume and is_ready(out_path):
            log(f"[{i}/{part_total}] Extractor: готово ранее, пропуск.", log_file)
            continue
        log(f"[{i}/{part_total}] Extractor...", log_file)
        try:
            text = call_llm(
                args.base_url, "extractor",
                render_template(prompts["extractor"], {
                    "TITLE": title, "AUTHOR": author,
                    "PART_NUM": str(i), "PART_TOTAL": str(part_total),
                    "TEXT": part_path,
                }),
                args.extractor_max_tokens, args.temperature, args.timeout, args.retries, args.retry_delay, log_file,
            )
            write_file(out_path, text)
            log(f"[{i}/{part_total}] Extractor OK ({len(text)} симв.)", log_file)
        except Exception as e:
            log(f"[{i}/{part_total}] Extractor ОШИБКА: {e}", log_file)
            failed.append(("extractor", i))

    # --- Validator: переключаем модель один раз на все части ---
    lms_switch_model(args.lms_path, args.validator_model, "validator",
                      args.validator_context, args.gpu, log_file)
    for i, part_path in enumerate(part_paths, start=1):
        extractor_out = os.path.join(out_dir, f"part{i:03d}_extractor.md")
        if not is_ready(extractor_out):
            log(f"[{i}/{part_total}] Validator: пропуск, нет результата Extractor.", log_file)
            continue
        out_path = os.path.join(out_dir, f"part{i:03d}_validated.md")
        if args.resume and is_ready(out_path):
            log(f"[{i}/{part_total}] Validator: готово ранее, пропуск.", log_file)
            continue
        log(f"[{i}/{part_total}] Validator...", log_file)
        try:
            text = call_llm(
                args.base_url, "validator",
                render_template(prompts["validator"], {"TEXT": part_path, "EXTRACTOR_OUTPUT": extractor_out}),
                args.validator_max_tokens, args.temperature, args.timeout, args.retries, args.retry_delay, log_file,
            )
            write_file(out_path, text)
            log(f"[{i}/{part_total}] Validator OK ({len(text)} симв.)", log_file)
        except Exception as e:
            log(f"[{i}/{part_total}] Validator ОШИБКА: {e}", log_file)
            failed.append(("validator", i))

    if failed and not args.force:
        log(f"ОСТАНОВКА перед Synthesizer: {len(failed)} этапов с ошибкой: {failed}", log_file)
        log("Почини (например, перезапусти сервер/подними timeout) и запусти скрипт снова с тем же "
            "--out-root — --resume подхватит только недостающее. Либо добавь --force, чтобы "
            "продолжить, пропустив проблемные части.", log_file)
        return False

    # --- Synthesizer (модель validator уже загружена) ---
    synth_out = os.path.join(out_dir, "book_synthesis.md")
    if not (args.resume and is_ready(synth_out)):
        log("Synthesizer...", log_file)
        try:
            text = call_llm(
                args.base_url, "validator",
                render_template(prompts["synthesizer"], {
                    "TITLE": title, "AUTHOR": author, "PART_TOTAL": str(part_total),
                    "ALL_VALIDATED_RESULTS": os.path.join(out_dir, "part*_validated.md"),
                }),
                args.synthesizer_max_tokens, args.temperature, args.timeout, args.retries, args.retry_delay, log_file,
            )
            write_file(synth_out, text)
            log(f"Synthesizer OK ({len(text)} симв.)", log_file)
        except Exception as e:
            log(f"Synthesizer ОШИБКА: {e}", log_file)
            return False
    else:
        log("Synthesizer: готово ранее, пропуск.", log_file)

    # --- Distiller ---
    final_out = os.path.join(out_dir, "book_final.md")
    if not (args.resume and is_ready(final_out)):
        log("Distiller...", log_file)
        try:
            text = call_llm(
                args.base_url, "validator",
                render_template(prompts["distiller"], {"SYNTHESIZER_OUTPUT": synth_out}),
                args.distiller_max_tokens, args.temperature, args.timeout, args.retries, args.retry_delay, log_file,
            )
            write_file(final_out, text)
            log(f"Distiller OK ({len(text)} симв.)", log_file)
        except Exception as e:
            log(f"Distiller ОШИБКА: {e}", log_file)
            return False
    else:
        log("Distiller: готово ранее, пропуск.", log_file)

    log(f"=== ГОТОВО: {final_out} ===", log_file)
    return True


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description="Полностью автоматический пайплайн анализа книг через LM Studio")
    ap.add_argument("--book", default=None, help="Путь к .txt книги ИЛИ к папке с несколькими .txt книгами")
    ap.add_argument("--parts", action="append", default=None,
                     help="Папка с уже готовыми part001.txt, part002.txt... — нарезка не выполняется, "
                          "части берутся как есть. Можно указать флаг несколько раз для нескольких книг "
                          "(тогда --title/--author лучше не задавать — имя книги возьмётся из имени папки).")
    ap.add_argument("--prompts", default="prompts", help="Папка с extractor.txt/validator.txt/synthesizer.txt/distiller.txt")
    ap.add_argument("--out-root", default="out", help="Корневая папка результатов (у каждой книги своя подпапка)")
    ap.add_argument("--title", default=None, help="Название (только для режима с одной книгой)")
    ap.add_argument("--author", default=None, help="Автор (только для режима с одной книгой)")

    ap.add_argument("--extractor-model", default="openai/gpt-oss-20b")
    ap.add_argument("--extractor-context", type=int, default=60000)
    ap.add_argument("--extractor-max-tokens", type=int, default=4096)

    ap.add_argument("--validator-model", default="qwen/qwen3.6-27b")
    ap.add_argument("--validator-context", type=int, default=24576)
    ap.add_argument("--validator-max-tokens", type=int, default=4096)
    ap.add_argument("--synthesizer-max-tokens", type=int, default=8192)
    ap.add_argument("--distiller-max-tokens", type=int, default=2048)

    ap.add_argument("--gpu", default="max")
    ap.add_argument("--lms-path", default="lms", help="Путь к утилите lms, если её нет в PATH")
    ap.add_argument("--base-url", default="http://127.0.0.1:1234/v1")
    ap.add_argument("--temperature", type=float, default=0.2)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--retries", type=int, default=2)
    ap.add_argument("--retry-delay", type=int, default=15)

    ap.add_argument("--target-tokens", type=int, default=5500, help="Целевой размер части книги в токенах")
    ap.add_argument("--chars-per-token", type=float, default=2.0)

    ap.add_argument("--resume", dest="resume", action="store_true", default=True,
                     help="Пропускать уже готовые части/этапы (по умолчанию включено)")
    ap.add_argument("--no-resume", dest="resume", action="store_false", help="Пересчитать всё заново")
    ap.add_argument("--force", action="store_true",
                     help="Продолжать до Synthesizer/Distiller, даже если были ошибки в частях")

    args = ap.parse_args()

    if not args.book and not args.parts:
        print("Укажи --book (файл/папка с текстом книги) или --parts (папка с уже готовыми part*.txt, "
              "можно несколько раз)", file=sys.stderr)
        sys.exit(1)

    jobs = []
    if args.book:
        if os.path.isdir(args.book):
            book_files = sorted(glob.glob(os.path.join(args.book, "*.txt")))
            if not book_files:
                print(f"В папке {args.book} не найдено .txt файлов", file=sys.stderr)
                sys.exit(1)
            jobs += [{"kind": "book", "path": p} for p in book_files]
        else:
            jobs.append({"kind": "book", "path": args.book})

    if args.parts:
        for p in args.parts:
            if not os.path.isdir(p):
                print(f"Папка с частями не найдена: {p}", file=sys.stderr)
                sys.exit(1)
            jobs.append({"kind": "parts", "path": p})

    print(f"К обработке: {len(jobs)} книг(и).")
    results = {}
    for job in jobs:
        try:
            ok = process_book(job, args)
            results[job["path"]] = "OK" if ok else "ОСТАНОВЛЕНО (см. лог книги)"
        except Exception as e:
            results[job["path"]] = f"ОШИБКА: {e}"
            print(f"Критическая ошибка на {job['path']}: {e}", file=sys.stderr)
            # идём дальше к следующей книге, а не останавливаем весь батч

    print("\n=== ИТОГ ===")
    for path, status in results.items():
        print(f"{path}: {status}")


if __name__ == "__main__":
    main()
