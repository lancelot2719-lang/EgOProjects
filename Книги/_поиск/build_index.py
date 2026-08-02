#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Строит поисковый индекс по извлечённым текстам книг.

Подход: разбиение на чанки + TF-IDF (символьные и словесные н-граммы).
Нейросетевые эмбеддинги недоступны — в этой песочнице нет интернета,
поэтому sentence-transformers/FAISS установить невозможно. TF-IDF на
символьных н-граммах хорошо работает с русской морфологией (падежи,
окончания) без необходимости в стеммере.
"""
import json, re, pickle, sys
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

EXTRACTED = Path("/tmp/rag_pipeline/extracted")
INDEX_DIR = Path("/tmp/rag_pipeline/index")
INDEX_DIR.mkdir(parents=True, exist_ok=True)

CHUNK_CHARS = 2000       # ~350-400 слов, комфортно для цитирования
CHUNK_OVERLAP = 300      # перекрытие, чтобы не резать мысль пополам


TOKEN_RE = re.compile(r"[а-яёa-z0-9]+", re.I)
STEM_LEN = 6


def ru_stem_tokenizer(text: str):
    """Токенизация с обрезкой до псевдо-основы. Русский язык сильно
    флективный; обрезка до 6 символов схлопывает падежи и числа в одну
    форму без словаря и внешних зависимостей (pymorphy недоступен —
    в песочнице нет интернета для установки пакетов)."""
    out = []
    for m in TOKEN_RE.finditer(text.lower()):
        w = m.group(0)
        if len(w) < 3:
            continue
        out.append(w[:STEM_LEN])
    return out


def clean_text(t: str) -> str:
    t = t.replace("\x00", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def chunk_text(text: str, size=CHUNK_CHARS, overlap=CHUNK_OVERLAP):
    """Режем по абзацам, добирая до нужного размера — так чанки
    заканчиваются на смысловой границе, а не посреди слова."""
    paras = [p.strip() for p in text.split("\n") if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if len(cur) + len(p) + 1 <= size:
            cur += ("\n" if cur else "") + p
        else:
            if cur:
                chunks.append(cur)
            if len(p) > size:
                # длинный абзац рубим окном с перекрытием
                for i in range(0, len(p), size - overlap):
                    piece = p[i:i + size]
                    if len(piece.strip()) > 100:
                        chunks.append(piece.strip())
                cur = ""
            else:
                cur = p
    if cur:
        chunks.append(cur)
    return [c for c in chunks if len(c.strip()) >= 150]


def main():
    docs, meta = [], []
    files = sorted(EXTRACTED.rglob("*.txt"))
    print(f"Файлов для индексации: {len(files)}")

    for fp in files:
        topic = fp.parent.name
        title = fp.stem
        try:
            raw = fp.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  ! пропуск {fp.name}: {e}")
            continue
        text = clean_text(raw)
        if len(text) < 500:
            continue
        for i, ch in enumerate(chunk_text(text)):
            docs.append(ch)
            meta.append({"topic": topic, "title": title, "chunk_id": i,
                         "file": str(fp)})

    print(f"Всего чанков: {len(docs):,}")

    # Индексируем по «псевдо-основам»: обрезаем слова до 6 символов.
    # Это дёшево снимает русскую морфологию (инвестор/инвестора/инвестору
    # -> инвест), даёт устойчивость к падежам почти как символьные н-граммы,
    # но индекс выходит в ~10 раз компактнее (символьный вариант занимал 1.2 ГБ).
    print("Строю TF-IDF (псевдо-основы слов)...")
    word_vec = TfidfVectorizer(
        analyzer="word", tokenizer=ru_stem_tokenizer, token_pattern=None,
        ngram_range=(1, 2), min_df=2, max_df=0.5,
        max_features=400_000, sublinear_tf=True, lowercase=True,
        dtype=np.float32,
    )
    word_mat = word_vec.fit_transform(docs)
    print(f"  словарь: {len(word_vec.vocabulary_):,}, матрица: {word_mat.shape}, "
          f"nnz={word_mat.nnz:,}")

    print("Сохраняю индекс...")
    with open(INDEX_DIR / "index.pkl", "wb") as f:
        pickle.dump({
            "docs": docs, "meta": meta,
            "word_vec": word_vec, "word_mat": word_mat,
        }, f, protocol=4)

    stats = {
        "n_files": len(files), "n_chunks": len(docs),
        "n_chars": sum(len(d) for d in docs),
        "topics": sorted({m["topic"] for m in meta}),
        "books": sorted({m["title"] for m in meta}),
    }
    (INDEX_DIR / "stats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")

    size_mb = (INDEX_DIR / "index.pkl").stat().st_size / 1024 / 1024
    print(f"Готово. Индекс: {size_mb:.1f} МБ, {len(docs):,} чанков, "
          f"{len(stats['books'])} книг, {len(stats['topics'])} тем.")


if __name__ == "__main__":
    main()
