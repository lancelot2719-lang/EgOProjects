#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Поиск по библиотеке книг.

Использование:
    python3 search.py "как формировать привычки"
    python3 search.py "запас прочности" --topic Финансы --top 10
    python3 search.py "прокрастинация" --book "Атомные"

Возвращает релевантные фрагменты с указанием книги и темы.
"""
import argparse, pickle, re, sys, textwrap
from pathlib import Path

import numpy as np
from sklearn.metrics.pairwise import linear_kernel

INDEX_PATH = Path(__file__).parent / "index" / "index.pkl"

TOKEN_RE = re.compile(r"[а-яёa-z0-9]+", re.I)
STEM_LEN = 6


def ru_stem_tokenizer(text: str):
    out = []
    for m in TOKEN_RE.finditer(text.lower()):
        w = m.group(0)
        if len(w) < 3:
            continue
        out.append(w[:STEM_LEN])
    return out


_INDEX = None


def load_index():
    global _INDEX
    if _INDEX is None:
        with open(INDEX_PATH, "rb") as f:
            _INDEX = pickle.load(f)
    return _INDEX


def search(query, top=8, topic=None, book=None, per_book_limit=2):
    idx = load_index()
    docs, meta = idx["docs"], idx["meta"]
    qv = idx["word_vec"].transform([query])
    scores = linear_kernel(qv, idx["word_mat"]).ravel()

    # Фильтры по теме/книге применяем как маску, а не постфильтром,
    # иначе при узком фильтре в топе не останется ничего.
    mask = np.ones(len(docs), dtype=bool)
    if topic:
        tl = topic.lower()
        mask &= np.array([tl in m["topic"].lower() for m in meta])
    if book:
        bl = book.lower()
        mask &= np.array([bl in m["title"].lower() for m in meta])
    scores = np.where(mask, scores, -1.0)

    order = np.argsort(-scores)
    results, per_book = [], {}
    for i in order:
        if scores[i] <= 0:
            break
        title = meta[i]["title"]
        # не даём одной книге занять всю выдачу
        if per_book.get(title, 0) >= per_book_limit:
            continue
        per_book[title] = per_book.get(title, 0) + 1
        results.append({
            "score": float(scores[i]),
            "topic": meta[i]["topic"],
            "title": title,
            "text": docs[i],
        })
        if len(results) >= top:
            break
    return results


def main():
    ap = argparse.ArgumentParser(description="Поиск по библиотеке книг")
    ap.add_argument("query", help="поисковый запрос")
    ap.add_argument("--top", type=int, default=8, help="сколько фрагментов вернуть")
    ap.add_argument("--topic", help="ограничить темой (подстрока)")
    ap.add_argument("--book", help="ограничить книгой (подстрока названия)")
    ap.add_argument("--full", action="store_true", help="печатать фрагмент целиком")
    args = ap.parse_args()

    res = search(args.query, top=args.top, topic=args.topic, book=args.book)
    if not res:
        print("Ничего не найдено.")
        return
    for i, r in enumerate(res, 1):
        print(f"\n{'='*78}")
        print(f"[{i}] {r['title']}")
        print(f"    тема: {r['topic']}   релевантность: {r['score']:.3f}")
        print(f"{'-'*78}")
        body = r["text"] if args.full else r["text"][:700]
        print(textwrap.fill(body, width=78))
        if not args.full and len(r["text"]) > 700:
            print("    [...]")


if __name__ == "__main__":
    main()
