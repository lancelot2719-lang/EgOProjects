# ИНСТРУМЕНТЫ — AI-инфраструктура

```
tools/
├── INDEX.md              ← ты здесь
├── opencode.md           ← OpenCode: модели, конфиги
├── whisper-pipeline.md   ← транскрибация аудио/видео
├── rag-system.md         ← семантический поиск
├── book-analysis.md      ← книжный AI-анализ
└── infra.md              ← Ollama, модели, окружение
```

## Состав инструментов

| Инструмент | Назначение | Статус |
|-----------|-----------|--------|
| **OpenCode** | AI-агент CLI, основа второго мозга | Работает |
| **Ollama** | Локальные модели (Qwen 3.5, Mistral) | Работает |
| **Whisper** (xkeyC/gguf) | Транскрибация аудио/видео | Работает |
| **RAG** (rag_simple.py) | Поиск по своей KB (FAISS) | Эксперимент |
| **MarkItDown** | Конвертация файлов→Markdown | Работает |
| **Unlimited-OCR** | Распознавание длинных PDF | Без GPU не работает |
| **SyntX AI** | Российский агрегатор нейросетей | Изучается |

## Куда смотреть
- [[../../AGENTS.md]] — основная инструкция для агента
- [[../../opencode.json]] — конфигурация OpenCode
- [[../../tech/whisper_flow/]] — Whisper pipeline
- [[../../tech/transcription_options.md]] — сравнение решений транскрибации
- [[../../projects/knigi/]] — книжный AI-анализ
