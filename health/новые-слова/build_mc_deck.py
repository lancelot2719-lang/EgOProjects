import genanki
import json
import random
import os
from pathlib import Path

DECK_ID = 2059400110
MODEL_ID = 2059400112
DECK_NAME = "Умные слова — smogue.com"

FRONT_HTML = """<div class="mc-wrap">
  <div class="word-row">
    <span class="word">{{Word}}</span>
    {{#PartOfSpeech}}<span class="pos">{{PartOfSpeech}}</span>{{/PartOfSpeech}}
  </div>
  <div class="opts" id="opts">
    <button class="btn" data-correct="1" onclick="pick(this,1)">{{Definition}}</button>
    <button class="btn" data-correct="0" onclick="pick(this,0)">{{Wrong1}}</button>
    <button class="btn" data-correct="0" onclick="pick(this,0)">{{Wrong2}}</button>
    <button class="btn" data-correct="0" onclick="pick(this,0)">{{Wrong3}}</button>
  </div>
  <div id="fb"></div>
  <div class="bottom-bar">
    <span class="streak" id="streak">&#x1f525; 0</span>
    <span class="easy-star" id="easyStar" onclick="toggleEasy()">&#x2606;</span>
  </div>
</div>
<script>
(function(){
  var done = false;
  var opts = document.getElementById('opts');
  var children = Array.from(opts.children);
  children.sort(function(){return 0.5-Math.random()});
  children.forEach(function(b){opts.appendChild(b)});
  var fb = document.getElementById('fb');

  window.pick = function(btn, ok){
    if(done)return;
    var all = document.querySelectorAll('.btn');
    all.forEach(function(b){b.disabled=true});
    if(ok){
      done=true;
      btn.classList.add('ok');
      fb.innerHTML='<span class="ok-txt">&#x2713; Верно!</span>';
      var s = parseInt(localStorage.getItem('mc_streak')||'0')+1;
      localStorage.setItem('mc_streak',s);
      document.getElementById('streak').innerHTML='&#x1f525; '+s;
    } else {
      btn.classList.add('no');
      localStorage.setItem('mc_streak','0');
      document.getElementById('streak').innerHTML='&#x1f525; 0';
      fb.innerHTML='<span class="no-txt">&#x2717; Неверно</span>';
      setTimeout(function(){
        btn.classList.remove('no');
        btn.disabled=false;
        all.forEach(function(b){if(!done)b.disabled=false});
        fb.innerHTML='';
      },700);
    }
  };

  var s = parseInt(localStorage.getItem('mc_streak')||'0');
  document.getElementById('streak').innerHTML='&#x1f525; '+s;

  window.toggleEasy = function(){
    var star = document.getElementById('easyStar');
    var key = 'easy_'+'{{Word}}';
    var val = localStorage.getItem(key);
    if(val==='1'){
      localStorage.removeItem(key);
      star.innerHTML='&#x2606;';
    } else {
      localStorage.setItem(key,'1');
      star.innerHTML='&#x2605;';
    }
  };
  if(localStorage.getItem('easy_{{Word}}')==='1'){
    document.getElementById('easyStar').innerHTML='&#x2605;';
  }
})();
</script>"""

BACK_HTML = """<div class="word-row">
  <span class="word">{{Word}}</span>
  {{#PartOfSpeech}}<span class="pos">{{PartOfSpeech}}</span>{{/PartOfSpeech}}
</div>
<hr id="answer">
<div class="def">{{Definition}}</div>
<div class="easy-hint" id="easyHint"></div>
<script>
(function(){
  var key = 'easy_{{Word}}';
  var hint = document.getElementById('easyHint');
  if(localStorage.getItem(key)==='1'){
    hint.innerHTML = '&#x2b50; Помечено как лёгкое (эта сессия)';
  }
})();
</script>"""

CSS = """
* { box-sizing: border-box; }
.mc-wrap { max-width: 600px; margin: 0 auto; padding: 20px; font-family: 'Segoe UI', Arial, sans-serif; }
.word-row { text-align: center; margin: 30px 0 10px; display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap; }
.word { font-size: 30px; font-weight: 700; color: #1a1a2e; letter-spacing: 0.5px; }
.pos { font-size: 13px; font-weight: 600; color: #fff; background: #6c63ff; padding: 3px 10px; border-radius: 20px; letter-spacing: 0.3px; }
.opts { display: flex; flex-direction: column; gap: 10px; max-width: 540px; margin: 20px auto; }
.btn { padding: 14px 20px; font-size: 16px; line-height: 1.4; border: 2px solid #dde; border-radius: 12px; background: #f8f9ff; color: #1a1a2e; cursor: pointer; transition: all .15s ease; }
.btn:hover { border-color: #6c63ff; background: #f0f0ff; transform: translateY(-1px); box-shadow: 0 2px 8px rgba(108,99,255,.15); }
.btn.ok { background: #d4edda; border-color: #28a745; animation: pulse-green .3s ease; }
.btn.no { background: #f8d7da; border-color: #dc3545; animation: shake .3s ease; }
.btn:disabled { opacity: .7; cursor: default; transform: none; }
#fb { text-align: center; margin: 15px 0; font-size: 20px; font-weight: 700; min-height: 30px; }
.ok-txt { color: #28a745; }
.no-txt { color: #dc3545; }
.bottom-bar { display: flex; justify-content: space-between; align-items: center; margin-top: 10px; padding: 0 10px; }
.streak { font-size: 16px; color: #666; }
.easy-star { font-size: 28px; cursor: pointer; color: #f5b342; transition: transform .2s ease; user-select: none; }
.easy-star:hover { transform: scale(1.25); }
#answer { border: none; border-top: 1px solid #ddd; margin: 20px 0; }
.def { font-size: 18px; color: #333; text-align: center; line-height: 1.6; padding: 0 20px; }
.easy-hint { text-align: center; margin-top: 15px; font-size: 15px; color: #f5b342; }
@keyframes pulse-green { 0%{transform:scale(1)} 50%{transform:scale(1.02)} 100%{transform:scale(1)} }
@keyframes shake { 0%,100%{transform:translateX(0)} 20%{transform:translateX(-6px)} 40%{transform:translateX(6px)} 60%{transform:translateX(-4px)} 80%{transform:translateX(4px)} }
"""

model = genanki.Model(
    MODEL_ID,
    "Smogue MC v2",
    fields=[
        {"name": "Word"},
        {"name": "Definition"},
        {"name": "Wrong1"},
        {"name": "Wrong2"},
        {"name": "Wrong3"},
        {"name": "PartOfSpeech"},
    ],
    templates=[{"name": "Card", "qfmt": FRONT_HTML, "afmt": BACK_HTML}],
    css=CSS,
)


def build_deck(words: list[dict]) -> str:
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for i, w in enumerate(words):
        others = [x["definition"] for j, x in enumerate(words) if j != i]
        wrongs = random.sample(others, min(3, len(others)))
        while len(wrongs) < 3:
            wrongs.append("")
        note = genanki.Note(
            model=model,
            fields=[
                w["word"],
                w["definition"],
                wrongs[0],
                wrongs[1],
                wrongs[2],
                w.get("partOfSpeech", ""),
            ],
        )
        deck.add_note(note)
    out = Path(__file__).parent / "umnye_slova_mc.apkg"
    genanki.Package(deck).write_to_file(str(out))
    return str(out)


if __name__ == "__main__":
    path = Path(__file__).parent / "words.json"
    with open(path, encoding="utf-8") as f:
        words = json.load(f)
    random.shuffle(words)
    print(f"Loaded {len(words)} words")
    out = build_deck(words)
    print(f"Saved: {out}")
