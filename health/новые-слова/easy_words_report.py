"""
Выгрузка лёгких слов из Anki.

Режимы:
  1) python easy_words_report.py              — читает базу Anki напрямую
  2) python easy_words_report.py <путь к .anki2> — читает указанный файл

Что считает «лёгким»:
  - ease_factor >= 250 И reps >= 3
  - ИЛИ interval > 30 дней И reps >= 2

Результат: D:\AI_Project\health\новые-слова\easy_words.json
"""

import json
import os
import sqlite3
import shutil
import sys
import tempfile
from pathlib import Path
from datetime import datetime

EASY_THRESHOLD_EASE = 250   # ease factor (%)
EASY_THRESHOLD_REPS = 3
EASY_THRESHOLD_INTERVAL = 30  # days
EASY_THRESHOLD_REPS2 = 2

BASE_DIR = Path(__file__).parent
DECK_NAME = "Умные слова — smogue.com"
OUT_PATH = BASE_DIR / "easy_words.json"


def _find_db() -> Path:
    appdata = os.environ.get("APPDATA", "")
    base = Path(appdata) / "Anki2"
    if not base.is_dir():
        raise FileNotFoundError(f"Anki directory not found: {base}")
    profiles = sorted(base.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
    for p in profiles:
        if p.is_dir() and (p / "collection.anki2").exists():
            return p / "collection.anki2"
    raise FileNotFoundError(f"No Anki collection DB found under {base}")


def extract_easy(db_path: Path) -> list[dict]:
    tmp = Path(tempfile.gettempdir()) / "anki_easy_copy.anki2"
    shutil.copy2(str(db_path), str(tmp))
    conn = sqlite3.connect(str(tmp))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # find the deck ID
    cur.execute("SELECT id FROM decks WHERE name LIKE ?", (f"%{DECK_NAME}%",))
    row = cur.fetchone()
    if not row:
        print(f"Deck '{DECK_NAME}' not found in DB.")
        conn.close()
        tmp.unlink(missing_ok=True)
        return []
    deck_id = row["id"]

    # notes with their cards
    cur.execute("""
        SELECT n.id AS nid, n.flds, n.tags,
               c.id AS cid, c.ease, c.ivl, c.reps, c.type, c.queue
        FROM notes n
        JOIN cards c ON c.nid = n.id
        WHERE c.did = ?
        ORDER BY n.id
    """, (deck_id,))
    rows = cur.fetchall()

    easy = []
    easy_ids = set()
    for r in rows:
        if r["nid"] in easy_ids:
            continue
        ease = r["ease"]
        ivl = r["ivl"]
        reps = r["reps"]
        is_easy = (ease >= EASY_THRESHOLD_EASE and reps >= EASY_THRESHOLD_REPS) or \
                  (ivl > EASY_THRESHOLD_INTERVAL and reps >= EASY_THRESHOLD_REPS2)
        if not is_easy:
            continue

        fields = r["flds"].split("\x1f")
        word = fields[0].strip() if len(fields) > 0 else ""
        definition = fields[1].strip() if len(fields) > 1 else ""
        pos = fields[5].strip() if len(fields) > 5 else ""

        easy.append({
            "word": word,
            "definition": definition,
            "partOfSpeech": pos,
            "ease": ease,
            "interval_days": ivl,
            "reviews": reps,
        })
        easy_ids.add(r["nid"])

    conn.close()
    tmp.unlink(missing_ok=True)
    return easy


def main():
    if len(sys.argv) > 1:
        db_path = Path(sys.argv[1])
    else:
        db_path = _find_db()
    if not db_path.is_file():
        print(f"DB file not found: {db_path}")
        sys.exit(1)
    print(f"Reading: {db_path}")
    words = extract_easy(db_path)
    if not words:
        print("No easy words found yet. Review some cards first.")
        OUT_PATH.write_text("[]", encoding="utf-8")
        return
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Easy words: {len(words)}")
    print(f"Saved: {OUT_PATH}")
    print("\n".join(f"  {w['word']} ({w['partOfSpeech']}) — {w['interval_days']}d, ease {w['ease']}%, reps {w['reviews']}" for w in words[:20]))
    if len(words) > 20:
        print(f"  ... and {len(words)-20} more")


if __name__ == "__main__":
    main()
