#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcribe_books.py — пакетная транскрибация аудиокниг (mp3) в текст.

Поддерживает два движка:
  - faster-whisper   (Whisper large-v3 / large-v3-turbo через CTranslate2)
  - gigaam            (специализированная модель для русского языка, Сбер —
                        для русской речи обычно заметно точнее Whisper)

БЫСТРОЕ СРАВНЕНИЕ движков на 1-2 файлах (рекомендуется сделать в первую очередь):

    python transcribe_books.py --input-dir "D:\путь\к\mp3" --engine faster-whisper --limit 2 --output-dir ".\test_fw"
    python transcribe_books.py --input-dir "D:\путь\к\mp3" --engine gigaam         --limit 2 --output-dir ".\test_giga"

Сравните тексты в test_fw/ и test_giga/ на слух/глаз, выберите победителя.

ПОЛНЫЙ ПРОГОН выбранным движком:

    python transcribe_books.py --input-dir "D:\путь\к\mp3" --engine gigaam --output-dir "D:\путь\к\результату"

Скрипт НЕ трогает исходные mp3 — только читает их и пишет .txt рядом или в
указанную output-папку. Уже готовые .txt по умолчанию не перезаписываются
(можно продолжить прерванный прогон) — флаг --overwrite включает перезапись.

──────────────────────────────────────────────────────────────────────────
УСТАНОВКА

faster-whisper:
    pip install faster-whisper

gigaam:
    git clone https://github.com/salute-developers/GigaAM.git
    cd GigaAM
    pip install -e ".[torch]"
    pip install -e ".[longform]"     # для длинных файлов (VAD-нарезка)

    # для longform нужен бесплатный токен HuggingFace и разовое согласие
    # с условиями модели pyannote/segmentation-3.0 на huggingface.co
    #   1) зарегистрироваться на huggingface.co, получить токен (Settings -> Access Tokens)
    #   2) открыть https://huggingface.co/pyannote/segmentation-3.0 и нажать "Agree"
    #   3) задать переменную окружения HF_TOKEN (см. --hf-token или заранее в системе)

Оба движка:
    ffmpeg должен быть установлен и доступен в PATH.

