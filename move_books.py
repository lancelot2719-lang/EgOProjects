import os, shutil

ROOT = r"D:\AI_Project\Книги"

def move_file(src_rel, dst_folder):
    """Move a file (and its .fb2 pair if exists) from src_rel to dst_folder."""
    src = os.path.join(ROOT, src_rel)
    dst = os.path.join(ROOT, dst_folder)
    os.makedirs(dst, exist_ok=True)

    if not os.path.exists(src):
        print(f"  NOT FOUND: {src_rel}")
        return

    # Move main file
    dst_path = os.path.join(dst, os.path.basename(src))
    shutil.move(src, dst_path)
    print(f"  MOVED: {src_rel[:60]:60s} -> {dst_folder}")

    # Also move companion FB2 if exists
    base = os.path.splitext(src)[0]
    fb2_path = base + ".fb2"
    if os.path.exists(fb2_path):
        dst_fb2 = os.path.join(dst, os.path.basename(fb2_path))
        if not os.path.exists(dst_fb2):
            shutil.move(fb2_path, dst_fb2)
            print(f"  +FB2: {os.path.basename(fb2_path)[:55]} -> {dst_folder}")

    # Also move companion TXT if exists
    txt_path = base + ".txt"
    if os.path.exists(txt_path):
        dst_txt = os.path.join(dst, os.path.basename(txt_path))
        if not os.path.exists(dst_txt):
            shutil.move(txt_path, dst_txt)

print("=" * 70)
print("MOVING BOOKS TO CORRECT FOLDERS")
print("=" * 70)

# ===== 1. FIX MISPLACED IN FINANCE =====
print("\n--- Fixing Финансы: moving to Продажи ---")
moves_finance = [
    # (source_rel_path, dest_folder_name)
    ("Финансы/Решетняк Владимир - Основы продаж.pdf", "Продажи"),
]

for f, dst in moves_finance:
    move_file(f, dst)

# ===== 2. MOVE FINANCE BOOKS TO BETTER CATEGORIES =====
print("\n--- From Финансы to other folders ---")
moves_finance2 = [
    ("Финансы/Короткий С - Терминаторный менеджмент.pdf", "Бизнес, менеджмент"),
    ("Финансы/Хилл Наполеон - Механизмы работы мозга которые делают нас богатыми.pdf", "Мышление, привычки, навыки"),
    ("Финансы/Хилл Наполеон - Самое главное Думай и богатей.pdf", "Мышление, привычки, навыки"),
    ("Финансы/Хилл Наполеон - Золотой стандарт успеха и богатства 52 правила.pdf", "Мышление, привычки, навыки"),
    ("Финансы/Десаи Михир - Разумный финансист.pdf", "Бизнес, менеджмент"),
]
for f, dst in moves_finance2:
    move_file(f, dst)

