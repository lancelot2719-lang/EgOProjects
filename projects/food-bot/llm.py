import json
import re

import requests

from config import LMSTUDIO_MODEL, LMSTUDIO_URL

SYSTEM_PROMPT = (
    "Ты — нутрициолог-ассистент. Тебе присылают описание того, что человек съел "
    "(на русском, неформально, возможно с указанием примерного веса порций). "
    "Оцени пищевую ценность ВСЕГО приёма пищи целиком, исходя из обычных порций. "
    "Если блюд несколько — просуммируй в одну оценку. "
    "Отвечай СТРОГО одним JSON-объектом, без пояснений и без markdown-разметки, "
    "в формате:\n"
    '{"kcal": <число>, "protein_g": <число>, "carbs_g": <число>, "fat_g": <число>, '
    '"comment": "<короткий комментарий на русском, до 12 слов>"}'
)


def _extract_json(text: str):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
        text = re.sub(r"```$", "", text).strip()
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None


def estimate_macros(food_text: str, timeout: int = 30):
    """Возвращает dict с kcal/protein_g/carbs_g/fat_g/comment или None, если не удалось."""
    payload = {
        "model": LMSTUDIO_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": food_text},
        ],
        "temperature": 0.2,
    }
    try:
        resp = requests.post(f"{LMSTUDIO_URL}/chat/completions", json=payload, timeout=timeout)
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
    except Exception:
        return None

    data = _extract_json(content)
    if not data:
        return None

    try:
        return {
            "kcal": round(float(data.get("kcal", 0))),
            "protein_g": round(float(data.get("protein_g", 0)), 1),
            "carbs_g": round(float(data.get("carbs_g", 0)), 1),
            "fat_g": round(float(data.get("fat_g", 0)), 1),
            "comment": str(data.get("comment", "")).strip(),
        }
    except (TypeError, ValueError):
        return None
