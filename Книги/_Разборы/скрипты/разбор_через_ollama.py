#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Пакетный разбор книг через локальную Ollama.

Запуск (из папки _Разборы):
    ollama serve                       # в отдельном окне, если не запущена
    ollama pull qwen2.5:14b-instruct
    python скрипты\\разбор_через_ollama.py

Скрипт берёт тексты из «тексты_для_NotebookLM», прогоняет через локальную модель
и складывает результат в «новые_разборы». Уже готовые файлы пропускает,
поэтому прерывать и продолжать можно свободно.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

# ── настройки ────────────────────────────────────────────────────────────────
MODEL = "qwen2.5:14b-instruct"     # можно заменить на любую установленную
OLLAMA_URL = "http://localhost:11434/api/generate"
CTX = 16384          # размер контекста; при нехватке VRAM уменьшите до 8192
TIMEOUT = 1800       # секунд на одну книгу

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "тексты_для_NotebookLM"
DST = BASE / "новые_разборы"
PROMPT_FILE = BASE / "ПРОМПТ_для_NotebookLM.txt"

# Локальная модель не умеет искать по всей книге, поэтому готовим выжимку:
# начало + равномерные срезы + концовка.
HEAD = 25_000
SLICE = 3_500
N_SLICES = 10
TAIL = 8_000


def make_digest(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text.replace("\x00", " "))
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    n = len(text)
    if n <= HEAD + TAIL + SLICE * N_SLICES:
        return text
    out = [text[:HEAD]]
    start, end = HEAD, n - TAIL
    step = (end - start) // N_SLICES
    for i in range(N_SLICES):
        p = start + i * step
        out.append(f"\n\n[...фрагмент ~{int(100*p/n)}% книги...]\n")
        out.append(text[p:p + SLICE])
    out.append("\n\n[...концовка книги...]\n")
    out.append(text[-TAIL:])
    return "".join(out)


def ask_ollama(prompt: str) -> str:
    payload = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"num_ctx": CTX, "temperature": 0.3},
    }).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read().decode("utf-8")).get("response", "")


def main():
    if not SRC.is_dir():
        sys.exit(f"Не найдена папка с текстами: {SRC}")
    DST.mkdir(exist_ok=True)
    template = PROMPT_FILE.read_text(encoding="utf-8")

    files = sorted(SRC.glob("*.txt"))
    print(f"Книг к обработке: {len(files)}   модель: {MODEL}\n")

    for i, f in enumerate(files, 1):
        out = DST / (f.stem + ".md")
        if out.exists() and out.stat().st_size > 2000:
            print(f"[{i}/{len(files)}] пропуск (уже готово): {f.stem}")
            continue

        print(f"[{i}/{len(files)}] {f.stem} ... ", end="", flush=True)
        try:
            digest = make_digest(f.read_text(encoding="utf-8", errors="replace"))
            prompt = (
                template
                + "\n\n=== ТЕКСТ КНИГИ (выжимка: начало, срезы по всей книге, концовка) ===\n\n"
                + digest
            )
            answer = ask_ollama(prompt)
            if len(answer.strip()) < 500:
                print("ОШИБКА: слишком короткий ответ, пропускаю")
                continue
            out.write_text(answer, encoding="utf-8")
            print(f"готово, {len(answer.split())} слов")
        except Exception as e:
            print(f"ОШИБКА: {e}")

    print(f"\nРезультаты: {DST}")


if __name__ == "__main__":
    main()
