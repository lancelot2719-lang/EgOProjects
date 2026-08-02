# -*- coding: utf-8 -*-
"""
Шаг 1 миграции OpenCode -> Cloude.
Читает opencode.db (read-only) и строит sessions-manifest.md со списком
всех сессий для ручной разметки целевой папки.
"""
import json
import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = r"C:\Users\x2\.local\share\opencode\opencode.db"
OUT_PATH = Path(r"D:\AI_Project\tech\opencode-migration\sessions-manifest.md")

# ключевые слова -> подсказка папки (не решение, просто намёк для человека)
HINTS = {
    "second-brain": "projects/second-brain",
    "vpn": "tech",
    "xray": "tech",
    "aitek": "tech",
    "rag": "projects/knowledge-base",
    "мафи": "projects/second-brain (mafia)",
    "здоров": "health",
    "сон": "health",
    "трениров": "health",
    "питани": "health",
}


def guess_hint(title, preview):
    text = f"{title or ''} {preview or ''}".lower()
    for kw, folder in HINTS.items():
        if kw in text:
            return folder
    return ""


def main():
    uri = f"file:{DB_PATH}?mode=ro"
    con = sqlite3.connect(uri, uri=True)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    sessions = cur.execute(
        "SELECT id, directory, title, time_created FROM session ORDER BY time_created ASC"
    ).fetchall()

    rows = []
    for s in sessions:
        sid = s["id"]
        directory = s["directory"] or ""
        title = s["title"] or ""
        ts = s["time_created"]
        date_str = datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M") if ts else ""

        # первое сообщение role=user
        msg = cur.execute(
            """
            SELECT id, data FROM message
            WHERE session_id = ? AND json_extract(data, '$.role') = 'user'
            ORDER BY time_created ASC LIMIT 1
            """,
            (sid,),
        ).fetchone()

        preview = ""
        if msg:
            part = cur.execute(
                """
                SELECT data FROM part
                WHERE message_id = ? AND json_extract(data, '$.type') = 'text'
                ORDER BY id ASC LIMIT 1
                """,
                (msg["id"],),
            ).fetchone()
            if part:
                try:
                    text = json.loads(part["data"]).get("text", "")
                except (json.JSONDecodeError, TypeError):
                    text = ""
                preview = " ".join(text.split())[:200]

        hint = guess_hint(title, preview)
        rows.append(
            {
                "id": sid,
                "date": date_str,
                "directory": directory,
                "title": title,
                "preview": preview,
                "hint": hint,
            }
        )

    con.close()

    lines = []
    lines.append("# Манифест сессий OpenCode -> Cloude")
    lines.append("")
    lines.append(f"Всего сессий: {len(rows)}")
    lines.append("")
    lines.append(
        "Заполни колонку **Целевая папка** абсолютным или относительным (от "
        "D:\\AI_Project) путём для каждой строки, затем передай файл шагу 2 "
        "(import_to_claude.py)."
    )
    lines.append("")
    lines.append("| # | ID сессии | Дата | Папка в OpenCode | Заголовок | Превью | Подсказка | Целевая папка |")
    lines.append("|---|-----------|------|-------------------|-----------|--------|-----------|---------------|")

    def esc(s):
        return (s or "").replace("|", "\\|").replace("\n", " ")

    for i, r in enumerate(rows, 1):
        lines.append(
            f"| {i} | {r['id']} | {r['date']} | {esc(r['directory'])} | "
            f"{esc(r['title'])} | {esc(r['preview'])} | {esc(r['hint'])} |  |"
        )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Готово: {OUT_PATH} ({len(rows)} сессий)")


if __name__ == "__main__":
    main()
