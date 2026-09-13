#!/usr/bin/env python3
"""
Однокомандный запуск анализа книги. Настрой один раз блок DEFAULTS ниже под
себя — дальше команда всегда одна и та же, дальше ничего руками не делаешь:

    python analyze.py "D:\\путь\\к\\книге.txt"
    python analyze.py "D:\\AI_Project\\localTest\\parts_prodat"

Скрипт сам:
1. Проверяет, жив ли сервер LM Studio, и если нет — пробует поднять (lms server start).
2. Определяет, дан ли сырой текст книги (нарежет сам) или уже готовая папка с частями
   part*.txt (использует как есть).
3. Запускает run_pipeline.py со всеми нужными флагами.
4. В конце печатает путь к готовому файлу и пытается открыть его автоматически.

Можно также перетащить файл/папку на analyze.bat в проводнике Windows — без
консольных команд вообще.
"""

import glob
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))

# ==================== НАСТРОЙ ОДИН РАЗ ПОД СЕБЯ ====================
DEFAULTS = dict(
    prompts=os.path.join(HERE, "prompts"),
    out_root=os.path.join(HERE, "results"),   # куда складывать результаты всех книг

    extractor_model="openai/gpt-oss-20b",
    extractor_context=60000,

    validator_model="qwen/qwen3.6-27b",
    validator_context=24576,

    base_url="http://127.0.0.1:1234/v1",
    lms_path="lms",   # если lms не в PATH — укажи полный путь к lms.exe
)
# =====================================================================


def server_alive(base_url: str, timeout: int = 3) -> bool:
    try:
        urllib.request.urlopen(base_url.rstrip("/") + "/models", timeout=timeout)
        return True
    except Exception:
        return False


def ensure_server(lms_path: str, base_url: str) -> bool:
    if server_alive(base_url):
        print("LM Studio сервер уже запущен.")
        return True

    print("Сервер не отвечает, пробую поднять (lms server start)...")
    try:
        subprocess.run([lms_path, "server", "start"], capture_output=True, text=True, timeout=60)
    except FileNotFoundError:
        print(f"Не найдена команда '{lms_path}'. Открой LM Studio вручную хотя бы раз "
              f"(это ставит lms в PATH), либо пропиши полный путь в DEFAULTS['lms_path'].")
        return False
    except Exception as e:
        print(f"lms server start вернул ошибку: {e}")

    for _ in range(15):
        if server_alive(base_url):
            print("Сервер поднялся, продолжаю.")
            return True
        time.sleep(2)

    print("Не удалось автоматически поднять сервер. Открой приложение LM Studio "
          "(можно свёрнутым) и запусти команду ещё раз.")
    return False


def looks_like_parts_dir(path: str) -> bool:
    return os.path.isdir(path) and bool(glob.glob(os.path.join(path, "part*.txt")))


def sanitize(name: str) -> str:
    import re
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip() or "book"


def main():
    if len(sys.argv) < 2:
        print("Использование: python analyze.py <путь к .txt книги ИЛИ к папке с готовыми частями>")
        sys.exit(1)

    target = sys.argv[1].strip('"')
    if not os.path.exists(target):
        print(f"Путь не найден: {target}")
        sys.exit(1)

    if not ensure_server(DEFAULTS["lms_path"], DEFAULTS["base_url"]):
        sys.exit(1)

    run_pipeline_path = os.path.join(HERE, "run_pipeline.py")
    cmd = [
        sys.executable, run_pipeline_path,
        "--prompts", DEFAULTS["prompts"],
        "--out-root", DEFAULTS["out_root"],
        "--extractor-model", DEFAULTS["extractor_model"],
        "--extractor-context", str(DEFAULTS["extractor_context"]),
        "--validator-model", DEFAULTS["validator_model"],
        "--validator-context", str(DEFAULTS["validator_context"]),
        "--base-url", DEFAULTS["base_url"],
        "--lms-path", DEFAULTS["lms_path"],
    ]

    is_parts = looks_like_parts_dir(target)
    cmd += ["--parts", target] if is_parts else ["--book", target]

    print(f"Запускаю пайплайн для: {target} ({'готовые части' if is_parts else 'сырой текст/папка книг'})")
    print("-" * 60)
    result = subprocess.run(cmd)
    print("-" * 60)

    if result.returncode != 0:
        print("Пайплайн завершился с ошибкой — смотри вывод выше и pipeline.log в папке результата.")
        sys.exit(result.returncode)

    # Пытаемся найти и открыть готовый файл (работает для одиночной книги;
    # при обработке целой папки книг — просто загляни в DEFAULTS['out_root']).
    if not os.path.isdir(target) or is_parts:
        name = os.path.basename(os.path.normpath(target)) if is_parts else \
            os.path.splitext(os.path.basename(target))[0]
        final_path = os.path.join(DEFAULTS["out_root"], sanitize(name), "out", "book_final.md")
        if os.path.isfile(final_path):
            print(f"Готово: {final_path}")
            if hasattr(os, "startfile"):
                try:
                    os.startfile(final_path)
                except Exception:
                    pass
        else:
            print(f"Пайплайн завершился, но итоговый файл не найден по ожидаемому пути: {final_path}")
    else:
        print(f"Готово. Результаты всех книг — в {DEFAULTS['out_root']}")


if __name__ == "__main__":
    main()
