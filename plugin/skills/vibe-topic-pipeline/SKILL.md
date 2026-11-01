---
name: vibe-topic-pipeline
description: >-
  Use when picking, ranking, or batching Vibe知识大赏 Douyin knowledge-video topics,
  or when the user asks what to film next.
---
# Vibe知识大赏 topic pipeline

Output a ranked shortlist (usually 5–10) plus which craft base/template each would use. Pair with [vibe-knowledge-film](sand-workflow:vibe-knowledge-film) when making the film.

**Mode is per topic/ref:** suggest `silent` or `vo` from the intended craft base and whether the argument needs spoken narration. Do not force every topic silent.

## Progress ladder (required)
Every new topic must beat the last shipped episode on **at least one** axis, written in the shortlist row:
1. **Theory-family** — not the same mechanism family as a recent episode (see collision ban).
2. **Craft upgrade** — new base family, or same family with a named grammar leap (e.g. note-walk, clip-plane pour, HUD→prop).
3. **Prop novelty (N)** — ≥1 new allegory prop vs last same-family ep.
4. **Explain depth** — enough beats to teach the mechanism (silent story often **~45s–3min**); **no padding to hit minutes**; densest Gate stays 10s.

Maintain `$LIB/docs/PROGRESS-LADDER.md` (episode #, theory family, craft leap, what failed last time). Aim for **≥20 shipped episodes** so leaps compound into a house style that can break out — not automatic 爆款; distribution/taste still human.

### Theory-family collision ban
Do **not** schedule two episodes in the same batch (or adjacent publish) that a stranger would summarize as the same tip. Known collisions:
- **提取练习 / 学习曲线** — 越学越快 (chunking/fluency) ≈ 划重点还是记不住 (testing effect) → pick **one** learning-science lane per 5 eps, or force a different life scene **and** different craft + hook axis.
- **暗金社交话术** — 六层卸防 twins.
- **音乐预期** — Salimpoor / DROP twins without new walk grammar.

If two candidates share a family, keep the higher-score one and replace the other.

## Mix (default)
- **~70–80% main track** — 生活场景 + 核心理论 + 哲学升华, with a **冲突钩子** and **行动指引**.
- **~20–30% side track** — heat / AI / tool explainers. Still need a life hook and an action tip.
- At least **1 music×大脑 / 感知** topic in every batch of 5+ unless the user says otherwise.
- Prefer **template breakthrough**: don't assign two consecutive episodes the same craft family.

## Main-track formula (required fields)
1. **生活场景** — concrete lived moment.
2. **冲突钩子** (first 3s) — 反常识 / 数字反差 / 痛点 / 悬念.
3. **核心理论** — one named mechanism + real citation.
4. **哲学升华** — tip → worldview.
5. **行动指引** — <2 minutes today.
6. **本集升级点** — one sentence: what is strictly better than last ship.

Also note suggested **mode** (`silent` | `vo`) and **craft base**.

Structure on screen: 生活钩子 → 核心机制 → 反直觉 → 哲学升华 + 行动指引 → CTA.

## Side-track / craft hints
- Agent/workflow → Lemo `desktop-flythrough` / isometric / circuit-board (often silent).
- Music×brain → dark-gold with **path-walk** annotations (often silent).
- Learning/metacognition → `zhongshan-learn-fast` (often silent) — check collision ban.
- Bias/first impression → `sanhao-halo-effect`.
- History/textbook → `lailong-*`.

## Music / perception seed bank
Earworm / absolute pitch / speech-to-song / Salimpoor anticipation / groove — re-verify papers before `facts.md`.

## Scoring
Scene · counterintuitive · measurable vars · cite · action · title-as-question · template novelty · screenshotability · **upgrade vs last ship**. Prefer ≥42/70; **fail shortlist row** if upgrade field empty or theory-family collision.

## Steps
1. Read PROGRESS-LADDER + last 3 shipped theory families.
2. Scan heat + seed bank + constraints.
3. 5–10 one-liners with base + mode + **upgrade point**.
4. Drop collisions; mark top 2 with different templates.
5. On go-ahead → vibe-knowledge-film.
