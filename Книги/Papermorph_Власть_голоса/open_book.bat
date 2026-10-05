@echo off
cd /d "%~dp0"
start "" http://localhost:8765/vlast-golosa/
uv run python -m http.server 8765 -d site
