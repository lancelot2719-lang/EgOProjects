"""Translate the visible UI strings of a Papermorph engine copy into Russian.

Usage: python3 tools/vlast-golosa/ru_engine.py site/vlast-golosa/lib/engine.js
Each replacement must match exactly once (or the stated count); otherwise the script stops,
so an engine update that changes a string is noticed instead of silently left in English.
"""
import sys
from pathlib import Path

R = [
    ('aria-label="Lesson animation"', 'aria-label="Анимация урока"'),
    ('Paused. Press space or click to continue.', 'Пауза. Нажмите пробел или щёлкните, чтобы продолжить.'),
    ('aria-label="Keyboard shortcuts">', 'aria-label="Горячие клавиши">'),
    ('<h2>Keyboard shortcuts</h2>', '<h2>Горячие клавиши</h2>'),
    ('<h3>Lesson</h3>', '<h3>Урок</h3>'),
    ('<dd>Play or pause</dd>', '<dd>Пуск или пауза</dd>'),
    ('<dd>Previous or next step</dd>', '<dd>Предыдущий или следующий шаг</dd>'),
    ('<dd>Change step during a question</dd>', '<dd>Сменить шаг во время вопроса</dd>'),
    ('<dd>Start over</dd>', '<dd>Начать сначала</dd>'),
    ('<dd>Captions on or off</dd>', '<dd>Субтитры вкл./выкл.</dd>'),
    ('<dd>Full screen</dd>', '<dd>Полный экран</dd>'),
    ('<dd>Show this list</dd>', '<dd>Показать этот список</dd>'),
    ('<h3>Questions</h3>', '<h3>Вопросы</h3>'),
    ('<dd>Choose an answer or a ring</dd>', '<dd>Выбрать вариант ответа</dd>'),
    ('<dd>True or false</dd>', '<dd>Верно или неверно</dd>'),
    ('<dd>Move between rows</dd>', '<dd>Переход между строками</dd>'),
    ('<dd>Move along the number line, or pick a number to sort</dd>', '<dd>Перемещение по шкале или между объектами</dd>'),
    ('<dd>Check, then continue</dd>', '<dd>Проверить, затем продолжить</dd>'),
    ('<dd>Show the answer</dd>', '<dd>Показать ответ</dd>'),
    ('<dd>Leave an answer box</dd>', '<dd>Выйти из поля ответа</dd>'),
    ('Press <kbd>Esc</kbd> to close.', 'Нажмите <kbd>Esc</kbd>, чтобы закрыть.'),
    ('Sound could not play. The lesson continues with the on-screen text.', 'Звук не воспроизвёлся. Урок продолжается с текстом на экране.'),
    ('</svg>Start lesson</span>', '</svg>Начать урок</span>'),
    ('Press <kbd>Space</kbd> to start, <kbd>?</kbd> for shortcuts.', '<kbd>Пробел</kbd> — начать, <kbd>?</kbd> — горячие клавиши.'),
    ('aria-label="All chapters" title="All chapters"', 'aria-label="Все главы" title="Все главы"'),
    ('aria-label="Play or pause (space)"', 'aria-label="Пуск или пауза (пробел)"'),
    ('aria-label="Previous step (left arrow)"', 'aria-label="Предыдущий шаг (стрелка влево)"'),
    ('aria-label="Restart lesson"', 'aria-label="Начать урок заново"'),
    ('aria-label="Adjust volume"', 'aria-label="Громкость"'),
    ('title="Volume (0 = muted)"', 'title="Громкость (0 — без звука)"'),
    ('aria-label="Volume"', 'aria-label="Громкость"'),
    ('aria-label="Keyboard shortcuts (?)" title="Keyboard shortcuts (?)"', 'aria-label="Горячие клавиши (?)" title="Горячие клавиши (?)"'),
    ('aria-label="Captions (C)" title="Captions (C)"', 'aria-label="Субтитры (C)" title="Субтитры (C)"'),
    ('aria-label="Full screen"', 'aria-label="Полный экран"'),
    ("['t', 'True', null, 'T'], ['f', 'False', null, 'F']", "['t', 'Верно', null, 'T'], ['f', 'Неверно', null, 'F']"),
    ("t ? `${name}: ${r} of ${t} right on the first try.` : `${name}: not attempted.`",
     "t ? `${name}: с первой попытки верно ${r} из ${t}.` : `${name}: не пройдено.`"),
    ("h('a', 'btn quiet', 'All chapters')", "h('a', 'btn quiet', 'Все главы')"),
    ("['Watch again', kbd(", "['Смотреть снова', kbd("),
    ("['Next chapter', kbd('Enter')]", "['Следующая глава', kbd('Enter')]"),
    ("`Chapter ${CHAPTER.number} complete`", "`Глава ${CHAPTER.number} пройдена`"),
    ("line('Quick checks', sum('c-')), line('Chapter practice', sum('p-'))", "line('Быстрые проверки', sum('c-')), line('Практика', sum('p-'))"),
    ("label = 'Quick check')", "label = 'Быстрая проверка')"),
    ("['Check', kbd('Enter')]", "['Проверить', kbd('Enter')]"),
    ("['Show answer', kbd('S')]", "['Показать ответ', kbd('S')]"),
    ("'Next question' : 'Continue'", "'Следующий вопрос' : 'Продолжить'"),
    ("ok ? 'Correct. ' : 'Not quite. '", "ok ? 'Верно. ' : 'Не совсем. '"),
    ("['Answer: ', ...", "['Ответ: ', ..."),
    ("`   ${k + 1} of ${qs.length}`", "`   ${k + 1} из ${qs.length}`"),
    ("['Keys: ', ...ctl.hint]", "['Клавиши: ', ...ctl.hint]"),
    ("' choose, or click the grid'", "' выбрать, или щёлкните по сетке'"),
    ("' move along the line, ', kbd('Enter'), ' choose'", "' двигаться по шкале, ', kbd('Enter'), ' выбрать'"),
    ("' move, ', kbd('Enter'), ' choose, or click'", "' перемещение, ', kbd('Enter'), ' выбрать, или щёлкните'"),
    ("' move, ', kbd('Enter'), ' choose'", "' перемещение, ', kbd('Enter'), ' выбрать'"),
    ("[`${right} of ${rows.length} right. Fix the rows marked ✗ and check again.`]",
     "[`Правильных ответов: ${right} из ${rows.length}. Исправьте строки с ✗ и проверьте снова.`]", 2),
    ("'the correct choices are now selected.'", "'правильные варианты отмечены.'"),
    ("'the correct numbers are filled in.'", "'правильные числа подставлены.'"),
    ("'type numbers like 3/4 or −2 1/4, ' : 'type the number, '", "'вводите числа вида 3/4 или −2 1/4, ' : 'введите число, '"),
    ("' next box, ', kbd('Enter'), ' check, ', kbd('Esc'), ' leave the box'",
     "' следующее поле, ', kbd('Enter'), ' проверить, ', kbd('Esc'), ' выйти из поля'"),
    ("kbd('↓'), ' row, ']), ...(/\\d/.test(hot[0]) ? [kbd(hot[0]), '–', kbd(hot[hot.length - 1])] : hot.map(kbd)), ' choose']",
     "kbd('↓'), ' строка, ']), ...(/\\d/.test(hot[0]) ? [kbd(hot[0]), '–', kbd(hot[hot.length - 1])] : hot.map(kbd)), ' выбрать']"),
    ("`The point ${num(v)}`", "`Точка ${num(v)}`"),
    ("`Go to step ${i + 1}: ${b.title}`", "`Перейти к шагу ${i + 1}: ${b.title}`"),
    ("$('coverK').textContent = `Chapter ${CHAPTER.number}`;", "$('coverK').textContent = `Глава ${CHAPTER.number}`;"),
    ("`Lesson animation: ${CHAPTER.title}`", "`Анимация урока: ${CHAPTER.title}`"),
    ("`About ${CHAPTER.minutes} minutes, with sound and quick checks.`", "`Около ${CHAPTER.minutes} минут, со звуком и проверками.`"),
]

path = Path(sys.argv[1])
s = path.read_text(encoding="utf-8")
for item in R:
    old, new, n = (item + (1,))[:3]
    c = s.count(old)
    if c != n and s.count(new) == 0:
        sys.exit(f"expected {n}× {old!r}, found {c}")
    s = s.replace(old, new)
path.write_text(s, encoding="utf-8")
print("ok", len(R), "replacements")
