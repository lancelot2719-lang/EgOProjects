"""Пайплайн разбора книги (v5, максимальный режим):
- B1/B2/B3 ПАРАЛЛЕЛЬНО (threads) + keep_alive
- RAG-проверка идей (каждая идея подтверждается поиском в тексте)
- Автопроверка цитат скриптом (check_quotes.py)
- Судья: Claude Opus 5 через Anthropic API (если ключ в temp/.env), иначе qwen3.5
- Сборка B4 + итоговый отчёт

Запуск:  python pipeline.py <книга.txt> [--author "Автор"] [--title "Название"]
                              [--rag-source имя_файла_в_RAG] [--no-claude]
"""
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3.5:latest"
CTX = 32768
CTX_C = 32768
TIMEOUT = 2400

# Пути: скрипт лежит в .agents/skills/book-analysis/scripts/pipeline.py
SKILL_ROOT = Path(__file__).resolve().parent.parent
PROMPTS = SKILL_ROOT / "prompts"
SKRIPTS = SKILL_ROOT / "scripts"
TMP = Path(r"D:\AI_Project\temp\book_pipeline")
TMP.mkdir(parents=True, exist_ok=True)

# ============ КОНФИГ КНИГИ (переопределяется аргументами) ============
if len(sys.argv) > 1:
    BOOK_SRC = Path(sys.argv[1])
else:
    print("Ошибка: укажите путь к тексту книги: python pipeline.py <книга.txt>")
    sys.exit(1)

BOOK_TITLE_AUTHOR = "Адам Смит"
BOOK_TITLE_NAME = BOOK_SRC.stem
RAG_SOURCE_FILE = None

i = 2
while i < len(sys.argv):
    a = sys.argv[i]
    if a == "--author" and i + 1 < len(sys.argv):
        BOOK_TITLE_AUTHOR = sys.argv[i + 1]; i += 2
    elif a == "--title" and i + 1 < len(sys.argv):
        BOOK_TITLE_NAME = sys.argv[i + 1]; i += 2
    elif a == "--rag-source" and i + 1 < len(sys.argv):
        RAG_SOURCE_FILE = sys.argv[i + 1]; i += 2
    else:
        i += 1

# Digest: HEAD 25K + 12 срезов × 3K + TAIL 8K ≈ 69 КБ (~28K токенов) — покрытие ~7% толстой книги
HEAD, SLICE, N_SLICES, TAIL = 25_000, 3_000, 12, 8_000

RAG_QUESTIONS = [
    "Главная тема книги, ключевые идеи и тезисы",
    "Основные термины, концепции и их определения",
    "Практические рекомендации, советы, методики из книги",
    "Ключевые факты, цифры, статистика, примеры",
    "Критика автором других подходов, ограничения теории",
    "Исторический контекст, биография, источники вдохновения",
    "Аргументы за и против основной теории",
    "Связи с другими темами, концепциями, областями",
]

_ollama_lock = threading.Lock()  # Ollama не любит одновременные запросы


# ============ ЯДРО ============
def make_digest(text):
    text = re.sub(r"[ \t]+", " ", text.replace("\x00", " "))
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    n = len(text)
    if n <= HEAD + TAIL + SLICE * N_SLICES:
        return text
    out = [text[:HEAD]]
    start, end = HEAD, n - TAIL
    step = (end - start) // N_SLICES
    for i in range(N_SLICES):
        p = start + i * step
        out.append(f"\n\n[...фрагмент ~{int(100*p/n)}% книги...]\n")
        out.append(text[p:p + SLICE])
    out.append("\n\n[...концовка книги...]\n")
    out.append(text[-TAIL:])
    return "".join(out)


def ask_ollama(prompt, model=MODEL, ctx=CTX, temp=0.3):
    payload = {
        "model": model, "prompt": prompt, "stream": False, "think": False,
        "keep_alive": "30m",
        "options": {"num_ctx": ctx, "temperature": temp},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=data, headers={"Content-Type": "application/json"})
    with _ollama_lock:  # сериализуем, чтобы не переполнять VRAM
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return json.loads(r.read().decode("utf-8")).get("response", "")


