#!/usr/bin/env python3
"""compare.py REF_DIR SAMPLE.mp4 OUT.png [--ref f1,f2,..] [--t 1,3.5,6,9]
Side-by-side: top row = reference frames, bottom row = sample frames; per-frame stats
(mean luma, RMS contrast, p2/p98 luma, WCAG ratio of p98 vs p2 ≈ text-on-bg contrast, mean saturation)."""
import sys, subprocess, tempfile, json, argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np
ap = argparse.ArgumentParser(); ap.add_argument("ref"); ap.add_argument("sample"); ap.add_argument("out")
ap.add_argument("--ref-frames", default=""); ap.add_argument("--t", default="1,3.5,6,9")
a = ap.parse_args()
def lin(c): c = c / 255.0; return np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
def stats(im):
    x = np.asarray(im.convert("RGB").resize((480, 270))).astype(float)
    L = 0.2126 * lin(x[..., 0]) + 0.7152 * lin(x[..., 1]) + 0.0722 * lin(x[..., 2])
    y = 0.299 * x[..., 0] + 0.587 * x[..., 1] + 0.114 * x[..., 2]
    hsv = np.asarray(im.convert("RGB").resize((480, 270)).convert("HSV")).astype(float)
    p2, p98 = np.percentile(L, 2), np.percentile(L, 99.5)
    return dict(luma=round(y.mean(), 1), rms=round(y.std(), 1), wcag=round((p98 + .05) / (p2 + .05), 1), sat=round(hsv[..., 1].mean() / 255, 3),
                busy=round(float((np.abs(np.diff(y, axis=1)) > 12).mean()), 3))
refs = sorted(Path(a.ref).glob("*.jpg")) + sorted(Path(a.ref).glob("*.png"))
refs = [r for r in refs if not r.name.startswith(("sheet", "quad"))]
if a.ref_frames: refs = [Path(a.ref) / n for n in a.ref_frames.split(",")]
else: refs = [refs[int(i * (len(refs) - 1) / 3)] for i in range(4)]
ts = [float(v) for v in a.t.split(",")]
tmp = Path(tempfile.mkdtemp()); sams = []
for i, t in enumerate(ts):
    p = tmp / f"s{i}.png"; subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", a.sample, "-frames:v", "1", str(p)], check=True); sams.append(p)
W, H = 640, 360; n = max(len(refs), len(sams))
canvas = Image.new("RGB", (n * (W + 8) + 8, 2 * (H + 70) + 60), (24, 24, 24)); d = ImageDraw.Draw(canvas)
try: fnt = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 18)
except Exception: fnt = ImageFont.load_default()
d.text((10, 10), f"TOP: reference ({Path(a.ref).name})   BOTTOM: sample ({Path(a.sample).name})", fill=(255, 255, 255), font=fnt)
agg = {"ref": [], "sample": []}
for row, (lab, lst) in enumerate([("ref", refs), ("sample", sams)]):
    for i, p in enumerate(lst):
        im = Image.open(p); s = stats(im); agg[lab].append(s)
        x, y = 8 + i * (W + 8), 40 + row * (H + 70)
        canvas.paste(im.convert("RGB").resize((W, H)), (x, y))
        d.text((x, y + H + 6), f"luma {s['luma']}  rms {s['rms']}  wcag {s['wcag']}:1", fill=(255, 220, 150), font=fnt)
        d.text((x, y + H + 30), f"sat {s['sat']}  busy {s['busy']}  " + (p.name if lab == 'ref' else f"t={ts[i]}s"), fill=(200, 200, 200), font=fnt)
canvas.save(a.out)
mean = {k: {m: round(float(np.mean([s[m] for s in v])), 3) for m in v[0]} for k, v in agg.items()}
Path(a.out).with_suffix(".json").write_text(json.dumps(mean, indent=1)); print(json.dumps(mean))
