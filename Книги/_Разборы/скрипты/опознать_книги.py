#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Опознать книги с нечитаемыми именами файлов (1.pdf, 56786282.pdf, ff06f7b7-....pdf).

Берёт первые страницы такого файла и просит локальную модель определить
автора и название. Задача простая — локальная модель справляется хорошо.

Запуск (из папки _Разборы):
    ollama serve
    ollama pull qwen2.5:14b-instruct
    python скрипты\\опознать_книги.py "D:\\AI_Project\\Книги"

Результат: файл «опознанные_книги.csv» рядом со скриптом.
"""
import csv
import json
import re
import sys
import urllib.request
from pathlib import Path

MODEL = "qwen2.5:14b-instruct"
OLLAMA_URL = "http://localhost:11434/api/generate"
HEAD_CHARS = 6000          # первых символов книги обычно хватает

# Имена, которые считаем «нечитаемыми»: только цифры, hex-идентификаторы,
# служебные обрывки — то есть по имени невозможно понять, что это за книга.
BAD_NAME = re.compile(
    r"^(\d+|[0-9a-f]{6,}|[0-9a-f\-]{20,}|_+|\W*)$", re.I)


def looks_unidentified(stem: str) -> bool:
    s = stem.strip()
    if BAD_NAME.match(s):
        return True
    letters = re.sub(r"[^А-Яа-яA-Za-z]", "", s)
    return len(letters) < 4          # почти нет букв — опознать нельзя


def extract_head(path: Path) -> str:
    """Достаёт начало текста из PDF или TXT."""
    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8", errors="replace")[:HEAD_CHARS]
    try:
        import pypdf
        reader = pypdf.PdfReader(str(path))
        parts = []
        for page in reader.pages[:6]:
            parts.append(page.extract_text() or "")
            if sum(len(p) for p in parts) > HEAD_CHARS:
                break
        return "\n".join(parts)[:HEAD_CHARS]
    except Exception as e:
        return f"__ОШИБКА__ {e}"


def ask(prompt: str) -> str:
    payload = json.dumps({
        "model": MODEL, "prompt": prompt, "stream": False,
        "options": {"num_ctx": 8192, "temperature": 0.1},
    }).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode("utf-8")).get("response", "").strip()


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else r"D:\AI_Project\Книги")
    if not root.is_dir():
        sys.exit(f"Не найдена папка: {root}")

    targets = [
        f for f in root.rglob("*")
        if f.is_file()
        and f.suffix.lower() in (".pdf", ".txt", ".fb2", ".epub")
        and looks_unidentified(f.stem)
    ]
    print(f"Файлов с нечитаемыми именами: {len(targets)}\n")

    rows = []
    for i, f in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {f.name} ... ", end="", flush=True)
        head = extract_head(f)
        if head.startswith("__ОШИБКА__") or len(head.strip()) < 100:
            print("не удалось прочитать текст")
            rows.append([str(f), f.name, "", "", "не удалось прочитать"])
            continue
        prompt = (
            "Ниже начало книги. Определи автора и точное название.\n"
            "Ответь СТРОГО в формате, без пояснений:\n"
            "АВТОР: <автор или «неизвестно»>\n"
            "НАЗВАНИЕ: <название или «неизвестно»>\n"
            "УВЕРЕННОСТЬ: <высокая|средняя|низкая>\n\n"
            "=== НАЧАЛО КНИГИ ===\n" + head
        )
        try:
            ans = ask(prompt)
            g = lambda k: (re.search(rf"{k}:\s*(.+)", ans) or [None, ""])[1].strip()
            author, title, conf = g("АВТОР"), g("НАЗВАНИЕ"), g("УВЕРЕННОСТЬ")
            print(f"{author} — {title} ({conf})")
            rows.append([str(f), f.name, author, title, conf])
        except Exception as e:
            print(f"ОШИБКА: {e}")
            rows.append([str(f), f.name, "", "", f"ошибка: {e}"])

    out = Path(__file__).resolve().parent.parent / "опознанные_книги.csv"
    with open(out, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["путь", "имя файла", "автор", "название", "уверенность"])
        w.writerows(rows)
    print(f"\nГотово: {out}")


if __name__ == "__main__":
    main()
