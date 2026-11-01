#!/usr/bin/env python3
"""Validate / print Award Scorecard verdict (2026-10-31 vanity-Pass harden).

Usage:
  award_score_check.py L=4 M=4 C=4 N=5 T=5 X=4 H=4 D=5 G=4 K=4 F=4
  award_score_check.py "L4 M4 C4 N5 T5 X4 H4 D5 G4 K4 F4"
  award_score_check.py ... --gate-fail          # Pre-score Gate failed → max near-pass
  award_score_check.py ... --human-fail         # HUMAN-CHECK any No → max near-pass
  award_score_check.py ... --vanity             # Vanity Pass ban → fail
  award_score_check.py ... --no-evidence-cap    # C/G/T/N/X/D claimed ≥4 without frame cites
                                              # → those dims treated as capped at 3 for verdict

Numeric Pass still requires L/M/F≥4 and N/X/D≥4 and total≥44.
Gate / HUMAN-CHECK / Vanity flags override: script Pass ≠ claim 获奖级 without docs.
See docs/AWARD-SCORECARD.md.
"""
import re, sys
KEYS = ["L", "M", "C", "N", "T", "X", "H", "D", "G", "K", "F"]
CN = dict(
    L="光影", M="材质", C="镜头", N="道具新意", T="静音字", X="文案吸睛",
    H="3s钩子", D="距离", G="机制手势", K="知识锚", F="静帧投稿",
)
# Dims that need densest-frame evidence to score ≥4
EVIDENCE_DIMS = ("C", "G", "T", "N", "X", "D")
# Soft-capped when L or M ≤3 (unless scorer asserts frame proof via --lm-exception)
SOFT_CAP_DIMS = ("N", "X", "H", "G", "K")


def parse(args):
    flags = {
        "gate_fail": False,
        "human_fail": False,
        "vanity": False,
        "no_evidence_cap": False,
        "lm_exception": False,
    }
    score_args = []
    for a in args:
        if a == "--gate-fail":
            flags["gate_fail"] = True
        elif a == "--human-fail":
            flags["human_fail"] = True
        elif a == "--vanity":
            flags["vanity"] = True
        elif a == "--no-evidence-cap":
            flags["no_evidence_cap"] = True
        elif a == "--lm-exception":
            flags["lm_exception"] = True
        else:
            score_args.append(a)
    s = " ".join(score_args)
    scores = {}
    for k in KEYS:
        m = re.search(rf"{k}\s*[=:]?\s*([1-5])", s, re.I)
        if not m:
            m = re.search(rf"{k}([1-5])", s)
        if not m:
            raise SystemExit(f"missing {k}")
        scores[k] = int(m.group(1))
    return scores, flags


def apply_caps(sc, flags):
    """Return (adjusted_scores, notes). Does not mutate caller copy beyond return."""
    out = dict(sc)
    notes = []
    if flags["no_evidence_cap"]:
        for k in EVIDENCE_DIMS:
            if out[k] >= 4:
                notes.append(f"{k}{sc[k]}→3 (无密帧证据，§1.1 封顶)")
                out[k] = 3
    if (out["L"] <= 3 or out["M"] <= 3) and not flags["lm_exception"]:
        for k in SOFT_CAP_DIMS:
            if out[k] >= 5:
                notes.append(f"{k}{sc[k]}→4 (L/M≤3 软顶，§2.1)")
                out[k] = 4
    return out, notes


def verdict(sc, flags):
    adj, cap_notes = apply_caps(sc, flags)
    total = sum(adj.values())
    hard_nxd = adj["N"] >= 4 and adj["X"] >= 4 and adj["D"] >= 4
    beauty = adj["L"] >= 4 and adj["M"] >= 4 and adj["F"] >= 4
    reasons = list(cap_notes)

    if flags["vanity"]:
        label = "fail"
        reasons.append("Vanity Pass ban: 无密帧物证却灌分≥4 → Fail（§2.2）")
    elif adj["N"] <= 2 or adj["X"] <= 2 or adj["D"] <= 2 or total < 33:
        label = "fail"
        if total < 33:
            reasons.append("总分 <33")
        if adj["N"] <= 2 or adj["X"] <= 2 or adj["D"] <= 2:
            reasons.append("N/X/D 任一 ≤2")
    elif total >= 44 and hard_nxd and beauty:
        label = "pass"
    else:
        label = "near-pass"

    # Gate / HUMAN-CHECK: demote Pass → near-pass
    if label == "pass" and flags["gate_fail"]:
        label = "near-pass"
        reasons.append("Pre-score Gate 未过 → 最高 near-pass（§0）")
    if label == "pass" and flags["human_fail"]:
        label = "near-pass"
        reasons.append("HUMAN-CHECK 任一 No/划走 → 最高 near-pass（§4）")

    if total >= 44 and hard_nxd and not beauty and label != "fail":
        reasons.append("美观硬门槛: L/M/F 需均≥4")
    if not hard_nxd and label != "fail":
        reasons.append("N/X/D 未全≥4")
    lows = [f"{k}{adj[k]}({CN[k]})" for k in KEYS if adj[k] <= 3]
    if lows:
        reasons.append("优先改: " + ", ".join(lows))
    if label == "pass":
        reasons.append(
            "脚本数字 Pass ≠ 可宣称获奖级：须 DISTILL-GAP 帧证 + HUMAN-CHECK 三问全过"
        )
    return total, label, reasons, adj


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sc, flags = parse(sys.argv[1:])
    total, label, reasons, adj = verdict(sc, flags)
    line = " ".join(f"{k}{adj[k]}" for k in KEYS)
    raw = " ".join(f"{k}{sc[k]}" for k in KEYS)
    print(f"Award Score: {line} = {total}/55 · {label}")
    if adj != sc:
        print(f"(raw input: {raw})")
    for r in reasons:
        print("-", r)
