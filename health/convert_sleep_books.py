import PyPDF2
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

INPUT_DIR = Path(__file__).parent / "books"
OUTPUT_DIR = Path("converted_sleep")
OUTPUT_DIR.mkdir(exist_ok=True)

for file in INPUT_DIR.glob("*"):
    if file.suffix.lower() == ".pdf":
        print(f"PDF: {file.name}")
        try:
            reader = PyPDF2.PdfReader(str(file))
            text = ""
            for page in reader.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
            out = OUTPUT_DIR / (file.stem + ".txt")
            out.write_text(text, encoding='utf-8')
            print(f"  OK: {out.name} ({len(text)} chars, {len(reader.pages)} pages)")
        except Exception as e:
            print(f"  FAIL: {e}")

    elif file.suffix.lower() == ".doc":
        print(f"DOC: {file.name} - skipping (needs LibreOffice)")

    elif file.suffix.lower() == ".fb2":
        print(f"FB2: {file.name}")
        try:
            if file.suffix.lower() == ".fb2":
                tree = ET.parse(file)
                root = tree.getroot()
                ns = {'fb': 'http://www.gribuser.ru/xml/fictionbook/2.0'}
                texts = []
                for body in root.findall('.//fb:body', ns):
                    for p in body.findall('.//fb:p', ns):
                        if p.text:
                            texts.append(p.text)
                text = "\n\n".join(texts)
            else:
                continue
            out = OUTPUT_DIR / (file.stem + ".txt")
            out.write_text(text, encoding='utf-8')
            print(f"  OK: {out.name} ({len(text)} chars)")
        except Exception as e:
            print(f"  FAIL: {e}")

    else:
        print(f"SKIP: {file.name} ({file.suffix})")
