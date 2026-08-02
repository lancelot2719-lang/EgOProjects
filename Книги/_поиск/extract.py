#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Извлечение текста из книг библиотеки: PDF (текстовый слой -> OCR фолбэк),
FB2/EPUB (XML/zip), TXT (прямое чтение), DOC/DOCX (best-effort).
Сохраняет .txt рядом в extracted/<тема>/<имя>.txt и пишет лог проблем.
"""
import sys, os, re, json, zipfile, traceback, signal, logging, multiprocessing
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import pdfplumber
import pypdf
from bs4 import BeautifulSoup

# Some PDFs have malformed font descriptors that make pdfminer/pdfplumber
# spend near-infinite time re-parsing glyph widths (observed: single file
# stalling the whole batch for minutes). Silence the noisy warnings and
# enforce a hard per-file timeout so one bad PDF can never hang the run.
logging.getLogger("pdfminer").setLevel(logging.ERROR)

class TimeoutError(Exception):
    pass

def _timeout_handler(signum, frame):
    raise TimeoutError("extraction timed out")

PDF_TIMEOUT_SEC = 25
PDFTOTEXT_TIMEOUT_SEC = 90  # pdftotext is fast but big scans legitimately take ~40s

def with_timeout(fn, *args, timeout=PDF_TIMEOUT_SEC, **kwargs):
    old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(timeout)
    try:
        return fn(*args, **kwargs)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)

def _mp_worker(fn, args, kwargs, conn):
    try:
        conn.send(("ok", fn(*args, **kwargs)))
    except Exception as e:
        conn.send(("err", str(e)))
    finally:
        conn.close()

def with_hard_timeout(fn, *args, timeout=PDF_TIMEOUT_SEC, **kwargs):
    """OS-level timeout via subprocess. Kills the worker outright if it's
    stuck inside a blocking C call (e.g. pdfminer regex catastrophic
    backtracking on malformed PDFs) that SIGALRM can't interrupt.
    Uses a Pipe (not Queue) — Queue spawns a background feeder thread that
    can still be alive/lock-holding at the next fork(), which deadlocks
    the child. Pipe has no such thread, so it's safe to call repeatedly."""
    ctx = multiprocessing.get_context("spawn")
    parent_conn, child_conn = ctx.Pipe(duplex=False)
    p = ctx.Process(target=_mp_worker, args=(fn, args, kwargs, child_conn))
    p.start()
    child_conn.close()  # parent doesn't need its own copy of the write end

    # IMPORTANT: poll/recv the pipe BEFORE join(). A Pipe's OS buffer is
    # small (~64KB); a child sending back a large result (e.g. a full book's
    # text, hundreds of KB) blocks inside send() until the buffer is drained.
    # If we join() first, the parent never reads, the child never finishes
    # sending, and join() just burns the whole timeout waiting for an exit
    # that can't happen -> deadlock disguised as a timeout.
    got_data = parent_conn.poll(timeout)
    if not got_data:
        p.terminate()
        p.join(5)
        if p.is_alive():
            p.kill()
            p.join()
        parent_conn.close()
        raise TimeoutError(f"hard timeout after {timeout}s (process killed)")

    status, payload = parent_conn.recv()
    parent_conn.close()
    p.join(10)  # now safe: data already drained, child can exit
    if p.is_alive():
        p.terminate()
        p.join(5)
        if p.is_alive():
            p.kill()
            p.join()
    if status == "ok":
        return payload
    raise RuntimeError(payload)

SRC_ROOT = Path("/mnt/user-data/uploads/Книги")
OUT_ROOT = Path("/tmp/rag_pipeline/extracted")
LOG_PATH = Path("/tmp/rag_pipeline/logs/extract_log.jsonl")

MIN_CHARS_OK = 200  # если текстового слоя меньше — считаем что нужен OCR

def log(entry):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

def _extract_via_pdftotext(path):
    """poppler's pdftotext -- a C binary, by far the fastest and most
    robust engine here. Handles malformed PDFs that make pypdf/pdfplumber
    hang indefinitely (e.g. the 27MB Kurpatov scan). Made primary after
    benchmarking: files that timed out at 25s+ in pypdf finish in 1-4s here."""
    import subprocess, tempfile
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tf:
        out_path = tf.name
    try:
        subprocess.run(
            ["pdftotext", "-layout", str(path), out_path],
            check=True, capture_output=True, timeout=PDFTOTEXT_TIMEOUT_SEC,
        )
        return Path(out_path).read_text(encoding="utf-8", errors="replace")
    finally:
        try:
            os.unlink(out_path)
        except OSError:
            pass

