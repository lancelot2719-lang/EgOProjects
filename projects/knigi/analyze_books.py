import requests
from pathlib import Path

# ===== НАСТРОЙКИ =====
INPUT_DIR = "converted"              # папка с текстами книг (после конвертации)
OUTPUT_DIR = "outputs"               # папка для анализов каждой книги
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

PROMPT_TEMPLATE = """
Ты — опытный аналитик. Проанализируй текст книги и выдели:
1. Ключевые тезисы (не более 7).
2. Практические советы и рекомендации.
3. Глубинные идеи и размышления автора.
4. Для каждого пункта приведи цитату из текста (или укажи раздел/страницу).
5. Оцени значимость каждого тезиса по шкале 1–5.
6. Заверши кратким резюме.

Текст книги (начало):
{text}
"""

Path(OUTPUT_DIR).mkdir(exist_ok=True)

for file in Path(INPUT_DIR).glob("*.txt"):
    print(f"Обработка {file.name}...")
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Обрезаем, чтобы не перегружать модель (первые 8000 символов)
    text = text[:8000]
    prompt = PROMPT_TEMPLATE.format(text=text)

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=180)
        if response.status_code == 200:
            result = response.json()
            analysis = result['response']
        else:
            analysis = f"Ошибка: {response.status_code}"
    except Exception as e:
        analysis = f"Ошибка подключения: {e}"

    out_file = Path(OUTPUT_DIR) / (file.stem + "_analysis.txt")
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(analysis)
    print(f"✅ Сохранён анализ для {file.stem}")