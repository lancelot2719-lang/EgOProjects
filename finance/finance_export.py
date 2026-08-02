"""Build multilingual index for finance chunks and export structured results"""
import sys, os, pickle
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, r"D:\AI_Project")
from pathlib import Path
from sentence_transformers import SentenceTransformer
import faiss, numpy as np
from collections import defaultdict

# Load finance chunks
with open(r"D:\AI_Project\booklm_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)
finance_chunks = [c for c in chunks if "Финанс" in c.metadata.get("source", "")]
print(f"Total finance chunks: {len(finance_chunks)}", flush=True)

texts = [d.page_content for d in finance_chunks]
metadatas = [d.metadata for d in finance_chunks]
texts_prefixed = [f"passage: {t}" for t in texts]

# Multilingual embeddings
model = SentenceTransformer("intfloat/multilingual-e5-small", device="cpu")
all_emb = []
for i in range(0, len(texts), 32):
    batch = texts_prefixed[i:i+32]
    emb = model.encode(batch, show_progress_bar=False, normalize_embeddings=True)
    all_emb.extend(emb)
    pct = 100 * (i + 32) // len(texts)
    print(f"Embeddings: {min(i+32, len(texts))}/{len(texts)} ({pct}%)", flush=True)

dim = len(all_emb[0])
index = faiss.IndexFlatIP(dim)
index.add(np.array(all_emb).astype("float32"))
print(f"Index built: {index.ntotal} vectors, dim={dim}", flush=True)

# Finance queries
queries = [
    ("budget", "личные финансы управление бюджетом экономия учет расходов доходов финансовая дисциплина"),
    ("invest", "инвестиции создание капитала пассивный доход накопления портфель фондовый рынок"),
    ("income", "заработок увеличение дохода карьерный рост дополнительные источники денег продажи"),
    ("psychology", "психология денег финансовые ошибки ловушки мышления убеждения установки"),
    ("wealth", "богатство финансовое благополучие независимость успех изобилие достаток"),
    ("debt", "долги кредиты как избавиться от долгов финансовая свобода выплаты проценты"),
    ("planning", "финансовое планирование цели бюджет SMART учет финансовые цели"),
    ("business", "бизнес предпринимательство управление деньгами финансовая грамотность"),
    ("habits", "денежные привычки автоматизация сбережений накопления финансовая подушка"),
    ("protection", "налоги страхование защита риски подушка безопасности финансовая защита"),
]

all_data = defaultdict(list)
seen = set()

for key, q in queries:
    q_emb = model.encode([f"query: {q}"], normalize_embeddings=True)
    scores, indices = index.search(np.array(q_emb).astype("float32"), 30)
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0: continue
        src = metadatas[idx].get("source", "?").replace(".pdf", "").replace("_", " ").strip()
        text = texts[idx][:800].replace("\n", " ").strip()
        dedup_key = src + text[:80]
        if dedup_key not in seen:
            seen.add(dedup_key)
            all_data[key].append((score, src, text))
    print(f"[{key}] found {len(all_data[key])} items", flush=True)

# Group by source for each topic
topic_names = {
    "budget": "Бюджет и учёт расходов",
    "invest": "Инвестиции и накопление капитала",
    "income": "Заработок и доход",
    "psychology": "Психология денег",
    "wealth": "Богатство и финансовое благополучие",
    "debt": "Долги и кредиты",
    "planning": "Финансовое планирование",
    "business": "Бизнес и предпринимательство",
    "habits": "Денежные привычки",
    "protection": "Защита и страхование",
}

lines = ["# Финансовые лайфхаки, советы и стратегии из книг\n"]
lines.append("> Собрано из 35 книг финансовой тематики с помощью multilingual-e5-small + Mistral 7B\n")
lines.append(f"> Всего найдено: {len(seen)} уникальных советов по 10 темам\n")
lines.append("---\n")

for key, topic in topic_names.items():
    items = sorted(all_data[key], key=lambda x: -x[0])
    lines.append(f"## {topic}\n")
    # Skip low-relevance
    for score, src, text in items:
        if score < 0.3: continue
        lines.append(f"- **{src}** (релевантность: {score:.2f})")
        lines.append(f"  {text}\n")
    lines.append("")

result = "\n".join(lines)
with open(r"D:\AI_Project\finance_booklm.md", "w", encoding="utf-8") as f:
    f.write(result)

print(f"\nDone! Saved to finance_booklm.md ({len(result)} chars, {len(seen)} items)", flush=True)
