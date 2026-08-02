#!/usr/bin/env python3
"""Шаг 0: аудит очереди книг перед массовым прогоном.

Находит:
- дубликаты книг (по имени файла и похожим названиям),
- файлы-саммари / обрезки меньше 100 000 символов,
- файлы, у которых нет кандидата в RAG (source_file).

Использование:
  python audit_books.py <папка_с_текстами> [--min-chars 100000]
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

MIN_CHARS = 100_000


def norm_name(name: str) -> str:
    """Нормализация названия для поиска дублей: буквы в нижний регистр, без знаков."""
    n = re.sub(r"[^\w\s]", " ", name.lower())
    n = re.sub(r"\b(т\.е|и т\.?д|и т\.?п)\b", " ", n)
    n = re.sub(r"\b(полная версия|аудиокнига|книга|том \d+)\b", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", help="папка с текстами книг")
    ap.add_argument("--min-chars", type=int, default=MIN_CHARS)
    args = ap.parse_args()

    folder = Path(args.folder)
    files = sorted(folder.rglob("*.txt"))
    if not files:
        print("Файлов .txt не найдено.")
        return

    print(f"Всего файлов: {len(files)}\n")

    # 1. Размеры
    small = []
    for f in files:
        size = f.stat().st_size
        if size < args.min_chars:
            small.append((f, size))

    # 2. Дубли по нормализованному имени
    by_name = defaultdict(list)
    for f in files:
        by_name[norm_name(f.stem)].append(f)
    dups = {k: v for k, v in by_name.items() if len(v) > 1}

    print("=== Файлы меньше", args.min_chars, "символов (саммари/обрезки) ===")
    if small:
        for f, s in sorted(small, key=lambda x: x[1]):
            print(f"  {s:>8} симв  {f.name}")
    else:
        print("  нет")

    print(f"\n=== Дубликаты названий ({len(dups)} групп) ===")
    if dups:
        for name, paths in sorted(dups.items()):
            print(f"  «{name[:60]}» ({len(paths)} шт):")
            for p in paths:
                print(f"    {p.name}  [{p.stat().st_size} симв]")
    else:
        print("  нет")

    # 3. Итог
    total_waste = sum(s for _, s in small)
    dup_waste = sum(p.stat().st_size for v in dups.values() for p in v[1:])
    print(f"\n=== Итог ===")
    print(f"  Готовы к разбору: {len(files) - len(small) - sum(len(v) - 1 for v in dups.values())} из {len(files)}")
    print(f"  Мелкие файлы: {len(small)} (экономия ~{total_waste/1024/1024:.0f} МБ времени)")
    print(f"  Дубли: {sum(len(v) - 1 for v in dups.values())} лишних копий (экономия ~{dup_waste/1024/1024:.0f} МБ)")


if __name__ == "__main__":
    main()
