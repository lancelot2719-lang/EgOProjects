@echo off
chcp 65001 >nul
cd /d "%~dp0"
uv run --with edge-tts tools\vlast-golosa\tts.py content\vlast-golosa\ch06\narration.ru.json site\vlast-golosa\ch06\audio\ru
pause