def _extract_via_pypdf(path):
    reader = pypdf.PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def _extract_via_pdfplumber(path):
    text_parts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text_parts.append(page.extract_text() or "")
    return "\n".join(text_parts)

def extract_pdf_text_layer(path):
    """Try engines in order of speed+robustness: pdftotext -> pypdf -> pdfplumber.
    Returns the best (longest) result found; only reports failure if all fail."""
    best_text = ""
    errors = []

    # 1) pdftotext (poppler C binary) -- fastest and handles malformed PDFs
    #    that hang the pure-Python parsers. Runs in-process (it already
    #    subprocesses internally with its own timeout).
    try:
        text = _extract_via_pdftotext(path)
        if len((text or "").strip()) >= MIN_CHARS_OK:
            return text, None
        if len((text or "").strip()) > len(best_text.strip()):
            best_text = text or ""
    except Exception as e:
        errors.append(f"pdftotext: {e}")

    # 2) pypdf fallback, isolated in a killable subprocess.
    try:
        text = with_hard_timeout(_extract_via_pypdf, path, timeout=PDF_TIMEOUT_SEC)
        if len((text or "").strip()) >= MIN_CHARS_OK:
            return text, None
        if len((text or "").strip()) > len(best_text.strip()):
            best_text = text or ""
    except Exception as e:
        errors.append(f"pypdf: {e}")

    # 3) pdfplumber last -- best layout fidelity but slowest and most fragile.
    try:
        text = with_hard_timeout(_extract_via_pdfplumber, path, timeout=PDF_TIMEOUT_SEC)
        if len((text or "").strip()) > len(best_text.strip()):
            best_text = text or ""
    except Exception as e:
        errors.append(f"pdfplumber: {e}")

    if best_text.strip():
        return best_text, None
    return "", "all_pdf_engines_failed: " + " | ".join(errors)

def ocr_pdf(path, max_pages=None):
    """OCR фолбэк через pdf2image + pytesseract (rus+eng)."""
    from pdf2image import convert_from_path
    import pytesseract
    text_parts = []
    try:
        images = convert_from_path(str(path), dpi=200)
    except Exception as e:
        return "", f"pdf2image_failed: {e}"
    if max_pages:
        images = images[:max_pages]
    for i, img in enumerate(images):
        try:
            t = pytesseract.image_to_string(img, lang="rus+eng")
            text_parts.append(t)
        except Exception as e:
            text_parts.append("")
    return "\n".join(text_parts), None

def extract_fb2(path):
    try:
        raw = Path(path).read_bytes()
        soup = BeautifulSoup(raw, "xml")
        body = soup.find("body")
        if not body:
            return "", "fb2_no_body"
        return body.get_text("\n"), None
    except Exception as e:
        return "", f"fb2_failed: {e}"

def extract_epub(path):
    try:
        text_parts = []
        with zipfile.ZipFile(path) as z:
            names = [n for n in z.namelist() if n.lower().endswith((".xhtml", ".html", ".htm"))]
            for n in sorted(names):
                data = z.read(n)
                soup = BeautifulSoup(data, "lxml")
                text_parts.append(soup.get_text("\n"))
        return "\n".join(text_parts), None
    except Exception as e:
        return "", f"epub_failed: {e}"

def extract_txt(path):
    for enc in ("utf-8", "cp1251", "latin-1"):
        try:
            return Path(path).read_text(encoding=enc), None
        except Exception:
            continue
    return "", "txt_decode_failed"

