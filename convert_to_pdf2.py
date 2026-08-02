import os, re, zipfile, xml.etree.ElementTree as ET
from fpdf import FPDF

FONT_PATH = r"C:\Windows\Fonts\arial.ttf"
FONT_PATH_BOLD = r"C:\Windows\Fonts\arialbd.ttf"

class BookPDF(FPDF):
    def header(self):
        pass
    def footer(self):
        self.set_y(-15)
        self.set_font("ArialUni", size=8)
        self.cell(0, 10, str(self.page_no()), align="C")

def text_to_pdf(text, pdf_path, title="Book", max_chars=30000):
    pdf = BookPDF()
    pdf.add_font("ArialUni", "", FONT_PATH, uni=True)
    pdf.add_font("ArialUni", "B", FONT_PATH_BOLD, uni=True)
    pdf.set_auto_page_break(auto=True, margin=20)

    pdf.add_page()
    pdf.set_font("ArialUni", "B", 16)
    pdf.cell(0, 10, text=title[:200], new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_font("ArialUni", "", 10)

    paragraphs = text.split("\n")
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        # fpdf2 can handle Unicode directly
        para_clean = para[:max_chars] if len(para) > max_chars else para
        pdf.multi_cell(0, 5, text=para_clean)

    pdf.output(pdf_path)

def extract_fb2(path):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        ns = {"fb": "http://www.gribuser.ru/xml/fictionbook/2.0"}
        texts = []
        for body in root.findall(".//fb:body", ns):
            for p in body.findall(".//fb:p", ns):
                if p.text:
                    texts.append(p.text)
        return "\n".join(texts)
    except Exception as e:
        raise Exception(f"FB2 parse error: {e}")

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

def convert_file(fpath, pdf_path):
    ext = os.path.splitext(fpath)[1].lower()
    stem = os.path.splitext(os.path.basename(fpath))[0]

    if ext in (".doc", ".docx"):
        # Use win32com for DOC/DOCX (not handled here - handled separately)
        return False
    elif ext == ".fb2":
        text = extract_fb2(fpath)
    elif ext == ".epub":
        text = extract_epub(fpath)
    elif ext == ".txt":
        text = open(fpath, "r", encoding="utf-8", errors="replace").read()
    else:
        return False

    if len(text) < 50:
        raise Exception(f"Too short: {len(text)} chars")
    text_to_pdf(text, pdf_path, stem)
    return True

# === MAIN ===
FOLDERS = [
    r"D:\AI_Project\Книги\свободные_книги",
    r"D:\AI_Project\Книги\Развитие",
    r"D:\AI_Project\health\books",
]

SKIP_PREFIXES = ("анализ_", "анализ ", "общий ")
SKIP_NAMES = {"Список нужных книг.txt", "psixologiia-stressa.txt"}
TARGET_EXTS = {".fb2", ".epub", ".txt"}

total = 0
ok = 0
fail = 0

for folder in FOLDERS:
    if not os.path.exists(folder):
        continue
    for fname in sorted(os.listdir(folder)):
        fpath = os.path.join(folder, fname)
        if os.path.isdir(fpath):
            continue
        ext = os.path.splitext(fname)[1].lower()
        if ext not in TARGET_EXTS:
            continue
        if any(fname.startswith(p) for p in SKIP_PREFIXES):
            continue
        if fname in SKIP_NAMES:
            continue

        stem = os.path.splitext(fname)[0]
        pdf_path = os.path.join(folder, stem + ".pdf")
        if os.path.exists(pdf_path):
            continue

        total += 1
        print(f"[{total}] {fname[:55]:55s}...", end=" ")
        try:
            result = convert_file(fpath, pdf_path)
            if result:
                size = os.path.getsize(pdf_path)
                print(f"OK ({size/1024:.0f} KB)")
                ok += 1
            else:
                print("SKIP (DOC handled by separate script)")
        except Exception as e:
            print(f"FAIL: {str(e)[:80]}")
            fail += 1

print(f"\nDone: {ok} OK, {fail} FAIL out of {total}")