Модели скачиваются автоматически при первом запуске (нужен интернет один раз,
дальше работает офлайн).
──────────────────────────────────────────────────────────────────────────
"""

import argparse
import os
import sys
import time
import traceback
from pathlib import Path


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def find_mp3_files(input_dir: Path, recursive: bool):
    pattern = "**/*.mp3" if recursive else "*.mp3"
    return sorted(input_dir.glob(pattern), key=lambda p: p.name.lower())


# ──────────────────────────────────────────────────────────────────────────
# faster-whisper
# ──────────────────────────────────────────────────────────────────────────

def run_faster_whisper(files, output_dir: Path, model_name: str, device: str,
                        compute_type: str, language: str, overwrite: bool):
    from faster_whisper import WhisperModel

    log(f"Загружаю faster-whisper модель '{model_name}' "
        f"(device={device}, compute_type={compute_type})...")
    model = WhisperModel(model_name, device=device, compute_type=compute_type)
    log("Модель загружена.")

    for i, mp3_path in enumerate(files, 1):
        out_path = output_dir / (mp3_path.stem + ".txt")
        if out_path.exists() and not overwrite:
            log(f"[{i}/{len(files)}] Пропускаю (уже есть .txt): {mp3_path.name}")
            continue

        log(f"[{i}/{len(files)}] Транскрибирую: {mp3_path.name}")
        t0 = time.time()
        try:
            segments, info = model.transcribe(
                str(mp3_path),
                language=language,
                vad_filter=True,   # пропускает тишину/музыку — быстрее и чище текст
                beam_size=5,
            )
            text = "\n".join(seg.text.strip() for seg in segments if seg.text.strip())
            out_path.write_text(text, encoding="utf-8")
            dt = time.time() - t0
            log(f"    готово за {dt:.0f} сек | язык: {info.language} "
                f"(p={info.language_probability:.2f}) | символов: {len(text)}")
        except Exception as e:
            log(f"    ОШИБКА на файле {mp3_path.name}: {e}")
            (output_dir / (mp3_path.stem + ".ERROR.txt")).write_text(
                traceback.format_exc(), encoding="utf-8"
            )


# ──────────────────────────────────────────────────────────────────────────
# GigaAM
# ──────────────────────────────────────────────────────────────────────────

def run_gigaam(files, output_dir: Path, model_name: str, device: str, overwrite: bool):
    import gigaam

    log(f"Загружаю GigaAM модель '{model_name}' (device={device})...")
    model = gigaam.load_model(model_name, device=device)
    log("Модель загружена.")

    for i, mp3_path in enumerate(files, 1):
        out_path = output_dir / (mp3_path.stem + ".txt")
        if out_path.exists() and not overwrite:
            log(f"[{i}/{len(files)}] Пропускаю (уже есть .txt): {mp3_path.name}")
            continue

        log(f"[{i}/{len(files)}] Транскрибирую (longform, VAD): {mp3_path.name}")
        t0 = time.time()
        try:
            result = model.transcribe_longform(str(mp3_path))
            # result — список сегментов с атрибутами .start / .end / .text
            text = "\n".join(seg.text.strip() for seg in result if getattr(seg, "text", "").strip())
            out_path.write_text(text, encoding="utf-8")
            dt = time.time() - t0
            log(f"    готово за {dt:.0f} сек | сегментов: {len(result)} | символов: {len(text)}")
        except Exception as e:
            log(f"    ОШИБКА на файле {mp3_path.name}: {e}")
            (output_dir / (mp3_path.stem + ".ERROR.txt")).write_text(
                traceback.format_exc(), encoding="utf-8"
            )


# ──────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Пакетная транскрибация аудиокниг (mp3 -> txt) через faster-whisper или GigaAM",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--input-dir", required=True, help="Папка с mp3-файлами")
    parser.add_argument("--output-dir", default=None,
                         help="Куда сохранять .txt (по умолчанию — та же папка, что input-dir)")
    parser.add_argument("--engine", choices=["faster-whisper", "gigaam"], required=True)
    parser.add_argument("--model", default=None,
                         help="faster-whisper: large-v3 / large-v3-turbo / medium (по умолчанию large-v3-turbo). "
                              "gigaam: v3_e2e_rnnt / v3_rnnt / v2_rnnt (по умолчанию v3_e2e_rnnt).")
    parser.add_argument("--device", default="cuda", help="cuda или cpu (по умолчанию cuda)")
    parser.add_argument("--compute-type", default="float16",
                         help="Только faster-whisper: float16 / int8_float16 / int8 (по умолчанию float16)")
    parser.add_argument("--language", default="ru", help="Только faster-whisper (по умолчанию ru)")
    parser.add_argument("--hf-token", default=None,
                         help="Только gigaam longform: токен HuggingFace (иначе берётся из HF_TOKEN)")
    parser.add_argument("--recursive", action="store_true", help="Искать mp3 и в подпапках")
    parser.add_argument("--limit", type=int, default=None,
                         help="Обработать только первые N файлов (удобно для сравнения движков)")
    parser.add_argument("--files", nargs="*", default=None,
                         help="Обработать только эти файлы (имена внутри input-dir) вместо всей папки")
    parser.add_argument("--overwrite", action="store_true", help="Перезаписывать уже готовые .txt")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    if not input_dir.is_dir():
        log(f"Папка не найдена: {input_dir}")
        sys.exit(1)

    output_dir = Path(args.output_dir) if args.output_dir else input_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.files:
        files = [input_dir / f for f in args.files]
        missing = [f for f in files if not f.exists()]
        if missing:
            log("Не найдены файлы: " + ", ".join(str(m) for m in missing))
            sys.exit(1)
    else:
        files = find_mp3_files(input_dir, args.recursive)

    if args.limit:
        files = files[: args.limit]

    if not files:
        log("Не найдено ни одного mp3-файла — проверьте --input-dir / --recursive.")
        sys.exit(0)

    if args.hf_token:
        os.environ["HF_TOKEN"] = args.hf_token

    log(f"Найдено файлов: {len(files)} | движок: {args.engine} | результат -> {output_dir}")
    t_start = time.time()

    if args.engine == "faster-whisper":
        model_name = args.model or "large-v3-turbo"
        run_faster_whisper(files, output_dir, model_name, args.device,
                            args.compute_type, args.language, args.overwrite)
    else:
        if not os.environ.get("HF_TOKEN"):
            log("ВНИМАНИЕ: переменная HF_TOKEN не задана — transcribe_longform (VAD) может упасть "
                "с ошибкой доступа. См. раздел УСТАНОВКА в шапке файла.")
        model_name = args.model or "v3_e2e_rnnt"
        run_gigaam(files, output_dir, model_name, args.device, args.overwrite)

    log(f"Готово. Всего затрачено: {(time.time() - t_start) / 60:.1f} мин.")


if __name__ == "__main__":
    main()
