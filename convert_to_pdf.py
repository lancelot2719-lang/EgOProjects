import os, sys, zipfile, re, xml.etree.ElementTree as ET, win32com.client

WORD = None

def get_word():
    global WORD
    if WORD is None:
        WORD = win32com.client.Dispatch("Word.Application")
        WORD.Visible = False
    return WORD

def text_to_pdf(text, pdf_path, title="Book"):
    word = get_word()
    doc = word.Documents.Add()
    try:
        doc.Range().Text = text
        doc.SaveAs(pdf_path, FileFormat=17)
        return True
    finally:
        doc.Close()

def doc_to_pdf(doc_path, pdf_path):
    word = get_word()
    doc = word.Documents.Open(doc_path)
    try:
        doc.SaveAs(pdf_path, FileFormat=17)
        return True
    finally:
        doc.Close()

def extract_fb2(path):
    tree = ET.parse(path)
    root = tree.getroot()
    ns = {"fb": "http://www.gribuser.ru/xml/fictionbook/2.0"}
    texts = []
    for body in root.findall(".//fb:body", ns):
        for p in body.findall(".//fb:p", ns):
            if p.text:
                texts.append(p.text)
    return "\n\n".join(texts)

def extract_epub(path):
    text = ""
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if name.endswith((".htm", ".html", ".xhtml")):
                content = z.read(name).decode("utf-8", errors="replace")
                clean = re.sub(r"<[^>]+>", "", content)
                clean = re.sub(r"\s+", " ", clean)
                text += clean + "\n"
    return text

# === CONFIG ===
FOLDERS = [
    r"D:\AI_Project\Книги\свободные_книги",
    r"D:\AI_Project\Книги\Развитие",
    r"D:\AI_Project\health\books",
    r"D:\AI_Project\Книги\Финансы",
]

SKIP_PREFIXES = ("анализ_", "анализ ", "общий ")
SKIP_NAMES = {"Список нужных книг.txt", "psixologiia-stressa.txt"}

for folder in FOLDERS:
    if not os.path.exists(folder):
        continue
    for fname in sorted(os.listdir(folder)):
        fpath = os.path.join(folder, fname)
        if os.path.isdir(fpath):
            continue
        ext = os.path.splitext(fname)[1].lower()
        if ext not in {".fb2", ".epub", ".txt", ".doc", ".docx"}:
            continue
        if any(fname.startswith(p) for p in SKIP_PREFIXES):
            continue
        if fname in SKIP_NAMES:
            continue

        stem = os.path.splitext(fname)[0]
        pdf_path = os.path.join(folder, stem + ".pdf")
        if os.path.exists(pdf_path):
            continue

        print(f"Converting: {fname}...", end=" ")
        try:
            if ext in (".doc", ".docx"):
                doc_to_pdf(fpath, pdf_path)
            elif ext == ".fb2":
                text = extract_fb2(fpath)
                text_to_pdf(text, pdf_path, stem)
            elif ext == ".epub":
                text = extract_epub(fpath)
                text_to_pdf(text, pdf_path, stem)
            elif ext == ".txt":
                text = open(fpath, "r", encoding="utf-8", errors="replace").read()
                text_to_pdf(text, pdf_path, stem)
            size = os.path.getsize(pdf_path)
            print(f"OK ({size/1024:.0f} KB)")
        except Exception as e:
            print(f"FAIL: {e}")
