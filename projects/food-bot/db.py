import sqlite3
from contextlib import contextmanager
from datetime import datetime, timedelta

from config import DB_PATH


@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with get_conn() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                chat_id INTEGER PRIMARY KEY,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS food_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                ts TEXT NOT NULL,
                raw_text TEXT NOT NULL,
                kcal REAL,
                protein_g REAL,
                carbs_g REAL,
                fat_g REAL,
                comment TEXT
            );

            CREATE TABLE IF NOT EXISTS weight_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                ts TEXT NOT NULL,
                weight_kg REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS water_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                ts TEXT NOT NULL
            );
            """
        )


def register_user(chat_id: int):
    with get_conn() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO users (chat_id, created_at) VALUES (?, ?)",
            (chat_id, datetime.now().isoformat()),
        )


def get_all_chat_ids():
    with get_conn() as conn:
        rows = conn.execute("SELECT chat_id FROM users").fetchall()
    return [r["chat_id"] for r in rows]


def log_food(chat_id, raw_text, kcal, protein_g, carbs_g, fat_g, comment):
    with get_conn() as conn:
        conn.execute(
            """INSERT INTO food_log (chat_id, ts, raw_text, kcal, protein_g, carbs_g, fat_g, comment)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (chat_id, datetime.now().isoformat(), raw_text, kcal, protein_g, carbs_g, fat_g, comment),
        )


def log_weight(chat_id, weight_kg):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO weight_log (chat_id, ts, weight_kg) VALUES (?, ?, ?)",
            (chat_id, datetime.now().isoformat(), weight_kg),
        )


def log_water(chat_id):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO water_log (chat_id, ts) VALUES (?, ?)",
            (chat_id, datetime.now().isoformat()),
        )


def _today_bounds():
    start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=1)
    return start.isoformat(), end.isoformat()


def get_today_totals(chat_id):
    start, end = _today_bounds()
    with get_conn() as conn:
        row = conn.execute(
            """SELECT COALESCE(SUM(kcal),0) AS kcal, COALESCE(SUM(protein_g),0) AS protein_g,
                      COALESCE(SUM(carbs_g),0) AS carbs_g, COALESCE(SUM(fat_g),0) AS fat_g,
                      COUNT(*) AS entries
               FROM food_log WHERE chat_id = ? AND ts >= ? AND ts < ?""",
            (chat_id, start, end),
        ).fetchone()
    return dict(row)


def get_water_count_today(chat_id):
    start, end = _today_bounds()
    with get_conn() as conn:
        row = conn.execute(
            "SELECT COUNT(*) AS c FROM water_log WHERE chat_id = ? AND ts >= ? AND ts < ?",
            (chat_id, start, end),
        ).fetchone()
    return row["c"]


def get_last_weight(chat_id):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT ts, weight_kg FROM weight_log WHERE chat_id = ? ORDER BY ts DESC LIMIT 1",
            (chat_id,),
        ).fetchone()
    return dict(row) if row else None


def get_week_summary(chat_id):
    start = (datetime.now() - timedelta(days=7)).isoformat()
    with get_conn() as conn:
        food_row = conn.execute(
            """SELECT COALESCE(AVG(daily_kcal),0) AS avg_kcal, COALESCE(AVG(daily_protein),0) AS avg_protein
               FROM (
                   SELECT DATE(ts) AS d, SUM(kcal) AS daily_kcal, SUM(protein_g) AS daily_protein
                   FROM food_log WHERE chat_id = ? AND ts >= ?
                   GROUP BY DATE(ts)
               )""",
            (chat_id, start),
        ).fetchone()
        weights = conn.execute(
            "SELECT ts, weight_kg FROM weight_log WHERE chat_id = ? AND ts >= ? ORDER BY ts",
            (chat_id, start),
        ).fetchall()
    return {
        "avg_kcal": food_row["avg_kcal"],
        "avg_protein": food_row["avg_protein"],
        "weights": [dict(w) for w in weights],
    }
