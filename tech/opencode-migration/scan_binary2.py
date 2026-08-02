# -*- coding: utf-8 -*-
import re
import sys

path = sys.argv[1]
with open(path, "rb") as f:
    data = f.read()

text = data.decode("latin1")


def show(pattern, context=200, limit=10):
    idxs = [m.start() for m in re.finditer(pattern, text)]
    print(f"=== pattern {pattern!r}: {len(idxs)} matches ===")
    for i in idxs[:limit]:
        ctx = text[max(0, i - context): i + context]
        ctx_clean = "".join(ch if 32 <= ord(ch) < 127 else "." for ch in ctx)
        print("...", ctx_clean, "...")
        print("---")


show(re.escape("[^a-zA-Z0-9]"), context=250, limit=15)
show(re.escape(".claude"), context=150, limit=5)
show(re.escape("projects"), context=150, limit=10)
