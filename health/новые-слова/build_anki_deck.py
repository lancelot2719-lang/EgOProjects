import genanki
import json
from pathlib import Path

DECK_ID = 2059400110
MODEL_ID = 2059400111

DECK_NAME = "Умные слова — smogue.com"

model = genanki.Model(
    MODEL_ID,
    "Smogue Words",
    fields=[
        {"name": "Word"},
        {"name": "Definition"},
        {"name": "Wrong1"},
        {"name": "Wrong2"},
        {"name": "Wrong3"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": '<div class="card">{{Word}}</div>',
            "afmt": '{{FrontSide}}<hr id="answer"><div class="def">{{Definition}}</div>',
        }
    ],
    css="""
.card { font-size: 28px; text-align: center; margin-top: 60px; font-weight: bold; }
.def { font-size: 18px; color: #444; text-align: center; margin-top: 20px; padding: 0 20px; line-height: 1.5; }
""",
)

def load_words() -> list[dict]:
    words_path = Path(__file__).parent / "words.json"
    with open(words_path, encoding="utf-8") as f:
        return json.load(f)

def build_deck(words: list[dict]) -> str:
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for w in words:
        note = genanki.Note(
            model=model,
            fields=[w["word"], w["definition"], w.get("wrong1", ""), w.get("wrong2", ""), w.get("wrong3", "")]
        )
        deck.add_note(note)
    out = Path(__file__).parent / "umnye_slova.apkg"
    genanki.Package(deck).write_to_file(str(out))
    return str(out)

if __name__ == "__main__":
    words = load_words()
    print(f"Loaded {len(words)} words")
    path = build_deck(words)
    print(f"Deck saved: {path}")
