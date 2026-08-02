import os
import re
import hashlib
from pathlib import Path

CHROMA_DIR = Path(__file__).parent / "chroma_db"
BOOKS_TXT = Path(__file__).parent / "books_txt"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def extract_metadata(filename: str) -> dict:
    name = Path(filename).stem
    meta = {"filename": filename, "source_file": filename}
    match = re.match(r"(\d+)[_\-]\s*(.+)", name)
    if match:
        meta["index"] = match.group(1)
        meta["title"] = match.group(2).replace("_", " ").strip()
    else:
        meta["title"] = name.replace("_", " ").strip()
    return meta


def split_text(text: str, chunk_size: int, overlap: int) -> list[dict]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk_words = words[i : i + chunk_size]
        chunk_text = " ".join(chunk_words)
        chunk_id = hashlib.md5(chunk_text.encode()).hexdigest()[:12]
        chunks.append({"text": chunk_text, "id": chunk_id, "start_word": i})
        i += chunk_size - overlap
        if len(chunks) > 1 and chunks[-1]["text"] == chunks[-2]["text"]:
            chunks.pop()
            break
    return chunks


def index_books():
    print("=" * 60)
    print("RAG Indexer: индексация книг")
    print("=" * 60)

    txt_files = sorted(BOOKS_TXT.glob("*.txt"))
    if not txt_files:
        print(f"\n[!] Нет .txt файлов в {BOOKS_TXT}")
        print("Положи туда книги в формате .txt и запусти снова.\n")
        return

    print(f"\nНайдено книг: {len(txt_files)}\n")

    all_chunks = []
    for filepath in txt_files:
        meta = extract_metadata(filepath.name)
        print(f"  [{meta.get('index', '?')}] {meta['title']}")

        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

        text_clean = re.sub(r"\s+", " ", text).strip()
        if not text_clean:
            print(f"       ⚠ пустой файл, пропущен")
            continue

        chunks = split_text(text_clean, CHUNK_SIZE, CHUNK_OVERLAP)
        for c in chunks:
            c.update(meta)
        all_chunks.extend(chunks)

        ch_count = len(chunks)
        print(f"       {ch_count} чанков, всего слов: {len(text_clean.split())}")

    print(f"\n{'=' * 60}")
    print(f"Всего чанков: {len(all_chunks)}")
    print(f"Сохранение в ChromaDB...")

    try:
        import chromadb
        from sentence_transformers import SentenceTransformer

        print("  Загрузка модели эмбеддингов (multilingual)...")
        model = SentenceTransformer(
            "intfloat/multilingual-e5-small",
            device="cpu",
        )
        print("  Модель загружена.")

        client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        collection_name = "books"

        try:
            collection = client.get_collection(name=collection_name)
            print(f"  Коллекция '{collection_name}' существует, удаляем...")
            client.delete_collection(name=collection_name)
        except Exception:
            pass

        collection = client.create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )

        batch_size = 64
        for i in range(0, len(all_chunks), batch_size):
            batch = all_chunks[i : i + batch_size]
            texts = [
                f"passage: {c['text']}" for c in batch
            ]

            embeddings = model.encode(texts, show_progress_bar=False)

            ids = [f"book_{c['source_file']}_{c['id']}" for c in batch]
            documents = [c["text"] for c in batch]
            metadatas = [
                {
                    "title": c.get("title", ""),
                    "source_file": c.get("source_file", ""),
                    "start_word": c.get("start_word", 0),
                    "index": c.get("index", ""),
                }
                for c in batch
            ]

            collection.add(
                ids=ids,
                embeddings=embeddings.tolist(),
                documents=documents,
                metadatas=metadatas,
            )

        count = collection.count()
        print(f"\n[OK] Проиндексировано {count} чанков в коллекции '{collection_name}'")
        print(f"   ChromaDB: {CHROMA_DIR}")

    except ImportError as e:
        print(f"\n[WARN] Ошибка импорта: {e}")
        print("Установи зависимости:")
        print("  pip install -r requirements.txt")
        print("\nЧанки сохранены в памяти, но не записаны в БД.")
        print("Для просмотра структуры чанков:")

    except Exception as e:
        print(f"\n[ERR] Ошибка: {e}")
        print("\nЧанки были подготовлены, но запись в БД не удалась.")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    index_books()
