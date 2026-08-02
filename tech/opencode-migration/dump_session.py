# -*- coding: utf-8 -*-
"""Выгружает одну сессию OpenCode в читаемый текст (для просмотра/проверки
перед импортом) и опционально в JSONL формата Claude Code."""
import json
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = r"C:\Users\x2\.local\share\opencode\opencode.db"


def get_session_messages(session_id):
    uri = f"file:{DB_PATH}?mode=ro"
    con = sqlite3.connect(uri, uri=True)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    session = cur.execute("SELECT * FROM session WHERE id = ?", (session_id,)).fetchone()
    if not session:
        print(f"Сессия {session_id} не найдена")
        return None, []

    messages = cur.execute(
        "SELECT id, data, time_created FROM message WHERE session_id = ? ORDER BY time_created ASC",
        (session_id,),
    ).fetchall()

    result = []
    for m in messages:
        try:
            mdata = json.loads(m["data"])
        except (json.JSONDecodeError, TypeError):
            mdata = {}
        role = mdata.get("role", "?")

        parts = cur.execute(
            "SELECT data FROM part WHERE message_id = ? ORDER BY id ASC",
            (m["id"],),
        ).fetchall()

        texts = []
        for p in parts:
            try:
                pdata = json.loads(p["data"])
            except (json.JSONDecodeError, TypeError):
                continue
            if pdata.get("type") == "text":
                texts.append(pdata.get("text", ""))

        result.append(
            {
                "role": role,
                "text": "\n".join(texts),
                "time_created": m["time_created"],
            }
        )

    con.close()
    return session, result


def main():
    session_id = sys.argv[1]
    session, messages = get_session_messages(session_id)
    if session is None:
        return

    print(f"=== {session['title']} ===")
    print(f"directory: {session['directory']}")
    print(f"сообщений: {len(messages)}")
    print()

    out_lines = []
    for m in messages:
        if not m["text"].strip():
            continue
        ts = datetime.fromtimestamp(m["time_created"] / 1000).strftime("%Y-%m-%d %H:%M")
        out_lines.append(f"--- [{m['role']}] {ts} ---")
        out_lines.append(m["text"])
        out_lines.append("")

    text_out = "\n".join(out_lines)

    out_path = Path(r"D:\AI_Project\tech\opencode-migration") / f"preview_{session_id}.md"
    out_path.write_text(f"# {session['title']}\n\n" + text_out, encoding="utf-8")
    print(f"[Сохранено в {out_path}]")


if __name__ == "__main__":
    main()
