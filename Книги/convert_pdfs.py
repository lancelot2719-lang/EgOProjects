import PyPDF2
from pathlib import Path

INPUT_DIR = "books"
OUTPUT_DIR = "converted"

Path(OUTPUT_DIR).mkdir(exist_ok=True)

for file in Path(INPUT_DIR).glob("*.pdf"):
    print(f"Конвертация {file.name}...")
    try:
        reader = PyPDF2.PdfReader(str(file))
        text = ""
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        
        out_file = Path(OUTPUT_DIR) / (file.stem + ".txt")
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"  OK: {file.stem}.txt ({len(reader.pages)} pages, {len(text)} chars)")
    except Exception as e:
        print(f"  ERROR: {e}")

doc_files = list(Path(INPUT_DIR).glob("*.doc"))
if doc_files:
    print(f"\nFound {len(doc_files)} DOC files. Need LibreOffice or antiword for .doc -> .txt conversion.")
    for f in doc_files:
        print(f"  - {f.name}")