def extract_zip_txt(path):
    """Handle .zip archives containing books. Many of these (esp. the
    Эзотерика ones) wrap a PDF rather than a .txt, so handle both:
    decode .txt members directly, and unpack PDF/FB2/EPUB members to a
    temp file and run the normal extractor over them."""
    import tempfile, shutil
    try:
        text_parts = []
        with zipfile.ZipFile(path) as z:
            for n in z.namelist():
                low = n.lower()
                if low.endswith(".txt"):
                    data = z.read(n)
                    for enc in ("utf-8", "cp1251", "latin-1"):
                        try:
                            text_parts.append(data.decode(enc))
                            break
                        except Exception:
                            continue
                elif low.endswith((".pdf", ".fb2", ".epub")):
                    suffix = "." + low.rsplit(".", 1)[1]
                    tmpdir = tempfile.mkdtemp(prefix="zipbook_")
                    try:
                        inner = Path(tmpdir) / ("inner" + suffix)
                        inner.write_bytes(z.read(n))
                        if suffix == ".pdf":
                            t, _ = extract_pdf_text_layer(inner)
                        elif suffix == ".fb2":
                            t, _ = extract_fb2(inner)
                        else:
                            t, _ = extract_epub(inner)
                        if t:
                            text_parts.append(t)
                    finally:
                        shutil.rmtree(tmpdir, ignore_errors=True)
        joined = "\n".join(text_parts)
        if not joined.strip():
            return "", "zip_no_extractable_members"
        return joined, None
    except Exception as e:
        return "", f"zip_failed: {e}"

def process_file(path: Path, topic: str, ocr_enabled=True):
    ext = path.suffix.lower()
    text, err = "", None
    used_ocr = False

    if ext == ".pdf":
        try:
            text, err = extract_pdf_text_layer(path)
        except Exception as e:
            text, err = "", f"pdf_extract_crashed: {e}"
        if len((text or "").strip()) < MIN_CHARS_OK and ocr_enabled:
            try:
                ocr_text, ocr_err = with_hard_timeout(ocr_pdf, path, timeout=180)
            except Exception as e:
                ocr_text, ocr_err = "", f"ocr_timeout_or_crash: {e}"
            if len((ocr_text or "").strip()) > len((text or "").strip()):
                text, err = ocr_text, ocr_err
                used_ocr = True
    elif ext == ".fb2":
        text, err = extract_fb2(path)
    elif ext == ".epub":
        text, err = extract_epub(path)
    elif ext == ".txt":
        text, err = extract_txt(path)
    elif ext == ".zip":
        text, err = extract_zip_txt(path)
    else:
        err = f"unsupported_ext:{ext}"

    out_dir = OUT_ROOT / topic
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / (path.stem + ".txt")
    chars = len((text or "").strip())
    if chars > 0:
        out_path.write_text(text, encoding="utf-8")
    log({
        "file": str(path), "topic": topic, "chars": chars,
        "used_ocr": used_ocr, "error": err,
        "status": "ok" if chars >= MIN_CHARS_OK else "empty_or_short"
    })
    return chars, used_ocr, err

def main():
    ocr_enabled = "--no-ocr" not in sys.argv
    positional = [a for a in sys.argv[1:] if not a.startswith("--")]
    topic_filter = positional[0] if positional else None
    workers = 4

    # Gather the full file list first so we can fan work out across
    # several books at once instead of one at a time. Each file's PDF
    # extraction already runs in its own isolated subprocess (with_hard_timeout),
    # so driving several of those from worker threads is safe and doesn't
    # add GIL contention -- the threads mostly just wait on subprocess I/O.
    todo = []
    for topic_dir in sorted(SRC_ROOT.iterdir()):
        if not topic_dir.is_dir():
            continue
        if topic_filter and topic_dir.name != topic_filter:
            continue
        for f in sorted(topic_dir.iterdir()):
            if f.is_dir():
                continue
            if f.suffix.lower() not in (".pdf", ".fb2", ".epub", ".txt", ".zip"):
                continue
            todo.append((f, topic_dir.name))

    results = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(process_file, f, topic, ocr_enabled): (f, topic)
            for f, topic in todo
        }
        for fut in as_completed(futures):
            f, topic = futures[fut]
            try:
                chars, used_ocr, err = fut.result()
            except Exception as e:
                chars, used_ocr, err = 0, False, f"worker_crashed: {e}"
            results.append((f.name, chars, used_ocr, err))
            flag = "OCR" if used_ocr else ("ERR" if err else "OK")
            print(f"[{flag}] {chars:7d} chars  {topic}/{f.name}")
    ok = sum(1 for r in results if r[1] >= MIN_CHARS_OK)
    print(f"\nDone: {ok}/{len(results)} extracted successfully")

if __name__ == "__main__":
    main()