# ===== 3. MOVE PSYCHOLOGY BOOKS FROM Развитие =====
print("\n--- From Развитие to Психология ---")
moves_psych = [
    ("Развитие/Ялом-И.-Экзистенциальная-психотерапия.pdf", "Психология"),
    ("Развитие/КПТ расстройств личности, Бек А. (2002).pdf", "Психология"),
    ("Развитие/1.pdf", "Психология"),  # Freud
    ("Развитие/Найду Ума - Беспокойный мозг Полезный гайд по снижению тревожности и стресса.pdf", "Психология"),
    ("Развитие/Брегман Питер - Эмоциональная смелость.pdf", "Психология"),
    ("Развитие/Вонг Майкл - Искусство маленьких шагов Заботливое руководство по обретению радости.pdf", "Психология"),
    ("Развитие/Короткий С - Жизнь как квест или Путе-Шествие канатоходца.pdf", "Психология"),
    ("Развитие/Херман Тодд - Эффект альтер эго Ваш скрытый ресурс на пути к большим целям.pdf", "Психология"),
    ("Развитие/Гоулман Дэниел - Социальный интеллект Новая наука о человеческих отношениях.pdf", "Психология"),
    ("Развитие/Гоулман Дэниел - Фокус внимания.pdf", "Психология"),
    ("Развитие/Гоулман Дэниел - Эмоциональная устойчивость Снизить тревожность и избавиться от навязчивых мыслей с помощью медитации.pdf", "Психология"),
    ("Развитие/Гоулман Дэниел - Эмоциональный интеллект вбизнесе.pdf", "Психология"),
    ("Развитие/Тонкое_искусство_пофигизма_Парадоксальныи_способ_жить_счастливо.pdf", "Психология"),
    ("Развитие/56786282.pdf", "Психология"),  # Nagoski Burnout
    ("Развитие/Tatyana_Muchickaya_Zoopark_v_tvoei_golove._25_psihologicheskih_sindromov_kotorye_meshaut_nam_chit_ltr.pdf", "Психология"),
    ("Развитие/Мужицкая Татьяна - Зоопарк в твоей голове 20 Еще 25 психологических синдромов которые мешают нам жить.pdf", "Психология"),
    ("Развитие/Makgonigal-K.-Sila-voli.-Kak-razvit-i-ukrepit-2012.pdf", "Психология"),
    ("Развитие/Andrey_Kurpatov_Chertogi_razuma_Ubey_v_sebe_idiota_33_2019.pdf", "Психология"),
    ("Развитие/Andrey_Kurpatov_Chetvyortaya_mirovaya_voyna.pdf", "Психология"),
    ("Развитие/Andrey_Kurpatov_Krasnaya_tabletka_Posmotri_pravde_v_glaza.pdf", "Психология"),
    ("Развитие/Andrey_Kurpatov_Troitsa_Bud_bolshe_samogo_sebya.pdf", "Психология"),
    ("Развитие/Kurpatov_Andrey_-_Krasnaya_tabletka-2_-_2020.pdf", "Психология"),
    ("Развитие/Mozg-ne-otlichaet-sobytij-vneshnego-mira-ot-teh.pdf", "Психология"),  # Dispenza
    ("Развитие/16.-Сапольски-Роберт.-Психология-стресса.pdf", "Психология"),
    ("Развитие/Кинг Патрик - Учитесь думать с помощью мысленных экспериментов.pdf", "Психология"),
    ("Развитие/Гамильтон Дэвид - Безграничная сила разума Как ваше сознание может исцелить ваше тело.pdf", "Психология"),
    ("Развитие/Демиденко Артем - Никакой инерционной фигни Руководство по жизни на своих условиях.pdf", "Психология"),
    ("Развитие/Василий Чибисов – Вся фигня – от мозга_!.pdf", "Психология"),
    ("Развитие/Кинг Патрик - Как читать людей быстро Думай как психолог анализируй поведение и расшифровывай эмоции.pdf", "Психология"),
    ("Развитие/Кинг Патрик - Как контролировать эмоции Обретите равновесие устойчивость спокойствие свободу от стресса тревожности и негатива.pdf", "Психология"),
    ("Развитие/Daniel_Kahneman-Thinking_Fast_and_Slow-RU.pdf", "Психология"),
]
for f, dst in moves_psych:
    move_file(f, dst)

# ===== 4. MOVE MINDSET/PRODUCTIVITY BOOKS =====
print("\n--- From Развитие to Мышление, привычки, навыки ---")
moves_mindset = [
    ("Развитие/Atomnye_privychki.pdf", "Мышление, привычки, навыки"),
    ("Развитие/mihay-chiksentmihayi-potok-psihologiya-optimalnogo-perezhivaniya.pdf", "Мышление, привычки, навыки"),
    ("Развитие/Stiven_Kovi_-_7_navykov_vysokoeffektivnykh_lyudey_Moschnye_instrumenty_razvitia_lichnosti.pdf", "Мышление, привычки, навыки"),
    ("Развитие/Braian_Treisi_Vyidi_iz_zony_komforta._Izmeni_svou_chizn_ltr.pdf", "Мышление, привычки, навыки"),
    ("Развитие/ff06f7b7-58e6-4f4c-bb7f-ce70c3215497.pdf", "Мышление, привычки, навыки"),  # Eat That Frog
    ("Развитие/1641907026_jessencializm_-put-k-prostote_makkeon-g_2015-254s.pdf", "Мышление, привычки, навыки"),
    ("Развитие/Джозеф Джебелли – Займись ничем_ система долгосрочной продуктивности.pdf", "Мышление, привычки, навыки"),
    ("Развитие/Лещенко Елена - Саммари книги Тони Шварца То как мы работаем не работает.pdf", "Мышление, привычки, навыки"),
    ("Развитие/Ньето-Родригес Антонио - Цель как проект Как успешно решать любые задачи с помощью проектного подхода.pdf", "Мышление, привычки, навыки"),
    ("Развитие/Льюис Харви - Принципы успеха Эффективные приемы розенкрейцеров для бизнеса и жизни.pdf", "Мышление, привычки, навыки"),
    ("Развитие/Манган Джеймс - Умение продвигать себя.pdf", "Мышление, привычки, навыки"),
    ("Развитие/Хилл Наполеон - Принципы изобилия Как правильное мышление помогает достигать целей и исполнять желания (1).pdf", "Мышление, привычки, навыки"),
    ("Развитие/Хилл Наполеон - Принципы изобилия Как правильное мышление помогает достигать целей и исполнять желания.pdf", "Мышление, привычки, навыки"),
    ("Развитие/avidreaders.ru__kak-reshayut-problemy-silnye-lyudi.pdf", "Мышление, привычки, навыки"),
    ("Развитие/Райан Холидей - Как решают проблемы сильные люди.pdf", "Мышление, привычки, навыки"),
]
for f, dst in moves_mindset:
    move_file(f, dst)

