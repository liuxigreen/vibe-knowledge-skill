#!/usr/bin/env python3
"""流量评分表 (PLAN.md §2.8). Auto-scores what can be measured from beats.yaml + compiled.json + final video;
takes the judgement items (life scene, counter-intuitive point, identity) from meta.rubric and caps them at the weights.
usage: rubric.py <episode_dir> [final.mp4]   -> writes qa/rubric.json, exits 1 if < 70"""
import json, re, subprocess, sys
from pathlib import Path
import yaml
ep = Path(sys.argv[1]); final = sys.argv[2] if len(sys.argv) > 2 else None
B = yaml.safe_load((ep / "beats.yaml").read_text(encoding="utf-8")); C = json.loads((ep / "build/compiled.json").read_text(encoding="utf-8"))
man = B["meta"].get("rubric", {}); rows = []
def add(k, w, s, why): rows.append({"item": k, "weight": w, "score": max(0, min(w, s)), "why": why})
add("普适生活场景", 20, man.get("life_scene", {}).get("score", 0), "manual: " + man.get("life_scene", {}).get("why", ""))
nprimary_roles = sum(1 for b in B["beats"] if b["role"] == "反直觉")
add("单一反直觉点", 20, man.get("counterintuitive", {}).get("score", 0) if nprimary_roles == 1 else 8,
    f"manual: {man.get('counterintuitive', {}).get('why', '')}; auto: exactly {nprimary_roles} 反直觉 beat")
b0 = C["beats"][0]; hl = b0.get("headline", {}) or {}
q_vis = (hl.get("at", 9) <= 1.0) and any("？" in l or "?" in l for l in hl.get("lines", []))
dyn = [p["type"] for p in b0["props"] if p.get("at", 9) <= 1.0 and p["type"] not in ("Footnote", "SerifTitleCard")]
title_open = any(p["type"] == "SerifTitleCard" for p in b0["props"])
hook = (8 if q_vis else 0) + (4 if dyn else 0) + (0 if title_open else 3)
add("前3秒钩子", 15, hook, f"question headline visible ≤1s: {q_vis}; moving props ≤1s: {dyn}; opens on title card: {title_open}")
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", final], capture_output=True, text=True).stdout) if final else C["duration"]
# long-form lessons (meta.long_form, default for new episodes; set `long_form: false` for a short cut):
# full marks for 3–10 min. Short-form keeps the old 35–50s band.
LF = B["meta"].get("long_form", True)
if LF: add("时长", 10, 10 if 180 <= dur <= 600 else 6 if 120 <= dur < 180 or 600 < dur <= 720 else 2, f"{dur:.1f}s (long-form band 180–600s)")
else: add("时长", 10, 10 if 35 <= dur <= 50 else 5 if 60 <= dur <= 80 else 7 if dur < 60 else 0, f"{dur:.1f}s (short-form band 35–50s)")
last = B["beats"][-1]["narration"]; cta = re.search(r"发给|转给|你是哪", last)
add("分享式CTA", 10, 10 if cta and re.search(r"那个.{0,12}人|的人", last) else 5 if cta else 0, f"last beat: {re.sub(r'\[\[.*?\]\]', '', last)}")
card = [p for b in B["beats"] for p in b["props"] if p["type"] == "SerifTitleCard"]
add("可截图金句", 10, man.get("screenshot_line", {}).get("score", 0) if card else 0, f"{len(card)} SerifTitleCard; manual: {man.get('screenshot_line', {}).get('why', '')}")
fn = " ".join(str(b.get("footnote", "")) for b in B["beats"])
add("证据锚", 5, 5 if re.search(r"(19|20)\d\d", fn) and re.search(r"[A-Z][a-z]+", fn) else 0, "footnotes cite author+year")
add("问句标题", 5, 5 if re.search(r"^为什么.*[？?]$", B["meta"]["title"]) else 2, B["meta"]["title"])
add("身份/自我投射", 5, man.get("identity", {}).get("score", 0), "manual: " + man.get("identity", {}).get("why", ""))
total = sum(r["score"] for r in rows)
out = {"total": total, "pass_threshold": 70, "pass": total >= 70, "rows": rows}
(ep / "qa").mkdir(exist_ok=True); (ep / "qa/rubric.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
for r in rows: print(f'{r["item"]:<10}{r["score"]:>3}/{r["weight"]:<3} {r["why"]}')
print("TOTAL", total, "PASS" if total >= 70 else "FAIL"); sys.exit(0 if total >= 70 else 1)
