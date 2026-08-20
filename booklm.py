import os, sys, glob, pickle, time
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path
from PyPDF2 import PdfReader as PyPdfReader
from pypdfium2 import PdfDocument
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

BOOKS_DIR = Path(r"D:\AI_Project\Книги")
VECTOR_DB_DIR = Path(r"D:\AI_Project\booklm_index")
EMBED_MODEL = "all-MiniLM-L6-v2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

def extract_text_from_pdf(path):
    # Try PyPDF2 first (fast for text PDFs)
    try:
        reader = PyPdfReader(str(path))
        texts = []
        for page in reader.pages:
            t = page.extract_text()
            if t and t.strip():
                texts.append(t)
        result = "\n".join(texts)
        if len(result) > 100:
            return result
    except Exception:
        pass
    # Fallback to pypdfium2 (better for complex PDFs)
    try:
        doc = PdfDocument(str(path))
        texts = []
        for page in doc:
            text = page.get_textpage().get_text_range()
            if text.strip():
                texts.append(text)
        return "\n".join(texts)
    except Exception as e:
        print(f"  Error: {e}")
        return ""

CACHE_FILE = VECTOR_DB_DIR.parent / "booklm_chunks.pkl"

def extract_all_chunks(force=False):
    if CACHE_FILE.exists() and not force:
        print(f"Loading chunks from {CACHE_FILE}...")
        with open(CACHE_FILE, "rb") as f:
            return pickle.load(f)

    all_files = list(BOOKS_DIR.rglob("*.pdf")) + list(BOOKS_DIR.rglob("*.txt"))
    print(f"Found {len(all_files)} files")

    all_chunks = []
    for i, pf in enumerate(all_files):
        rel = pf.relative_to(BOOKS_DIR)
        t0 = time.time()
        if pf.suffix.lower() == ".txt":
            text = extract_text_from_txt(pf)
        else:
            text = extract_text_from_pdf(pf)
        elapsed = time.time() - t0
        if not text:
            print(f"[{i+1}/{len(all_files)}] {rel} — SKIP (no text) [{elapsed:.1f}s]", flush=True)
            continue
        if len(text) < 50:
            print(f"[{i+1}/{len(all_files)}] {rel} — SKIP (too short: {len(text)} chars) [{elapsed:.1f}s]", flush=True)
            continue
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        chunks = splitter.create_documents([text], [{"source": str(rel)}])
        all_chunks.extend(chunks)
        print(f"[{i+1}/{len(all_files)}] {rel} — {len(chunks)} chunks [{elapsed:.1f}s]", flush=True)
        # Save incrementally every 10 PDFs
        if (i + 1) % 10 == 0:
            with open(CACHE_FILE, "wb") as f:
                pickle.dump(all_chunks, f)

    print(f"Total chunks: {len(all_chunks)}")
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_FILE, "wb") as f:
        pickle.dump(all_chunks, f)
    print(f"Chunks cached to {CACHE_FILE}")
    return all_chunks

def index_books(force=False):
    if VECTOR_DB_DIR.exists() and not force:
        print(f"Index exists at {VECTOR_DB_DIR}, loading...")
        emb = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
        return FAISS.load_local(str(VECTOR_DB_DIR), emb, allow_dangerous_deserialization=True)

    all_chunks = extract_all_chunks(force=force)
    if not all_chunks:
        print("No text extracted!")
        return None

    print("\nGenerating embeddings (batched)...", flush=True)
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(EMBED_MODEL, device="cpu")
    texts = [d.page_content for d in all_chunks]
    metadatas = [d.metadata for d in all_chunks]

    batch_size = 64
    all_embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        emb = model.encode(batch, show_progress_bar=False, normalize_embeddings=True)
        all_embeddings.extend(emb)
        if (i // batch_size) % 5 == 0:
            print(f"  embedded {min(i+batch_size, len(texts))}/{len(texts)}", flush=True)

    VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)
    text_embedding_pairs = list(zip(texts, all_embeddings))
    db = FAISS.from_embeddings(
        text_embeddings=text_embedding_pairs,
        embedding=HuggingFaceEmbeddings(model_name=EMBED_MODEL),
        metadatas=metadatas,
    )
    db.save_local(str(VECTOR_DB_DIR))
    print(f"Index saved to {VECTOR_DB_DIR}")
    return db

def ask(query, db, k=5, model="mistral:latest"):
    retriever = db.as_retriever(search_kwargs={"k": k})

    llm = ChatOpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",
        model=model,
        temperature=0.1,
    )

    prompt = PromptTemplate.from_template(
        "Ты — эксперт по книгам по саморазвитию, психологии и бизнесу. "
        "Отвечай на русском языке, используя только информацию из контекста ниже. "
        "Если ответа в контексте нет — скажи, что не знаешь.\n\n"
        "Контекст:\n{context}\n\n"
        "Вопрос: {question}\n\n"
        "Ответ:"
    )

    def format_docs(docs):
        return "\n\n---\n\n".join(
            f"[{d.metadata.get('source', '?')}] {d.page_content}" for d in docs
        )

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain.invoke(query)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python booklm.py index [--force]  — build index")
        print("  python booklm.py query <question>  — ask a question")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "index":
        force = "--force" in sys.argv
        index_books(force=force)

    elif cmd == "query":
        question = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else input("Question: ")
        db = index_books()
        if db:
            answer = ask(question, db)
            print(f"\nAnswer: {answer}")

    else:
        print(f"Unknown command: {cmd}")

def extract_text_from_txt(path):
    try:
        with open(str(path), "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        try:
            with open(str(path), "r", encoding="cp1251") as f:
                return f.read()
        except:
            return ""


