# -*- coding: utf-8 -*-
"""Ищет в бинарнике claude.exe строки/регэкспы, отвечающие за кодирование
пути проекта в имя папки истории (~/.claude/projects/<encoded>)."""
import re
import sys

path = sys.argv[1]
with open(path, "rb") as f:
    data = f.read()

text = data.decode("latin1")

# ищем разные варианты, которые обычно встречаются в таких функциях
patterns = [
    r"[^a-zA-Z0-9]{0,5}a-zA-Z0-9[^a-zA-Z0-9]{0,10}",
    r"replace\([^)]{0,60}\)",
]

seen = set()
for pat in patterns:
    for m in re.finditer(pat, text):
        s = m.group(0)
        if s not in seen:
            seen.add(s)

# более узкий и полезный поиск: контекст вокруг "a-zA-Z0-9"
idxs = [m.start() for m in re.finditer(r"a-zA-Z0-9", text)]
print(f"Найдено вхождений 'a-zA-Z0-9': {len(idxs)}")
for i in idxs[:20]:
    ctx = text[max(0, i - 80): i + 80]
    ctx_clean = "".join(ch if 32 <= ord(ch) < 127 else "." for ch in ctx)
    print("...", ctx_clean, "...")
    print("---")
