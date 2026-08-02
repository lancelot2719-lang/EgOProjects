import genanki
import json
import os
from pathlib import Path

DECK_ID = 2059400110
MODEL_ID = 2059400111

DECK_NAME = "Слова и понятия"

model = genanki.Model(
    MODEL_ID,
    "Multiple Choice",
    fields=[
        {"name": "Word"},
        {"name": "Definition"},
        {"name": "Wrong1"},
        {"name": "Wrong2"},
        {"name": "Wrong3"},
    ],
    templates=[
        {
            "name": "MC Template",
            "qfmt": """
<div class="card">{{Word}}</div>
""",
            "afmt": """
<div class="card">{{Word}}</div>
<hr id="answer">
<div class="def">{{Definition}}</div>
""",
        }
    ],
    css="""
.card { font-size: 24px; text-align: center; margin-top: 40px; }
.def { font-size: 18px; color: #555; margin-top: 20px; }
""",
)

def create_deck(words: list[dict]) -> str:
    deck = genanki.Deck(DECK_ID, DECK_NAME)

    for w in words:
        note = genanki.Note(
            model=model,
            fields=[
                w["word"],
                w["definition"],
                w.get("wrong1", ""),
                w.get("wrong2", ""),
                w.get("wrong3", ""),
            ],
        )
        deck.add_note(note)

    out = Path(__file__).parent / "anki_words.apkg"
    genanki.Package(deck).write_to_file(str(out))
    return str(out)

if __name__ == "__main__":
    import sys
    words_file = sys.argv[1] if len(sys.argv) > 1 else "words.json"
    if os.path.exists(words_file):
        with open(words_file, encoding="utf-8") as f:
            words = json.load(f)
        path = create_deck(words)
        print(f"Deck saved: {path}")
    else:
        print(f"File not found: {words_file}")
