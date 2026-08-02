import sys, os, re
import xml.etree.ElementTree as ET
from fpdf import FPDF

FONT_DIR = r"C:\Windows\Fonts"
NS = {'fb': 'http://www.gribuser.ru/xml/fictionbook/2.0'}

def extract_text(el):
    parts = []
    if el.text:
        parts.append(el.text)
    for child in el:
        tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        if tag in ('strong', 'emphasis'):
            parts.append(extract_text(child))
        elif tag in ('p', 'subtitle', 'title', 'text-author', 'poem', 'stanza', 'v'):
            text = extract_text(child).strip()
            if text:
                parts.append(text)
            parts.append('\n')
        elif tag == 'empty-line':
            parts.append('\n\n')
        else:
            parts.append(extract_text(child))
        if child.tail:
            parts.append(child.tail)
    return ''.join(parts)

def clean_text(text):
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def fb2_to_pdf(input_path, output_path=None):
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '.pdf'

    tree = ET.parse(input_path)
    root = tree.getroot()

    body = root.find('.//fb:body', NS)
    title_info = root.find('.//fb:title-info', NS)
    desc = root.find('.//fb:description', NS)

    title = ''
    if title_info is not None:
        t = title_info.find('fb:book-title', NS)
        if t is not None and t.text:
            title = t.text.strip()

    author = ''
    if title_info is not None:
        first = title_info.find('fb:author/fb:first-name', NS)
        last = title_info.find('fb:author/fb:last-name', NS)
        if first is not None or last is not None:
            author = f'{first.text.strip() if first is not None else ""} {last.text.strip() if last is not None else ""}'.strip()

    pdf = FPDF()
    pdf.add_font('Arial', '', os.path.join(FONT_DIR, 'arial.ttf'), uni=True)
    pdf.add_font('Arial', 'B', os.path.join(FONT_DIR, 'arialbd.ttf'), uni=True)
    pdf.set_auto_page_break(auto=True, margin=20)

    pdf.add_page()
    pdf.set_font('Arial', 'B', 18)
    pdf.multi_cell(0, 10, title if title else 'Untitled', align='C')
    pdf.ln(10)
    if author:
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 8, author, align='C')
        pdf.ln(10)

    sections = body.findall('fb:section', NS) if body is not None else []
    if not sections:
        sections = [body]

    for section in sections:
        stitle = section.find('fb:title', NS)
        if stitle is not None and title:
            pdf.add_page()
            t = extract_text(stitle).strip()
            if t:
                pdf.set_font('Arial', 'B', 14)
                pdf.multi_cell(0, 8, clean_text(t))
                pdf.ln(4)

        for elem in section:
            tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
            if tag in ('title',):
                continue
            text = extract_text(elem).strip()
            if text:
                pdf.set_font('Arial', '', 11)
                pdf.multi_cell(0, 5.5, clean_text(text))
                pdf.ln(2)

    pdf.output(output_path)
    return output_path

if __name__ == '__main__':
    target = r"D:\AI_Project\Книги\Финансы"
    for f in os.listdir(target):
        if f.lower().endswith('.fb2'):
            src = os.path.join(target, f)
            dst = os.path.join(target, os.path.splitext(f)[0] + '.pdf')
            print(f"Converting: {f}")
            try:
                fb2_to_pdf(src, dst)
                sz = os.path.getsize(dst)
                print(f"  -> {os.path.basename(dst)} ({sz / 1024:.0f} KB)")
            except Exception as e:
                print(f"  ERROR: {e}")
    print("Done")
