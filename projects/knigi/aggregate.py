import requests
import json
from pathlib import Path

# ===== НАСТРОЙКИ =====
OUTPUT_DIR = "outputs"               # папка с анализами отдельных книг
SUMMARY_DIR = "summary"              # папка для итогового отчёта
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"                # или mistral, gemma, phi, etc.

# ===== СБОР АНАЛИЗОВ =====
all_texts = []
for file in Path(OUTPUT_DIR).glob("*.txt"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        all_texts.append(f"--- Анализ книги {file.stem} ---\n{content}")

combined = "\n\n".join(all_texts)

# ===== ФОРМИРУЕМ ЗАПРОС К МОДЕЛИ =====
prompt = f"""
Ты — опытный аналитик. Перед тобой анализы нескольких книг по одной тематике.
Выполни следующие задачи:

1. Выдели общие советы и идеи, которые встречаются в большинстве книг.
2. Отметь уникальные или противоречивые рекомендации (укажи, в какой книге они встретились).
3. Сравни эти рекомендации с общеизвестными научными данными (если есть расхождения – явно укажи).
4. Составь итоговый список наиболее ценных, практически применимых решений.
5. Предложи, как можно улучшить процесс анализа для следующих тематик.

Вот тексты анализов (каждый начинается с названия книги):
{combined}
"""

# ===== ОТПРАВКА ЗАПРОСА К ЛОКАЛЬНОЙ МОДЕЛИ =====
payload = {
    "model": MODEL_NAME,
    "prompt": prompt,
    "stream": False
}

try:
    response = requests.post(OLLAMA_URL, json=payload, timeout=300)
    if response.status_code == 200:
        result = response.json()
        summary = result['response']
    else:
        summary = f"Ошибка при обращении к Ollama: {response.status_code}\n{response.text}"
except Exception as e:
    summary = f"Ошибка подключения к Ollama: {e}\nУбедитесь, что сервер запущен (ollama serve)."

# ===== СОХРАНЕНИЕ РЕЗУЛЬТАТА =====
Path(SUMMARY_DIR).mkdir(exist_ok=True)
output_path = Path(SUMMARY_DIR) / "final_report.txt"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(summary)

print(f"✅ Сводный отчёт сохранён в {output_path}")