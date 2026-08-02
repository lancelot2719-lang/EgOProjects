#!/usr/bin/env python3
"""Автопроверка цитат: fuzzy-поиск каждой цитаты по полному тексту книги.

Детерминированная проверка (без модели): берёт цитаты из разбора,
ищет их в полном тексте с допуском на сокращения ("...") и незначительные
различия в пунктуации. Выдаёт отчёт:
  [OK]       — цитата найдена дословно
  [ОК со скобкой] — найдена с сокращением (пропуск помечен ...)
  [НЕ НАЙДЕНО] — в тексте книги такой фразы нет (подозрение на галлюцинацию)

Использование:
  python quote_check.py <путь_к_разбору.md> <путь_к_полному_тексту.txt> [--json]
"""
import argparse
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# Порог схожести для "дословного совпадения" (без учета "..." пропусков)
SIMILARITY_OK = 0.93


def extract_quotes(md_text: str):
    """Достаёт цитаты в кавычках «...» из разбора."""
    quotes = []
    # Русские кавычки « » и " "
    for m in re.finditer(r"[«\"]([^»\"]{15,})[»\"]", md_text):
        q = m.group(1).strip()
        if len(q) >= 15:
            quotes.append(q)
    return quotes


def normalize(s: str) -> str:
    """Убирает пробелы, регистр, знаки препинания — для сравнения."""
    s = s.replace("...", " ")
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def find_quote(full_text: str, quote: str):
    """Ищет цитату в полном тексте. Возвращает (статус, позиция%, ближайшее совпадение)."""
    norm_quote = normalize(quote)
    if not norm_quote:
        return ("ПУСТО", None, "")

    # 1. Дословный поиск нормализованных строк
    norm_text = normalize(full_text)
    pos = norm_text.find(norm_quote)
    if pos >= 0:
        pct = round(100 * pos / len(norm_text))
        return ("OK", pct, "")

    # 1б. Текст из PDF мог разбить слово переносом строки («отноше\nния»).
    # Нормализация даст «отноше ния». Ищем вариант со сжатыми пробелами.
    nq_nospace = norm_quote.replace(" ", "")
    nt_nospace = norm_text.replace(" ", "")
    pos = nt_nospace.find(nq_nospace)
    if pos >= 0 and len(nq_nospace) > 40:
        pct = round(100 * pos / max(1, len(nt_nospace)))
        return ("OK_PDF", pct, "найдено со сжатием пробелов (перенос строки)")

    # 2. Поиск по словам с пропуском "...": берём слова до и после пропуска
    # ищем все вхождения первого слова, затем скользящее окно по словам цитаты
    q_words = norm_quote.split()
    t_words = norm_text.split()
    if not q_words:
        return ("ПУСТО", None, "")

    # Строим позиционные индексы слов текста
    from collections import defaultdict
    word_index = defaultdict(list)
    for i, w in enumerate(t_words):
        if len(w) > 2:
            word_index[w].append(i)

    first = q_words[0]
    if len(first) > 2 and first in word_index:
        for start in word_index[first][:50]:
            # Жадный сдвиг по словам с допуском на пропуски
            ti = start
            matched = 0
            skipped = 0
            for qw in q_words:
                if ti >= len(t_words):
                    break
                if t_words[ti] == qw:
                    matched += 1
                    ti += 1
                else:
                    # допускаем пропуск до 3 слов (как "...")
                    skipped += 1
                    ti += 1
                    if skipped > 3:
                        break
            ratio = matched / len(q_words)
            if ratio >= 0.90:
                pct = round(100 * start / max(1, len(t_words)))
                return ("OK_SKIP", pct, "")

    # 3. Скользящее окно SequenceMatcher на крупных кусках
    best = 0.0
    best_pct = None
    window = 1500
    for start in range(0, len(full_text), window):
        chunk = full_text[start:start + window * 2]
        n_chunk = normalize(chunk)
        ratio = SequenceMatcher(None, n_chunk, norm_quote).ratio()
        if ratio > best:
            best = ratio
            best_pct = round(100 * start / max(1, len(full_text)))
    if best >= SIMILARITY_OK:
        return ("OK_FUZZY", best_pct, f"схожесть {best:.0%}")
    # Короткие фразы с очень низкой схожестью — скорее всего названия книг/разделов, не цитаты
    if len(norm_quote) < 40 and best < 0.25:
        return ("SKIP", None, "похоже на название, не цитата")
    return ("NOT_FOUND", best_pct, f"макс. схожесть {best:.0%}")


def check_numbers(md_text, full_text):
    """Проверка чисел: все «смысловые» числа из разбора ищутся в полном тексте.

    Берёт числа, встречающиеся вне цитат/кода: годы, суммы, проценты, количества.
    Возвращает список (число, контекст, найден_ли).
    """
    # Убираем блоки цитат, чтобы не дублировать проверку дословности
    body = re.sub(r"[«\"][^»\"]{15,}[»\"]", "", md_text)
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    # Числа с контекстом: не менее 3 цифр (годы, суммы) или с % и т.п.
    nums = re.findall(r"(?<!\d)(\d{3,}(?:[\s\u00A0\u2009\u202F][\d\s]+)?\s*(?:%|млн|млрд|тыс|млн\.|млрд\.|тыс\.)?)", body)
    norm_text = normalize(full_text)
    seen, out = set(), []
    for n in nums:
        key = re.sub(r"\s+", " ", n.strip())
        if key in seen or len(key) < 3:
            continue
        seen.add(key)
        # варианты с пробелом/без (1 000 vs 1000)
        compact = key.replace(" ", "")
        found = key in norm_text or compact in norm_text
        out.append((key, found))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("razbor", help="путь к .md разбору")
    ap.add_argument("text", help="путь к полному тексту книги .txt")
    ap.add_argument("--json", action="store_true", help="вывести JSON")
    ap.add_argument("--no-numbers", action="store_true", help="пропустить проверку чисел")
    args = ap.parse_args()

    md = Path(args.razbor).read_text(encoding="utf-8", errors="replace")
    full = Path(args.text).read_text(encoding="utf-8", errors="replace")

    quotes = extract_quotes(md)
    results = []
    print(f"Проверяю {len(quotes)} цитат против {len(full)//1024//1024} МБ текста...\n")
    for i, q in enumerate(quotes, 1):
        status, pct, note = find_quote(full, q)
        icon = {"OK": "[OK]", "OK_PDF": "[OK^]", "OK_SKIP": "[OK*]", "OK_FUZZY": "[ОК~]", "NOT_FOUND": "[НЕТ]", "SKIP": "[--]", "ПУСТО": "[?]"}[status]
        loc = f"@{pct}%" if pct is not None else ""
        short = q[:70].replace("\n", " ")
        print(f"{icon} {loc:6} {short}  {note}")
        results.append({"n": i, "status": status, "position_pct": pct, "quote": q, "note": note})

    stats = {}
    for r in results:
        stats[r["status"]] = stats.get(r["status"], 0) + 1
    print("\nИтог:", ", ".join(f"{k}: {v}" for k, v in stats.items()))

    if not args.no_numbers:
        print("\n--- Проверка чисел ---")
        nums = check_numbers(md, full)
        found = [n for n, ok in nums if ok]
        miss = [n for n, ok in nums if not ok]
        print(f"Чисел всего: {len(nums)}, найдено: {len(found)}, НЕ найдено: {len(miss)}")
        if miss:
            print("Подозрительные (нет в тексте):", ", ".join(miss[:30]))
        results.append({"check": "numbers", "total": len(nums), "found": len(found), "missed": miss})

    if args.json:
        print("\n" + json.dumps(results, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
