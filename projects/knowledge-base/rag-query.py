import argparse
import sys
from pathlib import Path

CHROMA_DIR = Path(__file__).parent / "chroma_db"
TOP_K = 5


def query_books(question: str, top_k: int = TOP_K, verbose: bool = False):
    try:
        import chromadb
        from sentence_transformers import SentenceTransformer
    except ImportError as e:
        print(f"[rag-query] ❌ Ошибка импорта: {e}", file=sys.stderr)
        print("Установи зависимости: pip install -r requirements.txt", file=sys.stderr)
        return ""

    if not CHROMA_DIR.exists():
        print(
            f"[rag-query] ❌ База не найдена: {CHROMA_DIR}",
            file=sys.stderr,
        )
        print("Сначала запусти rag-indexer.py", file=sys.stderr)
        return ""

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    try:
        collection = client.get_collection(name="books")
    except Exception:
        print(
            "[rag-query] ❌ Коллекция 'books' не найдена",
            file=sys.stderr,
        )
        print("Сначала запусти rag-indexer.py", file=sys.stderr)
        return ""

    model = SentenceTransformer(
        "intfloat/multilingual-e5-small",
        device="cpu",
    )

    query_embedding = model.encode([f"query: {question}"])[0]

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k,
    )

    if not results["ids"] or not results["ids"][0]:
        print("[rag-query] ⚠ Ничего не найдено", file=sys.stderr)
        return ""

    context_parts = []
    sources = set()

    for i in range(len(results["ids"][0])):
        doc_id = results["ids"][0][i]
        text = results["documents"][0][i]
        meta = results["metadatas"][0][i]
        distance = results["distances"][0][i] if results.get("distances") else 0
        score = round(1.0 - distance, 4)

        title = meta.get("title", "Неизвестная книга")
        source = meta.get("source_file", "—")

        sources.add(f"{title} ({source})")

        context_parts.append(
            f"[Источник: «{title}», релевантность: {score:.2f}]\n{text}"
        )

    context = "\n\n---\n\n".join(context_parts)

    header = "## Контекст из книг (RAG)\n\n"
    footer = f"\n\n---\n**Источники:** {', '.join(sorted(sources))}"

    result = header + context + footer

    if verbose:
        print(result, file=sys.stderr)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="RAG Query: поиск релевантных отрывков из книг"
    )
    parser.add_argument(
        "question",
        nargs="*",
        help="Вопрос (или передай через stdin)"
    )
    parser.add_argument(
        "-k",
        "--top-k",
        type=int,
        default=TOP_K,
        help=f"Количество чанков (по умолчанию: {TOP_K})"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Показать контекст в stderr"
    )
    parser.add_argument(
        "-p",
        "--preview",
        action="store_true",
        help="Показать контекст в stdout (иначе тихо)"
    )

    args = parser.parse_args()

    if not args.question:
        question = sys.stdin.read().strip()
    else:
        question = " ".join(args.question)

    if not question:
        parser.print_help()
        sys.exit(1)

    context = query_books(question, top_k=args.top_k, verbose=args.verbose)

    if not context:
        print("[rag-query] Ничего не найдено по запросу.", file=sys.stderr)
        sys.exit(1)

    if args.preview:
        print(context)
    else:
        print(context)


if __name__ == "__main__":
    import os
    if 'PYTHONIOENCODING' not in os.environ:
        sys.stdin.reconfigure(encoding='utf-8', errors='replace')
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    main()
