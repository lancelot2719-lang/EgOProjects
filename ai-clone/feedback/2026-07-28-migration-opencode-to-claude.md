# Миграция OpenCode → Claude Code

## Что сделано
- `CLAUDE.md` переписан: импортирует `AGENTS.md` через `@AGENTS.md`
- AGENTS.md остался без изменений — это единый источник правил
- Создан `.claude/memory.md` — карта доменов для Claude Code
- AGENTS.md теперь виден Claude Code через импорт, дублирования нет

## Структура после миграции
```
D:\AI_Project\
├── CLAUDE.md          ← точка входа, @AGENTS.md + контекст проекта
├── AGENTS.md          ← системая инструкция (без изменений)
├── .claude/
│   └── memory.md      ← карта памяти (автозагружается Claude Code)
└── projects/second-brain/  ← второй мозг
```

## Проверка
После запуска `claude` в D:\AI_Project выполнить `/memory` — должны быть видны:
- CLAUDE.md
- AGENTS.md (через импорт)
- .claude/memory.md

## Дополнительно
- Создан `claude-vpn.cmd` — запуск Claude Code с авто-поднятием VPN
- Создан `tech/fix-boot-net.cmd` + `.ps1` — чинит интернет при загрузке (в автозагрузке)
- `fix-boot-net` зарегистрирован в HKCU\Run

## Замечание
OpenCode больше не используется? Если да — `opencode.json` и `.opencode/` можно удалить, но пока оставлено на случай отката.
