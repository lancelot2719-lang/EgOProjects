# Переустановка Windows на новый SSD

> План создан 2026-08-20 перед переустановкой.
> Новый SSD: **>= 1 ТБ** (NVMe). Работа переносится на SSD.

## Диски

| Буква | Диск | Объём | Роль | Судьба при переустановке |
|---|---|---|---|---|
| C: | TS120GSSD220S | 112 ГБ (SATA) | Система | Будет заменена на новый SSD |
| D: | WDC WD10EZEX | 932 ГБ (HDD) | Данные: AI_Project, Obsidian, Ollama | **Не трогать** — отдельный физический диск |
| E: | Samsung 970 EVO Plus | 250 ГБ (NVMe) | SteamLibrary (225 ГБ игр) | Не трогать |
| F: | CD-ROM | — | привод | — |

## Сделано до переустановки

- [x] `D:\AI_Project` защищён: push на GitHub (ветка `main`, коммит `fbfa7fa`, снапшот 2026-08-20).
- [x] Аудиокниги >100 МБ исключены из git (4 файла), остались на D:.
- [x] Свежий бекап C: → `D:\SAVE\C_Backup\2026-08-20_2030` (8.2 ГБ).
- [x] BG3 сейвы (PlayerProfiles) + моды включены в бекап (скрипт обновлён).
- [x] .lmstudio (1.3 ГБ модели) включён в бекап.
- [x] Бекап закрывает: Saved Games, AppData\Roaming, Steam, браузеры (закладки/пароли), SSH, WiFi-пароли, список программ.

## Порядок восстановления

1. **Установить Windows на новый SSD** (не форматировать D: и E:).
2. Скопировать `D:\SAVE\` (бекап) на новую систему.
3. **Перенести работу на SSD**: `D:\AI_Project` → `C:\AI\Projects` (152.8 ГБ целиком, на 2TB влезет с огромным запасом).
   - Содержимое: Книги 71.5 ГБ, ollama 43.3 ГБ (модели — переехать в `C:\AI\Ollama` через `OLLAMA_MODELS`), Ежедневник 18.3 ГБ, hf-cache 5.7 (→ `C:\AI\HuggingFace` через `HF_HOME`), projects/tech и т.д.
   - Финальная разметка дисков (2TB / 250GB / HDD) и роли каждого — см. `tech/pc-build-plan.md`, раздел «Разметка дисков».
   - После переноса настроить `tech/backup-ai-work.ps1` (ежедневный robocopy-mirror `C:\AI\Projects` → `E:\Backup\AI_Project`) через Task Scheduler.
4. Восстановить сейвы: `Saved Games`, `AppData\Local\Larian Studios\Baldur's Gate 3` (PlayerProfiles+Mods).
5. Восстановить конфиги: `AppData\Roaming\*`, `.config\` (OpenCode, Ollama), `.lmstudio`.
6. Импортировать WiFi-пароли (`wifi_passwords.csv`).
7. Установить программы из `installed_programs.csv` (WezTerm, Obsidian, VS Code, OpenCode, Chrome, Firefox, Steam и др.).
8. Настроить SSH-ключи (бэкап в `D:\SAVE\C_Backup\<date>\SSH\`).

## Риски

- **Единственный риск для D:**: случайно отформатировать не тот диск при установке. Проверять букву/объём диска перед форматированием.
- Свободное место на D: — 106 ГБ; после бекапа и до переноса на SSD место не нужно (перенос наоборот освободит D:).