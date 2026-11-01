#!/usr/bin/env python3
"""contrast_scan.py <frames_dir_or_files...> [--band sub|all] — same WCAG measure as qa_style, prints every box below threshold."""
import sys, glob, os, re, cv2, numpy as np
from rapidocr_onnxruntime import RapidOCR
ocr = RapidOCR(); band = sys.argv[sys.argv.index('--band') + 1] if '--band' in sys.argv else 'all'
need = float(sys.argv[sys.argv.index('--need') + 1]) if '--need' in sys.argv else 4.5
args = [a for i, a in enumerate(sys.argv[1:], 1) if not a.startswith('--') and sys.argv[i - 1] not in ('--band', '--need')]
files = sorted(sum([sorted(glob.glob(a + '/*.jpg')) if os.path.isdir(a) else [a] for a in args], []))
def lum(bgr):
    c = bgr[::-1] / 255.0; c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
for f in files:
    im = cv2.imread(f); y_off = 0
    if band == 'sub': y_off = 900; im2 = im[900:1080]
    else: im2 = im
    res, _ = ocr(im2)
    for box, txt, conf in (res or []):
        if float(conf) < .6: continue
        xs, ys = [p[0] for p in box], [p[1] + y_off for p in box]
        x0, x1, y0, y1 = int(max(min(xs), 0)), int(min(max(xs), 1919)), int(max(min(ys), 0)), int(min(max(ys), 1079))
        roi = im[y0:y1, x0:x1].reshape(-1, 3).astype(float)
        if len(roi) < 30: continue
        g = roi.mean(1); pad = 14; X0, X1, Y0, Y1 = max(x0 - pad, 0), min(x1 + pad, 1919), max(y0 - pad, 0), min(y1 + pad, 1079)
        ring = np.concatenate([im[Y0:y0, X0:X1].reshape(-1, 3), im[y1:Y1, X0:X1].reshape(-1, 3), im[Y0:Y1, X0:x0].reshape(-1, 3), im[Y0:Y1, x1:X1].reshape(-1, 3)]).astype(float)
        bgc = np.median(ring, 0)
        cr = max(((max(lum(fg), lum(bgc)) + .05) / (min(lum(fg), lum(bgc)) + .05)) for fg in (roi[g >= np.percentile(g, 92)].mean(0), roi[g <= np.percentile(g, 8)].mean(0)))
        kind = "footnote" if y0 > 1015 else ("subtitle" if 920 < y0 < 1015 else "content")
        if band == 'sub' and kind != 'subtitle': continue
        th = {'content': need, 'subtitle': 4.5, 'footnote': 3.0}[kind]
        if cr < th: print(f"{os.path.basename(f)}\t{kind}\t{cr:.2f}\t{txt}\t[{x0},{y0},{x1},{y1}]")