# ===== 5. MOVE ESOTERIC BOOKS =====
print("\n--- From Развитие to Эзотерика, духовность ---")
moves_esoteric = [
    ("Развитие/Бекенва Ольга - Чакры и характер или Как жить в ресурсе.pdf", "Эзотерика, духовность"),
    ("Развитие/Кинслоу Фрэнк - Секрет мгновенного исцеления Квантовая синхронизация здоровья.pdf", "Эзотерика, духовность"),
    ("Развитие/Dukhovny_marketing.pdf", "Эзотерика, духовность"),
    ("Развитие/Zastav_sebya_dumat_33_Andrey_Kurpatov__kopia.pdf", "Эзотерика, духовность"),
    ("Развитие/d0bad0b0d0ba-d187d0b5d0bbd0bed0b2d0b5d0ba-d0bcd18bd181d0bbd0b8d182-d0b4d0b6d0b5d0b9d0bcd181-d0b0d0bbd0bbd0b5d0bd.pdf", "Эзотерика, духовность"),
    ("Развитие/Кинг Патрик - Справочник мастера харизмы 174 поведенческих правила.pdf", "Общение, красноречие"),
    ("Развитие/Кинг Патрик - Как быть веселым остроумным и креативным.pdf", "Общение, красноречие"),
    ("Развитие/Демиденко Артем - Переговоры на грани Как выигрывать сложные диалоги.pdf", "Общение, красноречие"),
    ("Развитие/Хьюстон Тереза - Обратная связь Как сказать все что думаешь и получить все что хочешь.pdf", "Общение, красноречие"),
    ("Развитие/Юри Уильям - Мы можем договориться Стратегии разрешения сложных конфликтов.pdf", "Общение, красноречие"),
    ("Развитие/Гоулстон Марк - Умение слушать осознанно.pdf", "Общение, красноречие"),
    ("Развитие/Якуба Владимир - Продажник идет в сеть Как продавать через мессенджеры и соцсети.pdf", "Продажи"),
]

# Check if the PDF exists in Развитие first, since some might have been moved already
for f, dst in moves_esoteric:
    src = os.path.join(ROOT, f)
    if os.path.exists(src):
        move_file(f, dst)

# ===== 6. ZIP FILES (esoteric) =====
print("\n--- Moving .zip esoteric files ---")
zip_moves = [
    ("Развитие/dalay-lama-otkrytoye-serdtse-pdf.zip", "Эзотерика, духовность"),
    ("Развитие/elena-petrovna-blavatskaya-samopoznaniye-volya-i-zhelaniye-pdf.zip", "Эзотерика, духовность"),
    ("Развитие/ernst-kholms-sila-razuma-pdf.zip", "Эзотерика, духовность"),
    ("Развитие/germes-trismegist-aforizmy-pdf.zip", "Эзотерика, духовность"),
    ("Развитие/shri-aurobindo-mysli-i-aforizmy-pdf.zip", "Эзотерика, духовность"),
    ("Развитие/rayan-kholidey-kak-reshayut-problemy-silnyye-lyudi-pdf.zip", "Эзотерика, духовность"),
]
for f, dst in zip_moves:
    src = os.path.join(ROOT, f)
    if os.path.exists(src):
        move_file(f, dst)

print("\n" + "=" * 70)
print("DONE! All moves completed.")
print("=" * 70)
