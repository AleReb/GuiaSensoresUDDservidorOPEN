import json, re, subprocess
from pathlib import Path

analysis = Path(r"C:\Users\Ale\Documents\Zoom\2026-02-20 10.09.18 Reunión de Zoom de Alejandro Rebolledo\analysis")
video = Path(r"C:\Users\Ale\Documents\Zoom\2026-02-20 10.09.18 Reunión de Zoom de Alejandro Rebolledo\video1675864608.mp4")
frames = analysis / "frames"
frames.mkdir(parents=True, exist_ok=True)

j = json.loads((analysis/"transcript.json").read_text(encoding="utf-8"))
segs = j.get("segments", [])

keywords = [
  r"registr", r"sensor", r"variables?", r"unidad", r"conductiv", r"crear", r"relaci", r"editar", r"datasheet", r"agregar"
]
pat = re.compile("|".join(keywords), re.IGNORECASE)

candidates = []
for s in segs:
    txt = s.get("text", "").strip()
    if pat.search(txt):
        score = sum(1 for k in keywords if re.search(k, txt, re.IGNORECASE))
        candidates.append((score, float(s.get("start",0)), float(s.get("end",0)), txt))

# Deduplicate by minute bucket and keep strongest
picked = []
used_bucket = set()
for item in sorted(candidates, key=lambda x: (-x[0], x[1])):
    b = int(item[1] // 20)  # bucket each 20s
    if b in used_bucket:
        continue
    used_bucket.add(b)
    picked.append(item)
    if len(picked) == 8:
        break

picked = sorted(picked, key=lambda x: x[1])

rows = []
for i,(score,start,end,txt) in enumerate(picked, start=1):
    t = max(0.0, start + 0.2)
    hh = int(t//3600); mm = int((t%3600)//60); ss = t%60
    ts = f"{hh:02d}:{mm:02d}:{ss:06.3f}"
    out = frames / f"step_{i:02d}_{int(start):04d}s.jpg"
    cmd = ["ffmpeg","-y","-ss",ts,"-i",str(video),"-frames:v","1","-q:v","2",str(out)]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    rows.append({"step":i,"start":start,"end":end,"timestamp":ts,"text":txt,"frame":str(out)})

(analysis/"important_steps.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
print("picked", len(rows))
for r in rows:
    print(r["step"], r["timestamp"], r["text"][:90])
