import requests
import json
from pathlib import Path

INPUT_DIR = "converted"
OUTPUT_DIR = "outputs"
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "mistral"

SYSTEM_MSG = """Ты -- опытный аналитик и книжный обозреватель. Твоя задача -- составить подробный разбор книги на русском языке строго по следующему формату:

# Анализ книги: [Название]

## Основные тезисы (не более 10)
Для каждого: формулировка + краткое объяснение + цитата или отсылка.

## Практические советы
Таблица: номер | совет | суть.

## Глубинние идеи автора
Ключевые философские или методологические идеи.

## Сильные и слабые стороны

## Краткое резюме (3-5 предложений)
Общий вывод и кому подойдёт книга.

ВАЖНО: Отвечай ТОЛЬКО на русском языке. Строго соблюдай формат выше."""

Path(OUTPUT_DIR).mkdir(exist_ok=True)

for file in Path(INPUT_DIR).glob("*.txt"):
    print(f"Processing {file.name}...")
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = text[:25000]
    
    messages = [
        {"role": "system", "content": SYSTEM_MSG},
        {"role": "user", "content": f"Проанализируй эту книгу:\n\n{text}"}
    ]

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
        "options": {
            "num_predict": 4096,
            "temperature": 0.3
        }
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=600)
        if response.status_code == 200:
            result = response.json()
            analysis = result['message']['content']
        else:
            analysis = f"Error: {response.status_code}\n{response.text}"
    except Exception as e:
        analysis = f"Connection error: {e}"

    out_file = Path(OUTPUT_DIR) / (file.stem + "_analysis.md")
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(analysis)
    print(f"  Saved: {out_file.name}")
