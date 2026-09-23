import os
from pathlib import Path
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


def _get_int(name: str, default: int) -> int:
    val = os.getenv(name)
    return int(val) if val else default


BOT_TOKEN = os.getenv("BOT_TOKEN", "")

LMSTUDIO_URL = os.getenv("LMSTUDIO_URL", "http://localhost:1234/v1")
LMSTUDIO_MODEL = os.getenv("LMSTUDIO_MODEL", "local-model")

TARGET_KCAL = _get_int("TARGET_KCAL", 2350)
TARGET_PROTEIN_G = _get_int("TARGET_PROTEIN_G", 160)

TIMEZONE = os.getenv("TIMEZONE", "Europe/Moscow")
ZONE = ZoneInfo(TIMEZONE)

WATER_GLASS_ML = _get_int("WATER_GLASS_ML", 250)
WATER_TARGET_ML = _get_int("WATER_TARGET_ML", 2200)
WATER_REMINDER_TIMES = [
    t.strip()
    for t in os.getenv("WATER_REMINDER_TIMES", "11:00,14:30,18:00").split(",")
    if t.strip()
]

# 0 = понедельник ... 6 = воскресенье
WEIGHIN_DAY = _get_int("WEIGHIN_DAY", 0)
WEIGHIN_TIME = os.getenv("WEIGHIN_TIME", "09:00")

DB_PATH = BASE_DIR / os.getenv("DB_PATH", "food_bot.db")
