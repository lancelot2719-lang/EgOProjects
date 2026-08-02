import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BOOKS_TXT = Path(__file__).parent / "books_txt"
BOOKS_RAW = Path(__file__).parent / "books_raw"


def convert_pdf(filepath: Path) -> str | None:
    import pdfplumber

    text_parts = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text_parts.append(t)
    return "\n\n".join(text_parts) if text_parts else None


def convert_docx(filepath: Path) -> str | None:
    import docx

    doc = docx.Document(filepath)
    return "\n".join(p.text for p in doc.paragraphs)


def convert_fb2(filepath: Path) -> str | None:
    from bs4 import BeautifulSoup

    with open(filepath, "rb") as f:
        soup = BeautifulSoup(f.read(), "lxml-xml")
    body = soup.find("body")
    if body is None:
        body = soup
    for tag in body.find_all(["title", "subtitle", "epigraph", "cite", "p"]):
        pass
    text = body.get_text("\n", strip=True)
    return text


def convert_epub(filepath: Path) -> str | None:
    import ebooklib
    from bs4 import BeautifulSoup
    from ebooklib import epub

    book = epub.read_epub(filepath)
    text_parts = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), "html.parser")
            text_parts.append(soup.get_text("\n", strip=True))
    return "\n\n".join(text_parts)


def convert_txt(filepath: Path) -> str | None:
    with open(filepath, "rb") as f:
        raw = f.read()
    for enc in ["utf-8", "cp1251", "latin-1"]:
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace")


CONVERTERS = {
    ".pdf": convert_pdf,
    ".docx": convert_docx,
    ".fb2": convert_fb2,
    ".epub": convert_epub,
    ".txt": convert_txt,
}


def clean_filename(filename: str) -> str:
    name = Path(filename).stem
    name = re.sub(r"[^\w\s\-]", "", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name[:80] + ".txt"


def convert_book(filepath: Path) -> bool:
    ext = filepath.suffix.lower()
    converter = CONVERTERS.get(ext)
    if converter is None:
        print(f"  [SKIP] {filepath.name} — формат {ext} не поддерживается")
        return False

    print(f"  [CONV] {filepath.name}... ", end="", flush=True)
    try:
        text = converter(filepath)
    except Exception as e:
        print(f"ОШИБКА: {e}")
        return False

    if not text or len(text.strip()) < 50:
        print("пусто/слишком коротко, пропущен")
        return False

    text_clean = re.sub(r"\n{4,}", "\n\n", text)
    text_clean = re.sub(r"[ \t]{3,}", " ", text_clean)

    out_name = clean_filename(filepath.name)
    out_path = BOOKS_TXT / out_name

    counter = 1
    while out_path.exists():
        stem = out_path.stem
        out_path = BOOKS_TXT / f"{stem}_{counter}.txt"
        counter += 1

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text_clean)

    words = len(text_clean.split())
    print(f"OK — {words} слов → {out_path.name}")
    return True


def main():
    BOOKS_RAW.mkdir(parents=True, exist_ok=True)
    BOOKS_TXT.mkdir(parents=True, exist_ok=True)

    files = sorted(BOOKS_RAW.rglob("*"))
    files = [f for f in files if f.is_file() and f.suffix.lower() in CONVERTERS]

    if not files:
        print(f"Нет файлов для конвертации в {BOOKS_RAW}")
        print("Поддерживаемые форматы: PDF, DOCX, FB2, EPUB, TXT")
        print("Старый .doc — открой в Word и сохрани как .docx или .txt")
        print("Положи файлы в папку books_raw и запусти снова.")
        return

    print(f"Найдено файлов: {len(files)}\n")
    ok = 0
    for f in files:
        if convert_book(f):
            ok += 1

    print(f"\n[OK] Конвертировано: {ok}/{len(files)}")
    print(f"     Результат: {BOOKS_TXT}")
    print(f"     Затем запусти: python rag-indexer.py")


if __name__ == "__main__":
    main()
