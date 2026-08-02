# Основная инструкция (импорт из OpenCode)
@AGENTS.md

---

# Контекст Claude Code

## Диагностика памяти
- `/memory` — показать загруженные файлы в сессии
- `.claude/` — директория памяти (автозагрузка)

## Куда писать новое
@.claude/memory.md

---

# Контекст проекта

## Структура
- `D:\AI_Project\` — корень проектов
- `D:\AI_Project\projects\second-brain\` — второй мозг

## Состояние VPN (июль 2026)
Настроен **Aitek VPN** через Xray-core:
- `D:\Happ\core\xray.exe` — прокси-движок
- `D:\AI_Project\tech\aitek-xray-config.json` — конфиг подписки (VLESS+REALITY+XHTTP)
- Скрипт: `D:\AI_Project\tech\start-aitek-vpn.ps1` — запуск Xray + TUN
- TUN-сервис: `AitekTun` (установлен, ручной запуск)
- Порты: SOCKS5 127.0.0.1:10808, HTTP 127.0.0.1:10809
- Публичный IP через VPN: 45.130.127.182
- Ярлыки на рабочем столе: Aitek VPN / Stop Aitek VPN
- Порядок запуска: Xray → порт 10808 → TUN-сервис (system-wide routing)
- Автофикс при загрузке: `tech/fix-boot-net.cmd` (в автозагрузке) — отключает TUN, если Xray не запущен
- Запуск Claude Code с VPN: `claude-vpn.cmd` в корне проекта

## Windows Recovery
- Бекап: `D:\SAVE\C_Backup\` (4.29 GB)
- Скрипт: `D:\SAVE\backup-windows-reinstall.ps1`
- Порядок: драйверы → Git/Node/Python/Ollama → программы → AppData → Saved Games → Desktop/Docs/Pics → WiFi → AI_Project
