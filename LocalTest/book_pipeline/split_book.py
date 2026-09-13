#!/usr/bin/env python3
"""
Нарезает книгу (txt) на части заданного примерного размера в токенах,
режет по границам абзацев, чтобы не рвать предложения.

Использование:
    python split_book.py book.txt --out parts/ --target-tokens 8000

По умолчанию цель — 8000 токенов на часть. Это с запасом:
- Extractor грузится с --context-length=60000 (GPT-OSS-20B) — часть+промт+ответ влезут многократно.
- Validator грузится с --context-length=32000 (Qwen3.8-27B) — туда одновременно идут
  исходный текст части (~8000 ток.) + вывод Extractor по ней (обычно 3000-6000 ток.) +
  сам промт Validator (~800 ток.) — итого около 12000-15000, с большим запасом до 32000.

Точный подсчёт токенов без токенизатора конкретной модели невозможен, поэтому используется
консервативная оценка символов на токен (задаётся --chars-per-token). Для русского текста
токенизаторы обычно менее эффективны, чем для английского, поэтому по умолчанию взято
консервативное значение 2.3 символа/токен — лучше сделать часть чуть меньше, чем словить
overflow. Если после теста видишь, что реальный расход токенов ниже/выше — поправь этот
параметр и перезапусти нарезку.
"""

import argparse
import os
import re


def split_into_paragraphs(text: str) -> list[str]:
    # Абзацы — по одному или более пустых строк
    paras = re.split(r"\n\s*\n", text)
    return [p.strip() for p in paras if p.strip()]


def pack_paragraphs(paragraphs: list[str], max_chars: int) -> list[str]:
    parts = []
    current: list[str] = []
    current_len = 0

    for para in paragraphs:
        para_len = len(para) + 2  # + разделитель \n\n

        if current and current_len + para_len > max_chars:
            parts.append("\n\n".join(current))
            current = []
            current_len = 0

        # Если один абзац сам по себе больше лимита (редко, но бывает — большая глава без разбивки),
        # режем его по предложениям, чтобы не потерять текст и не превысить лимит одной части.
        if para_len > max_chars:
            sentences = re.split(r"(?<=[.!?…])\s+", para)
            buf = []
            buf_len = 0
            for sent in sentences:
                s_len = len(sent) + 1
                if buf and buf_len + s_len > max_chars:
                    parts.append(" ".join(buf))
                    buf, buf_len = [], 0
                buf.append(sent)
                buf_len += s_len
            if buf:
                current = [" ".join(buf)]
                current_len = len(current[0])
            continue

        current.append(para)
        current_len += para_len

    if current:
        parts.append("\n\n".join(current))

    return parts


def main():
    ap = argparse.ArgumentParser(description="Разбить книгу на части под лимит контекста локальной модели")
    ap.add_argument("input", help="Путь к txt-файлу книги")
    ap.add_argument("--out", default="parts", help="Папка для частей (по умолчанию ./parts)")
    ap.add_argument("--target-tokens", type=int, default=8000, help="Целевой размер части в токенах")
    ap.add_argument("--chars-per-token", type=float, default=2.3,
                     help="Оценка символов на токен (меньше = более консервативная нарезка)")
    args = ap.parse_args()

    max_chars = int(args.target_tokens * args.chars_per_token)

    with open(args.input, "r", encoding="utf-8") as f:
        text = f.read()

    paragraphs = split_into_paragraphs(text)
    parts = pack_paragraphs(paragraphs, max_chars)

    os.makedirs(args.out, exist_ok=True)
    for i, part in enumerate(parts, start=1):
        path = os.path.join(args.out, f"part{i:03d}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(part)

    total_chars = sum(len(p) for p in parts)
    print(f"Книга разбита на {len(parts)} частей в папке '{args.out}/'")
    print(f"Средний размер части: ~{total_chars // max(len(parts),1)} символов "
          f"(~{int(total_chars / max(len(parts),1) / args.chars_per_token)} токенов)")
    print("Проверь на первой части реальный расход токенов в логе LM Studio "
          "(строка 'prompt processing, n_tokens = ...') — если сильно отличается от цели, "
          "поправь --chars-per-token и перезапусти нарезку.")


if __name__ == "__main__":
    main()
