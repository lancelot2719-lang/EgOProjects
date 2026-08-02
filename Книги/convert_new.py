import PyPDF2, zipfile, xml.etree.ElementTree as ET, json, re
from pathlib import Path

INPUT_DIR = Path(__file__).parent / "Развитие"
OUTPUT_DIR = Path(__file__).parent / "converted_new"
OUTPUT_DIR.mkdir(exist_ok=True)

for file in sorted(INPUT_DIR.glob("*")):
    if file.suffix.lower() == ".pdf":
        try:
            reader = PyPDF2.PdfReader(str(file))
            text = ""
            for page in reader.pages:
                t = page.extract_text()
                if t: text += t + "\n"
            out = OUTPUT_DIR / (file.stem + ".txt")
            out.write_text(text, encoding='utf-8')
            print(f"PDF OK: {file.name} -> {len(text)} chars, {len(reader.pages)}p")
        except Exception as e:
            print(f"PDF FAIL: {file.name} -> {e}")

    elif file.suffix.lower() == ".fb2":
        try:
            tree = ET.parse(file)
            root = tree.getroot()
            ns = {'fb': 'http://www.gribuser.ru/xml/fictionbook/2.0'}
            texts = []
            for body in root.findall('.//fb:body', ns):
                for p in body.findall('.//fb:p', ns):
                    if p.text: texts.append(p.text)
            text = "\n\n".join(texts)
            out = OUTPUT_DIR / (file.stem + ".txt")
            out.write_text(text, encoding='utf-8')
            print(f"FB2 OK: {file.name} -> {len(text)} chars")
        except Exception as e:
            print(f"FB2 FAIL: {file.name} -> {e}")

    elif file.suffix.lower() == ".epub":
        try:
            text = ""
            with zipfile.ZipFile(file) as z:
                for name in z.namelist():
                    if name.endswith(".htm") or name.endswith(".html") or name.endswith(".xhtml"):
                        content = z.read(name).decode('utf-8', errors='replace')
                        clean = re.sub(r'<[^>]+>', '', content)
                        clean = re.sub(r'\s+', ' ', clean)
                        text += clean + "\n"
            if text.strip():
                out = OUTPUT_DIR / (file.stem + ".txt")
                out.write_text(text, encoding='utf-8')
                print(f"EPUB OK: {file.name} -> {len(text)} chars")
            else:
                print(f"EPUB EMPTY: {file.name}")
        except Exception as e:
            print(f"EPUB FAIL: {file.name} -> {e}")

    elif file.suffix.lower() == ".doc":
        print(f"DOC SKIP: {file.name} (needs LibreOffice)")

    elif file.suffix.lower() == ".txt":
        print(f"TXT: {file.name}")
        
    else:
        print(f"SKIP: {file.name} ({file.suffix})")
