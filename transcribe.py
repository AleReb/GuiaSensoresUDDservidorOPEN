import json, whisper, os
from pathlib import Path

audio = r"C:\Users\Ale\Documents\Zoom\2026-02-20 10.09.18 Reunión de Zoom de Alejandro Rebolledo\audio1675864608.m4a"
out = Path(r"C:\Users\Ale\Documents\Zoom\2026-02-20 10.09.18 Reunión de Zoom de Alejandro Rebolledo\analysis")
out.mkdir(parents=True, exist_ok=True)
model = whisper.load_model("base")
res = model.transcribe(audio, language="es", task="transcribe", fp16=False, verbose=False)
(out/"transcript.txt").write_text(res.get("text",""), encoding="utf-8")
(out/"transcript.json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
print("ok", len(res.get("segments", [])))
