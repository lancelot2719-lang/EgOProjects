"""Preview timings without network TTS: silent MP3s plus estimated word/mark times.

Usage: python3 tools/vlast-golosa/fake_tts.py content/vlast-golosa/ch06/narration.ru.json site/vlast-golosa/ch06/audio/ru

Writes timings.js in the same format as the skill's tts.py, so the page runs and can be
screenshotted. Replace with real audio by running tts.py where Edge TTS is reachable;
real runs overwrite these files (the real cache file is separate and is not created here).
"""
import json, re, subprocess, sys
from pathlib import Path

MARK = re.compile(r"\[\[(\w+)\]\]")
WPS = 2.35          # spoken words per second for ru-RU-DmitryNeural at -4% (rough)

def est(raw):
    t, marks, cues, sent_start, sent = 0.1, {}, [], 0.1, []
    for tok in re.split(r"(\[\[\w+\]\]|\s+)", raw):
        if not tok or tok.isspace():
            continue
        m = MARK.fullmatch(tok)
        if m:
            marks[m.group(1)] = round(t, 3)
            continue
        if not sent:
            sent_start = t
        sent.append(tok)
        letters = len(re.sub(r"\W", "", tok))
        t += 0.12 + letters * 0.062
        if tok.endswith((",", ":", "—", ";")):
            t += 0.22
        if tok.endswith((".", "?", "!")):
            t += 0.45
            cues.append([round(sent_start, 3), " ".join(sent)]); sent = []
    if sent:
        cues.append([round(sent_start, 3), " ".join(sent)])
    return round(t + 0.3, 3), marks, cues

src, out = Path(sys.argv[1]), Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
spec = json.loads(src.read_text(encoding="utf-8"))
res = {}
for beat, raw in spec["beats"].items():
    dur, marks, cues = est(raw)
    res[beat] = {"dur": dur, "marks": marks, "cues": cues}
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                    "-t", str(dur), "-c:a", "libmp3lame", "-b:a", "32k", str(out / f"{beat}.mp3")], check=True)
(out / "timings.js").write_text("window.TIMINGS = " + json.dumps(res, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
print("\n".join(f"{b:9s} {v['dur']:6.1f}s  marks: {', '.join(v['marks'])}" for b, v in res.items()))
print(f"total ≈ {sum(v['dur'] for v in res.values()) / 60:.1f} min of narration (preview estimate)")
