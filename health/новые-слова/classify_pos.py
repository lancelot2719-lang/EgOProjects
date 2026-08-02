import json
from pathlib import Path
from pymorphy2 import MorphAnalyzer

morph = MorphAnalyzer()

POS_MAP = {
    "NOUN":  "сущ.",
    "ADJF":  "прил.",
    "ADJS":  "прил.",
    "COMP":  "прил.",
    "VERB":  "глаг.",
    "INFN":  "глаг.",
    "PRTF":  "прич.",
    "PRTS":  "прич.",
    "GRND":  "деепр.",
    "ADVB":  "нареч.",
    "NUMR":  "числ.",
    "NPRO":  "мест.",
    "PREP":  "предл.",
    "CONJ":  "союз",
    "PRCL":  "част.",
    "INTJ":  "межд.",
    "PRED":  "предик.",
}

OVERRIDES = {
    "Гипоним": "сущ.",
    "Декантер": "сущ.",
    "Эксизм": "сущ.",
    "Ангажировать": "глаг.",
    "Нивелировать": "глаг.",
    "Превалировать": "глаг.",
    "Эпатировать": "глаг.",
    "Резонёрствовать": "глаг.",
    "Кантовать": "глаг.",
    "Транслировать": "глаг.",
}

def _fallback(word: str) -> str:
    """Guess POS by suffix for unknown words."""
    ending = word.lower()
    if ending.endswith(("ть", "чь", "ти")) and len(ending) > 3:
        return "глаг."
    if ending.endswith(("о", "е", "ё")) and len(ending) > 2:
        return "нареч."
    if ending.endswith(("ый", "ий", "ой", "ая", "ое", "ые", "его", "ому", "ым", "ом")):
        return "прил."
    return ""

def classify(word: str) -> str:
    if word in OVERRIDES:
        return OVERRIDES[word]
    p = morph.parse(word)[0]
    gram = p.tag
    if "UNKN" in gram or gram.POS is None:
        return _fallback(word)
    return POS_MAP.get(gram.POS, gram.POS or "")

path = Path(__file__).parent / "words.json"
with open(path, encoding="utf-8") as f:
    words = json.load(f)

ok = skip = 0
for w in words:
    pos = classify(w["word"])
    w["partOfSpeech"] = pos
    if pos:
        ok += 1
    else:
        skip += 1

with open(path, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Processed: {len(words)} words")
print(f"Recognized: {ok}, Unrecognized: {skip}")
uniq = set(w["partOfSpeech"] for w in words if w["partOfSpeech"])
print(f"POS found: {sorted(uniq)}")