def ask_claude(prompt, temp=0.2, max_tokens=8000):
    """Claude Opus 5 через Anthropic API. Ключ из temp/.env: ANTHROPIC_API_KEY=..."""
    env_path = Path(r"D:\AI_Project\temp\.env")
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key and env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("ANTHROPIC_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        return None

    # Пробуем актуальные ID моделей Opus
    models = ["claude-opus-5-0", "claude-opus-5-20260101", "claude-opus-4-0",
              "claude-opus-4-20250514", "claude-3-7-sonnet-20250219"]
    for model_id in models:
        payload = {
            "model": model_id,
            "max_tokens": max_tokens,
            "temperature": temp,
            "messages": [{"role": "user", "content": prompt}],
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages", data=data,
            headers={
                "Content-Type": "application/json",
                "x-api-key": key,
                "anthropic-version": "2023-06-01",
            })
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                resp = json.loads(r.read().decode("utf-8"))
                return "".join(
                    b.get("text", "") for b in resp.get("content", [])
                    if b.get("type") == "text")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")[:300]
            if "model" in body.lower() or e.code == 404:
                continue  # модель не найдена — пробуем следующую
            print(f"  [claude] ошибка {e.code}: {body}")
            return ""
        except Exception as e:
            print(f"  [claude] ошибка: {e}")
            return ""
    print("  [claude] ни одна модель Opus не найдена, проверьте ID модели")
    return ""


def load_prompt(name):
    return (PROMPTS / name).read_text(encoding="utf-8")


def save(name, content):
    (TMP / name).write_text(content, encoding="utf-8")
    print(f"  [saved] {name} ({len(content)//1024} KB, {len(content.split())} words)")


def load(name):
    p = TMP / name
    return p.read_text(encoding="utf-8") if p.exists() else ""


def run(name, prompt, save_name=None, ctx=CTX, temp=0.3, prompt_file=None):
    existing = load(save_name or name)
    if existing and prompt_file:
        # Инвалидация: если промпт новее checkpoint — пересобрать шаг
        pt = (PROMPTS / prompt_file).stat().st_mtime
        ct = (TMP / (save_name or name)).stat().st_mtime
        if pt > ct:
            print(f"[stale] {name}: промпт новее checkpoint ({prompt_file}), пересобираю")
            existing = ""
    if existing:
        print(f"[skip] {name}")
        return existing
    print(f"[run]  {name} ...", flush=True)
    t0 = time.time()
    ans = ask_ollama(prompt, ctx=ctx, temp=temp)
    print(f"  -> {len(ans.split())} words, {(time.time()-t0)/60:.1f} min")
    save(save_name or name, ans)
    return ans


def run_parallel(steps):
    """Запускает шаги параллельно в потоках (Ollama сериализует сам)."""
    results = {}
    threads = []

    def worker(step, fname, sname):
        existing = load(sname)
        if existing:
            pt = (PROMPTS / fname).stat().st_mtime
            ct = (TMP / sname).stat().st_mtime
            if pt > ct:
                print(f"[stale] {sname}: промпт новее checkpoint ({fname}), пересобираю")
                existing = ""
        if existing:
            results[sname] = existing
            print(f"[skip] {sname}")
            return
        p = load_prompt(fname).replace("{ТЕКСТ}", digest)
        print(f"[run]  {sname} ...", flush=True)
        t0 = time.time()
        ans = ask_ollama(p, ctx=CTX)
        print(f"  -> {sname}: {len(ans.split())} words, {(time.time()-t0)/60:.1f} min")
        save(sname, ans)
        results[sname] = ans

    for step, fname, sname in steps:
        t = threading.Thread(target=worker, args=(step, fname, sname))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return results


# ============ ПАЙПЛАЙН ============
t_start = time.time()

print("=== ПАЙПЛАЙН v5 (максимальный 2.0) ===")
print(f"Книга: {BOOK_SRC.name}")
digest = make_digest(BOOK_SRC.read_text(encoding="utf-8", errors="replace"))
save("digest.txt", digest)
full_text = BOOK_SRC.read_text(encoding="utf-8", errors="replace")

# --- Шаг 1: B1-B3 параллельно ---
print("\n--- Шаг 1: multi-pass B1-B3 (параллельно) ---")
results = run_parallel([
    ("B1", "УРОВЕНЬ-B1_структура.txt", "b1_structure.txt"),
    ("B2", "УРОВЕНЬ-B2_идеи.txt", "b2_ideas.txt"),
    ("B3", "УРОВЕНЬ-B3_цитаты.txt", "b3_quotes.txt"),
])
r1 = results.get("b1_structure.txt", load("b1_structure.txt"))
r2 = results.get("b2_ideas.txt", load("b2_ideas.txt"))
r3 = results.get("b3_quotes.txt", load("b3_quotes.txt"))

# --- Шаг 2: RAG-вопросы (D) ---
r_d = ""
if RAG_SOURCE_FILE:
    print("\n--- Шаг 2: RAG-запросы (D) ---")
    rag_ctx = load("rag_context.txt")
    if not rag_ctx:
        import chromadb
        from sentence_transformers import SentenceTransformer
        client = chromadb.PersistentClient(
            path=r"D:\AI_Project\projects\knowledge-base\chroma_db")
        col = client.get_collection(name="books")
        model = SentenceTransformer("intfloat/multilingual-e5-small", device="cpu")
        parts = []
        MAX_FRAG = 1200
        for qi, q in enumerate(RAG_QUESTIONS, 1):
            emb = model.encode([f"query: {q}"])[0]
            res = col.query(
                query_embeddings=[emb.tolist()], n_results=2,
                include=["documents", "metadatas", "distances"],
                where={"source_file": RAG_SOURCE_FILE})
            parts.append(f"### Вопрос {qi}: {q}")
            for j in range(len(res["ids"][0])):
                dist = res["distances"][0][j]
                frag = res["documents"][0][j].strip()
                if len(frag) > MAX_FRAG:
                    frag = frag[:MAX_FRAG] + " [...]"
                parts.append(f"[фрагмент {qi}.{j+1}, релевантность {round(1-dist,3)}]\n{frag}")
            parts.append("")
        rag_ctx = "\n".join(parts)
        save("rag_context.txt", rag_ctx)

    qlist = "\n".join(f"{i}. {q}" for i, q in enumerate(RAG_QUESTIONS, 1))
    p_d = load_prompt("УРОВЕНЬ-D_rag_вопросы.txt")
    p_d = p_d.replace("{ВОПРОСЫ}", qlist).replace("{ФРАГМЕНТЫ}", rag_ctx)
    r_d = run("D_rag_ответы", p_d, "d_rag_answers.txt", ctx=CTX, prompt_file="УРОВЕНЬ-D_rag_вопросы.txt")
else:
    print("\n--- Шаг 2: RAG отключён (нет --rag-source), пропускаю ---")

# --- Шаг 3: RAG-проверка идей (точность) ---
ideas_check = ""
if RAG_SOURCE_FILE and r2:
    print("\n--- Шаг 3: RAG-проверка идей ---")
    ideas_check = load("ideas_check.txt")
    if not ideas_check:
        import chromadb
        from sentence_transformers import SentenceTransformer
        client = chromadb.PersistentClient(
            path=r"D:\AI_Project\projects\knowledge-base\chroma_db")
        col = client.get_collection(name="books")
        model = SentenceTransformer("intfloat/multilingual-e5-small", device="cpu")
        # Достаём идеи из B2
        idea_blocks = re.split(r"\n\s*\d+\.\s+", r2)
        parts = ["## RAG-проверка идей (подтверждение по тексту)\n"]
        for idx, block in enumerate(idea_blocks[1:], 1):
            title = block.strip().split("\n")[0][:100]
            emb = model.encode([f"query: {title}"])[0]
            res = col.query(
                query_embeddings=[emb.tolist()], n_results=1,
                include=["documents", "metadatas", "distances"],
                where={"source_file": RAG_SOURCE_FILE})
            if res["ids"][0]:
                dist = res["distances"][0][j := 0]
                score = round(1 - dist, 3)
                frag = res["documents"][0][0][:300].replace("\n", " ")
                status = "ПОДТВЕРЖДЕНО" if score >= 0.55 else "СЛАБО"
                parts.append(f"- Идея {idx} «{title}»: {status} (релевантность {score})\n  Фрагмент: {frag}...\n")
        ideas_check = "\n".join(parts)
        save("ideas_check.txt", ideas_check)
        print(f"  [saved] ideas_check.txt ({len(ideas_check)//1024} KB)")
else:
    print("\n--- Шаг 3: RAG-проверка идей пропущена ---")

# --- Шаг 4: Сборка B4 ---
print("\n--- Шаг 4: Сборка (B4) ---")
p4 = load_prompt("УРОВЕНЬ-B4_агрегация.txt")
p4 = (p4.replace("{Автор}", BOOK_TITLE_AUTHOR)
        .replace("{Название}", BOOK_TITLE_NAME)
        .replace("{ПРОХОД1}", r1)
        .replace("{ПРОХОД2}", r2)
        .replace("{ПРОХОД3}", r3))
if r_d:
    p4 += "\n\n=== ДОПОЛНИТЕЛЬНЫЙ ПРОХОД D: RAG-ответы ===\n"
    p4 += "Используй как ДОПОЛНИТЕЛЬНЫЙ источник конкретики (цифры, факты), помечая [вопрос N]. Не дублируй уже имеющееся.\n\n"
    p4 += r_d
if ideas_check:
    p4 += "\n\n=== ПРОВЕРКА ИДЕЙ (RAG): используй для уточнения формулировок, пометь слабые идеи ===\n"
    p4 += ideas_check
ans4 = run("B4_агрегация", p4, "b4_final.txt", ctx=CTX, prompt_file="УРОВЕНЬ-B4_агрегация.txt")

# --- Шаг 5: Автопроверка цитат (скрипт) ---
print("\n--- Шаг 5: Автопроверка цитат ---")
try:
    cp = subprocess.run(
        [sys.executable, str(SKRIPTS / "check_quotes.py"),
         str(TMP / "b4_final.txt"), str(BOOK_SRC)],
        timeout=600, capture_output=True, text=True, encoding="utf-8")
    report_out = cp.stdout or "автопроверка не дала вывода"
    save("quote_report.txt", report_out)
except Exception as e:
    report_out = f"ошибка автопроверки: {e}"
    save("quote_report.txt", report_out)
print(report_out)

# --- Шаг 6: Верификация (C) — Claude Opus 5, fallback qwen3.5 ---
print("\n--- Шаг 6: Верификация (C) ---")
pc = load_prompt("УРОВЕНЬ-C_верификация.txt")
pc = pc.replace("{РАЗБОР}", ans4).replace("{ТЕКСТ}", digest)

verdict = ""
judge_used = "qwen3.5:latest"
if "--no-claude" not in sys.argv:
    verdict = ask_claude(pc)
    if verdict:
        judge_used = "Claude Opus 5"
        print(f"  [claude] -> {len(verdict.split())} words")
    else:
        print("  [claude] недоступен, fallback на qwen3.5")

if not verdict:
    verdict = ask_ollama(pc, ctx=CTX_C, temp=0)
    print(f"  [qwen] -> {len(verdict.split())} words")
save("c_verdict.txt", verdict)

# --- Итог ---
print("\n=== ИТОГ ===")
total = (time.time() - t_start) / 60
OUT_DIR = Path(r"D:\AI_Project\Книги\_Разборы\новые_разборы")
dst = OUT_DIR / (BOOK_SRC.stem + "_МАКСИМАЛЬНЫЙ.md")
dst.write_text(ans4, encoding="utf-8")
dstv = OUT_DIR / (BOOK_SRC.stem + "_ВЕРИФИКАЦИЯ.md")
dstv.write_text(verdict, encoding="utf-8")

# --- Маркировка судьи в самих файлах (доверие к проверке) ---
judge_note = (f"\n\n---\n*Разбор собран пайплайном book-analysis. "
              f"Верификация: {judge_used} | дайджест {round(len(digest)/1024, 1)} КБ | "
              f"{time.strftime('%Y-%m-%d %H:%M')}. "
              f"Если судья не Claude — проверка слабее, нужен выборочный аудит.*\n")
dst.write_text(ans4 + judge_note, encoding="utf-8")

# --- Метрики: одна строка CSV на книгу ---
def parse_quote_stats(report_text):
    import collections
    c = collections.Counter()
    # OK_PDF (вариант [OK^]) — найден по сжатию пробелов, считается успехом
    # OK/OK^ (OK_PDF)/OK* (OK_SKIP)/ОК~ (fuzzy) считаются успехом; НЕТ — провал
    for m in re.finditer(r"\[(OK[~\^*]*|ОК~|НЕТ)\]", report_text):
        c[m.group(1)] += 1
    total = sum(c.values())
    passed = c["OK"] + c["OK^"] + c["OK*"] + c["ОК~"]
    return total, passed, c

def parse_number_stats(report_text):
    m = re.search(r"Чисел всего: (\d+), найдено: (\d+)", report_text)
    return (int(m.group(1)), int(m.group(2))) if m else (0, 0)

qt, qp, qc = parse_quote_stats(report_out)
nt, nf = parse_number_stats(report_out)
metrics_row = {
    "date": time.strftime("%Y-%m-%d %H:%M"),
    "book": BOOK_SRC.stem,
    "author": BOOK_TITLE_AUTHOR,
    "digest_kb": round(len(digest) / 1024, 1),
    "quotes_total": qt, "quotes_passed": qp,
    "quotes_rate": round(qp / qt, 3) if qt else 0,
    "numbers_total": nt, "numbers_found": nf,
    "judge": judge_used,
    "ideas_count": len(re.findall(r"\n\s*\d+\.\s+[А-ЯA-Z]", ans4)),
    "final_words": len(ans4.split()),
    "time_min": round(total, 1),
}
CSV = Path(r"D:\AI_Project\Книги\_Разборы\новые_разборы\metrics.csv")
new = not CSV.exists()
with open(CSV, "a", encoding="utf-8-sig", newline="") as f:
    import csv as _csv
    w = _csv.DictWriter(f, fieldnames=list(metrics_row.keys()))
    if new:
        w.writeheader()
    w.writerow(metrics_row)
print(f"Метрики: {metrics_row['quotes_rate']:.0%} цитат прошло, записано в metrics.csv")

print(f"Финальный разбор: {dst} ({len(ans4.split())} слов)")
print(f"Верификация:      {dstv} ({len(verdict.split())} слов)")
print(f"Общее время:      {total:.1f} мин")
print("Готово.")
