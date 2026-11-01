# Progressive OCR checks (contrast + numbers) straight from a render_resume frame cache, using qa_style.py's own code.
# usage: qa_partial.py <ep> <frames_dir> [fps=30]   -> judges only sample times whose frame already exists
import sys, json, re, cv2, numpy as np
from pathlib import Path
from rapidocr_onnxruntime import RapidOCR
ep = Path(sys.argv[1]); FD = Path(sys.argv[2]); fps = float(sys.argv[3]) if len(sys.argv) > 3 else 30; TMIN = float(sys.argv[4]) if len(sys.argv) > 4 else 0; TMAX = float(sys.argv[5]) if len(sys.argv) > 5 else 1e9
data = json.loads((ep / "build" / "compiled.json").read_text()); base = {}
src = (Path(__file__).parent / "qa_style.py").read_text()
dur = data["beats"][-1]["vend"]
times = [i + 0.5 for i in range(int(dur))]
cuts = [b["vstart"] for b in data["beats"][1:]]
times = [t if all(abs(t - c) > 0.35 for c in cuts) else t + 0.45 for t in times]
settled = set()
for b in data["beats"]:
    st = round(b["vend"] - 0.6, 2); settled.add(st); times.append(st)
frames = []
for t in sorted(set(times)):
    f = FD / f"f{int(round(t * fps)):05d}.jpg"
    if f.exists() and TMIN <= t <= TMAX: frames.append((t, cv2.imread(str(f))))
R = {"checks": {}}; ocr = RapidOCR(); light_craft = False
def check(name, ok, **info): R["checks"][name] = {"pass": bool(ok), **info}
seg = src[src.index("def lum(bgr):"): src.index('check("text_contrast_wcag"')]
seg2 = src[src.index('check("numbers_in_facts"'):].split("\n")[0:2]
exec(seg)
check("numbers_in_facts", not numbers_bad and not counter_src_bad, unknown=numbers_bad[:40], glued=glued_ocr[:10])
check("text_contrast_wcag", not low, failures=low[:60], boxes=len(contrast))
print("judged", len(frames), "frames up to t=", frames[-1][0] if frames else None)
print(json.dumps(R, ensure_ascii=False, indent=0, default=float))
