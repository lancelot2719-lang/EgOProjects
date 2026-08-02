"""Extract finance advice from BookLM index using multilingual embeddings"""
import sys, os, pickle
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, r"D:\AI_Project")
from pathlib import Path

# Load chunks and filter to finance only
with open(r"D:\AI_Project\booklm_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

finance_chunks = [c for c in chunks if "Финанс" in c.metadata.get("source", "")]
print(f"Finance chunks: {len(finance_chunks)}", flush=True)

# Build small FAISS index with multilingual embeddings
from sentence_transformers import SentenceTransformer
print("Loading multilingual embedding model...", flush=True)
model = SentenceTransformer("intfloat/multilingual-e5-small", device="cpu")

texts = [d.page_content for d in finance_chunks]
metadatas = [d.metadata for d in finance_chunks]

# E5 models need prefix
texts_prefixed = [f"passage: {t}" for t in texts]

print(f"Generating {len(texts)} embeddings...", flush=True)
all_emb = []
batch_size = 32
for i in range(0, len(texts), batch_size):
    batch = texts_prefixed[i:i+batch_size]
    emb = model.encode(batch, show_progress_bar=False, normalize_embeddings=True)
    all_emb.extend(emb)
    print(f"  {min(i+batch_size, len(texts))}/{len(texts)}", flush=True)

# Build FAISS index
import faiss, numpy as np
dim = len(all_emb[0])
index = faiss.IndexFlatIP(dim)
index.add(np.array(all_emb).astype("float32"))

def search(query, k=30):
    q_emb = model.encode([f"query: {query}"], normalize_embeddings=True)
    scores, indices = index.search(np.array(q_emb).astype("float32"), k)
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx >= 0:
            results.append((score, texts[idx], metadatas[idx]))
    return results

# Queries to extract all finance wisdom
queries = [
    "личные финансы управление бюджетом экономия денег советы",
    "инвестиции создание капитала пассивный доход накопления",
    "заработок увеличение дохода карьерный рост деньги",
    "психология денег финансовые ошибки ловушки мышления",
    "богатство финансовое благополучие независимость успех",
    "долги кредиты как избавиться от долгов финансовая свобода",
    "сбережения инвестирование фондовый рынок ценные бумаги",
    "финансовое планирование цели бюджет учет расходов",
    "бизнес предпринимательство финансовая грамотность",
    "налоги страхование финансовая защита риски",
]

all_results = set()
for q in queries:
    print(f"\n=== {q} ===", flush=True)
    results = search(q, k=15)
    for score, text, meta in results:
        src = meta.get("source", "?")
        key = (src, text[:100])
        if key not in all_results:
            all_results.add(key)
            preview = text[:300].replace("\n", " ").strip()
            print(f"  [{score:.2f}] [{src}] {preview}", flush=True)

print(f"\n\nTotal unique results: {len(all_results)}", flush=True)
