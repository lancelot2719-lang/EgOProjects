# Сессия 28.07.2026 — VPN + подготовка к Claude

## Что сделано
- Проанализирован Happ VPN (D:\Happ\), извлечена подписка «Айтек» (VLESS+REALITY+XHTTP через Xray-core)
- Создан конфиг Xray: `tech/aitek-xray-config.json`
- Создан скрипт запуска: `tech/start-aitek-vpn.ps1`
- Установлен TUN-сервис `AitekTun` (tun2proxy-bin, system-wide routing через SOCKS5 :10808)
- Создан `CLAUDE.md` в корне проекта
- Ярлыки на рабочем столе: Aitek VPN / Stop Aitek VPN

## Статус VPN
- Xray работает (PID активен, порт 10808 LISTENING)
- TUN-сервис установлен (Manual start), интерфейс aitek-tun
- Публичный IP через VPN: 45.130.127.182
- Claude (claude.ai, api.anthropic.com) доступны через VPN

## Использованные файлы
- `tech/start-aitek-vpn.ps1` — основной лаунчер
- `tech/install-aitek-tun-service.ps1` — установка TUN-сервиса (админ)
- `tech/aitek-xray-config.json` — конфиг Xray
- `tech/fix-tun-service.ps1` — откат TUN-сервиса при ошибках
- `tech/ensure-happ-vpn.ps1` — старый скрипт (без Xray, напрямую через Happ)

## Решённые проблемы
- Петля маршрутизации: `--bypass 158.160.169.14` (трафик Xray к серверу VPN идёт в обход TUN)
- Порядок запуска: Xray → порт 10808 → TUN
- TUN-сервис не стартует автоматически (Manual), только после Xray

## Для Claude Code
- `CLAUDE.md` в корне — системная инструкция
- Second-brain структура сохранена
- opencode.json оставлен для совместимости
