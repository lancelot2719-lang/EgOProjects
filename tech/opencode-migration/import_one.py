# -*- coding: utf-8 -*-
"""
Пилотный импорт ОДНОЙ сессии OpenCode -> Claude Code, с реальным алгоритмом
кодирования имени папки (найден в claude.exe: replace(/[^a-zA-Z0-9]/g,'-'),
функции x0()/FK() в бандле).
"""
import json
import re
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = r"C:\Users\x2\.local\share\opencode\opencode.db"
# Пишем в оба места: старое (C:, пока текущая живая сессия Cloude не
# перезапущена и продолжает читать оттуда) и новое (D:, куда переехал
# CLAUDE_CONFIG_DIR и куда будут смотреть все сессии после перезапуска).
CLAUDE_HOMES = [
    Path(r"C:\Users\x2\.claude"),
    Path(r"D:\AI_Project\.claude-home"),
]
VERSION = "2.1.219"


def encode_project_dir(abs_path: str) -> str:
    # Точная копия функции x0(e) из claude.exe: replace(/[^a-zA-Z0-9]/g,'-')
    slug = re.sub(r"[^a-zA-Z0-9]", "-", abs_path)
    if len(slug) <= 200:
        return slug
    # truncate+hash не реализуем — для наших путей не требуется (<200 символов)
    raise ValueError("путь длиннее 200 символов — нужна отдельная логика хэша")


def get_session_and_text_messages(session_id):
    uri = f"file:{DB_PATH}?mode=ro"
    con = sqlite3.connect(uri, uri=True)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    session = cur.execute("SELECT * FROM session WHERE id = ?", (session_id,)).fetchone()
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
        role = mdata.get("role")
        model = None
        if isinstance(mdata.get("model"), dict):
            model = mdata["model"].get("modelID")

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
        text = "\n".join(texts).strip()
        if not text or role not in ("user", "assistant"):
            continue
        result.append(
            {"role": role, "text": text, "time_created": m["time_created"], "model": model}
        )

    con.close()
    return session, result


def to_iso(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def build_jsonl_lines(target_cwd, messages, new_session_id):
    lines = []
    parent = None
    for m in messages:
        line_uuid = str(uuid.uuid4())
        ts = to_iso(m["time_created"])
        if m["role"] == "user":
            obj = {
                "parentUuid": parent,
                "isSidechain": False,
                "promptId": str(uuid.uuid4()),
                "type": "user",
                "message": {"role": "user", "content": m["text"]},
                "uuid": line_uuid,
                "timestamp": ts,
                "permissionMode": "acceptEdits",
                "origin": {"kind": "human"},
                "promptSource": "opencode-import",
                "userType": "external",
                "entrypoint": "claude-desktop",
                "cwd": target_cwd,
                "sessionId": new_session_id,
                "version": VERSION,
                "gitBranch": "HEAD",
            }
        else:
            obj = {
                "parentUuid": parent,
                "isSidechain": False,
                "type": "assistant",
                "uuid": line_uuid,
                "timestamp": ts,
                "message": {
                    "id": str(uuid.uuid4()),
                    "role": "assistant",
                    "type": "message",
                    "model": m["model"] or "opencode-import",
                    "stop_reason": "end_turn",
                    "content": [{"type": "text", "text": m["text"]}],
                    "usage": {
                        "input_tokens": 0,
                        "output_tokens": 0,
                        "cache_creation_input_tokens": 0,
                        "cache_read_input_tokens": 0,
                    },
                },
                "userType": "external",
                "entrypoint": "claude-desktop",
                "cwd": target_cwd,
                "sessionId": new_session_id,
                "version": VERSION,
                "gitBranch": "HEAD",
            }
        lines.append(json.dumps(obj, ensure_ascii=False))
        parent = line_uuid
    return lines


def register_in_claude_json(claude_json_path, target_cwd):
    raw = claude_json_path.read_text(encoding="utf-8")
    data = json.loads(raw)
    projects = data.setdefault("projects", {})
    if target_cwd in projects:
        print(f"[{claude_json_path}] запись для {target_cwd} уже существует — не трогаю")
        return
    projects[target_cwd] = {
        "allowedTools": [],
        "mcpContextUris": [],
        "hasTrustDialogAccepted": False,
    }
    backup = claude_json_path.with_suffix(".json.bak-import-one")
    if not backup.exists():
        backup.write_text(raw, encoding="utf-8")
        print(f"[{claude_json_path}] бэкап сохранён: {backup}")
    claude_json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[{claude_json_path}] добавлена запись для {target_cwd}")


def main():
    session_id = sys.argv[1]
    target_cwd = sys.argv[2]  # напр. r"D:\AI_Project\тренировки"

    session, messages = get_session_and_text_messages(session_id)
    if not session:
        print("Сессия не найдена")
        return
    if not messages:
        print("Нет текстовых сообщений для переноса")
        return

    encoded = encode_project_dir(target_cwd)
    new_session_id = str(uuid.uuid4())
    lines = build_jsonl_lines(target_cwd, messages, new_session_id)
    content = "\n".join(lines) + "\n"

    for home in CLAUDE_HOMES:
        if not home.exists():
            print(f"[пропуск] {home} не существует")
            continue
        target_dir = home / "projects" / encoded
        target_dir.mkdir(parents=True, exist_ok=True)
        out_file = target_dir / f"{new_session_id}.jsonl"
        out_file.write_text(content, encoding="utf-8")
        print(f"[{home}] файл: {out_file}")
        register_in_claude_json(home / ".claude.json", target_cwd)

    print(f"cwd: {target_cwd}")
    print(f"encoded dir: {encoded}")
    print(f"сообщений перенесено: {len(messages)}")


if __name__ == "__main__":
    main()
