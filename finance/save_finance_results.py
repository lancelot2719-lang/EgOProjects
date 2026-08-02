"""Save finance extraction results and use LLM to structure them"""
import sys, os, pickle, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, r"D:\AI_Project")
from pathlib import Path
from sentence_transformers import SentenceTransformer
import faiss, numpy as np

# Load and filter finance chunks
with open(r"D:\AI_Project\booklm_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)
finance_chunks = [c for c in chunks if "Финанс" in c.metadata.get("source", "")]
print(f"Finance chunks: {len(finance_chunks)}", flush=True)

# Build index with multilingual embeddings
model = SentenceTransformer("intfloat/multilingual-e5-small", device="cpu")
texts = [d.page_content for d in finance_chunks]
metadatas = [d.metadata for d in finance_chunks]
texts_prefixed = [f"passage: {t}" for t in texts]

print("Generating embeddings...", flush=True)
all_emb = []
for i in range(0, len(texts), 32):
    batch = texts_prefixed[i:i+32]
    emb = model.encode(batch, show_progress_bar=False, normalize_embeddings=True)
    all_emb.extend(emb)
    print(f"  {min(i+32, len(texts))}/{len(texts)}", flush=True)

dim = len(all_emb[0])
index = faiss.IndexFlatIP(dim)
index.add(np.array(all_emb).astype("float32"))

def search(query, k=20):
    q_emb = model.encode([f"query: {query}"], normalize_embeddings=True)
    scores, indices = index.search(np.array(q_emb).astype("float32"), k)
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx >= 0:
            results.append({"score": float(score), "source": metadatas[idx]["source"], "text": texts[idx][:500]})
    return results

# Comprehensive finance queries
queries = [
    ("upravlenie_byudzhet", "личные финансы управление бюджетом экономия советы учет расходов доходов"),
    ("investirovanie", "инвестиции создание капитала пассивный доход накопления портфель"),
    ("zarabotok_dohod", "заработок увеличение дохода карьерный рост дополнительные источники денег"),
    ("psihologiya_deneg", "психология денег финансовые ошибки ловушки мышления убеждения"),
    ("bogatstvo_uspeh", "богатство финансовое благополучие независимость успех изобилие"),
    ("dolgi_kredity", "долги кредиты как избавиться от долгов финансовая свобода выплаты"),
    ("sberezheniya_rynok", "сбережения инвестирование фондовый рынок ценные бумаги акции облигации"),
    ("fin_planirovanie", "финансовое планирование цели бюджет учет SMART"),
    ("biznes_predprinimatelstvo", "бизнес предпринимательство финансовая грамотность управление деньгами"),
    ("nalogi_strahovanie", "налоги страхование финансовая защита риски подушка безопасности"),
    ("umniy_investor", "стоимостное инвестирование Грэм Баффетт анализ ценных бумаг"),
    ("denezhnye_privychki", "денежные привычки финансовая дисциплина автоматизация сбережений"),
]

all_data = {}
for key, q in queries:
    results = search(q, k=20)
    all_data[key] = results
    print(f"{key}: {len(results)} results", flush=True)

# Save raw data
with open(r"D:\AI_Project\temp\finance_raw.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)
print(f"\nSaved raw data", flush=True)

# Now use LLM to structure
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# Prepare context - merge all unique texts
all_texts_seen = set()
merged = []
for key, results in all_data.items():
    for r in results:
        key_val = (r["source"], r["text"][:100])
        if key_val not in all_texts_seen:
            all_texts_seen.add(key_val)
            merged.append(f"[{r['source']}] {r['text']}")

context = "\n\n---\n\n".join(merged)
print(f"Context length: {len(context)} chars, {len(merged)} snippets", flush=True)

chunks_for_llm = [merged[i:i+30] for i in range(0, len(merged), 30)]
print(f"Will process in {len(chunks_for_llm)} chunks", flush=True)

all_sections = []
for ci, chunk in enumerate(chunks_for_llm):
    ctx = "\n\n---\n\n".join(chunk)
    prompt = (
        "Ты — финансовый аналитик. Из предоставленных отрывков книг извлеки КОНКРЕТНЫЕ советы, "
        "рекомендации, лайфхаки, стратегии и ключевые идеи по финансам. "
        "Сгруппируй их по темам. Для каждого совета укажи источник (название книги). "
        "Формат:\n\n"
        "## Тема\n\n"
        "- **Совет**: ...\n  *Источник*: Название книги\n\n"
        "Если в отрывках нет советов — пропусти их.\n\n"
        f"Отрывки:\n\n{ctx}"
    )
    resp = client.chat.completions.create(
        model="mistral:latest",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=4000,
    )
    result = resp.choices[0].message.content
    all_sections.append(result)
    print(f"Chunk {ci+1}/{len(chunks_for_llm)} done ({len(result)} chars)", flush=True)

final = "\n\n".join(all_sections)
with open(r"D:\AI_Project\finance_booklm.md", "w", encoding="utf-8") as f:
    f.write("# Финансовые лайфхаки, советы и стратегии из книг\n\n")
    f.write("> Извлечено из 35 книг финансовой тематики\n\n")
    f.write(final)

print(f"Saved to finance_booklm.md ({len(final)} chars)", flush=True)
