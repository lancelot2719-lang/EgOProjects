# Как использовать

## 1. Установка
```powershell
cd D:\AI_Project\projects\knowledge-base
pip install -r requirements.txt
```

## 2. Индексация книг
```powershell
# Скопируй .txt книги в books_txt (или создай симлинк)
# Если книги в projects\knigi\ — скопируй оттуда .txt файлы
Copy-Item "..\knigi\*\*.txt" "books_txt\" -Recurse

# Запусти индексацию
python rag-indexer.py
```

## 3. Поиск
```powershell
# Быстрый поиск
python rag-query.py "как управлять финансами?" -p

# Поиск + передача контекста напрямую (тихий режим)
python rag-query.py "как сформировать привычку?" > context.txt
```

## 4. Подключение к OpenCode
При вопросе — сначала запроси контекст через `rag-query.py`, потом задай вопрос с этим контекстом.

Или используй режим наставника (см. AGENTS.md).
