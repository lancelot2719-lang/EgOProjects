# Papermorph — «Власть голоса»

Анимированная веб-книга по книге Жана Абитболя «Власть голоса», собранная скиллом [Papermorph](https://github.com/DozenTwelve/Papermorph).
Готова пилотная глава 6 «Высота, громкость, тембр и мозг». Остальные 21 глава есть в оглавлении с пометкой «скоро».

## Что где лежит

```
site/vlast-golosa/          готовая книга (только её и открывать/публиковать)
  index.html                обложка и оглавление
  ch06/                     урок главы 6; audio/ru — озвучка
  lib/                      движок (русифицированная копия)
content/vlast-golosa/ch06/  текст озвучки narration.ru.json
books/vlast-golosa/         план книги: BOOK.md, chapters.md, раскадровки chapters/chNN.md, split.py
tools/vlast-golosa/         tts.py (озвучка), fake_tts.py, ru_engine.py, e2e_ch06.py
```

## 1. Один раз: поставить инструменты

В PowerShell:

```
winget install astral-sh.uv
winget install Gyan.FFmpeg
```

Перезапустите терминал после установки.

## 2. Озвучить главу

Сейчас в главе беззвучные клипы-заглушки с примерными таймингами. Настоящий голос (ru-RU-DmitryNeural):

- дважды щёлкнуть `make_audio_ch06.bat`, или
- в терминале в этой папке:
  `uv run --with edge-tts tools/vlast-golosa/tts.py content/vlast-golosa/ch06/narration.ru.json site/vlast-golosa/ch06/audio/ru`

Нужен интернет (сервис Microsoft Edge TTS). Скрипт сам заменит заглушки и пересчитает тайминги анимации под реальную речь.

## 3. Открыть книгу

Дважды щёлкнуть `open_book.bat` или выполнить `uv run python -m http.server 8765 -d site`
и открыть http://localhost:8765/vlast-golosa/. Через двойной клик по index.html звук не заработает: нужен локальный сервер.

Управление: пробел — пуск/пауза, ←/→ — шаги, C — субтитры, ? — все клавиши.
