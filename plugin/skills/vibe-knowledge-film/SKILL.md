---
name: vibe-knowledge-film
description: >-
  Use when making a Vibe知识大赏 Douyin knowledge video (code-driven; VO or
  text-first by reference), or distilling a reference into a style base for that
  series.
---
# Vibe知识大赏 knowledge film

Styles, Award docs and tools live in this library (`github.com/liuxigreen/vibe-knowledge-skill`).

1. **Find `$LIB`.** Clone or open this repo; treat the repo root as `$LIB`.
2. **Read `$LIB/AGENTS.md` first**, then `DIRECTOR.md` / `TECHNIQUE.md` / `styles/<slug>/STYLE.md`.
3. **Never edit `styles/` for a user film** — copy KEEP grammar into the episode folder.

Before picking what to film, run [vibe-topic-pipeline](sand-workflow:vibe-topic-pipeline) unless the user already locked a topic.

Pipeline: `$LIB/` (styles/, episodes/<slug>/, tools/).

> **Core rule: a Skill gives the production flow, not taste.** Never jump straight to generating. Every episode passes the Reference Gate **and** Award Scorecard before batch render. Never claim「获奖级」from palette-only distill or prose scoring.

## Distill = 九项 (lesson 2026-10-31 · killed 旋律)
Palette alone is **not** a distill. Full checklist: `$LIB/docs/DISTILL-MULTIDIM.md` + Pre-score Gate in `docs/AWARD-SCORECARD.md` §0.
Before STYLE-BASE ship, lock **八维 + Mode证据两句 + 知识锚（出处/示意/易杠）**:
1. **Argument** — one mute-readable path + theory anchor + collision check
2. **Type ladder** ≥4 roles (kicker/hero/callout/foot) size·weight·color from densest frames
3. **Palette roles** — semantic duties, not decoration
4. **3s motion list** — what moves every beat; card-swap = fail
5. **In-frame show** — `docs/INFRAME-SHOW.md`; crop-bottom mute Gate; **禁图内字+底白同义复读**（底条稀疏辅助，少/短/偶尔）
6. **Props/gadgets** — persist+morph + ≥1 novel prop; BANNED twins
7. **Beat density** — hook ≤3–4s; typical beat ≤4–6s; no ~20s dwell
8. **BANNED twin list** — stranger can name the source → D fail
9. **Mode + 知识锚** — 听轨一句 + 密帧一句；出处/示意边界/易杠点

**Also lock narrative_mode** (`story_scene` / `diagram_bed` / `hybrid`) per `docs/STORY-SCENE-CRAFT.md` — see next section.

Audience test: would *you* swipe away? Beats Award padding. See `docs/DISTILL-REFLECT-melody-2026-10-31.md`.

Deliver: `STYLE-BASE.md` + `style-base.yaml` + `DISTILL-GAP.md` + `notes/teardown.md` + densest refs.

## 人物故事型 vs 图解床（2026-11-01 · 墨有意思渗流）
「像电视剧」≠ 死板模版。权威：`docs/STORY-SCENE-CRAFT.md`。密帧语法锚：`styles/moyou-story-percolation/`（墨有意思《没有回报的努力》· 渗流相变；**≠** `bite-red-queen` 红皇后跑步机）。

| 车道 | 何时用 | 底座锚 |
|---|---|---|
| **story_scene**（微剧场） | 人际/焦虑/卸防/平台期顿悟/「努力看不见回报」 | `moyou-story-percolation` · `nexo-crowd-phone` · `xiaomo-darkgold-disarm` · `sanhao-halo-effect` |
| **diagram_bed** | 波形/脑区/路线图/电路 | `moyou-darkgold-music` · `transit-map` · `circuit-board` |
| **hybrid** | 人物欲望线 + 一个 persist 机制床当**戏内道具** | 渗流：stick + LatticeBed |

**故事车道必须有的动画手法（KEEP · 从渗流蒸馏）：**
1. **同一角色可认回** — ≤3 人；跨幕姿态变，禁每屏新图标人。
2. **Persist 机制床 morph** — 主道具全程不换皮（格子/盾/波形）；状态差讲戏，禁 card-swap。
3. **计数/仪表是戏** — N/M、%、前后跳数跟着床状态走，不是旁白贴纸。
4. **长持 + 临界 snap** — 多数时间床在积；punch 砸在贯通/翻盘一瞬间（路径点亮、盾亮、泡变色）。
5. **字在戏里** — cream/ink hero 在卡内（常下三分之一或左上）；禁连续底白复读图内字。
6. **冲突→翻盘可见** — 钩受阻 → 机制露出 → 局势变 → 生活回扣；静帧第一反应是「这人卡在临界前」不是「又一张知识卡」。
7. **mini-TV 可选** — 竖卡嵌黑底 16:9 是源舞台语法之一；成片可全幅，但勿抄源 gestalt twin。

**反模版硬失败：** card-swap / 清单墙 / 只飘数字无人 / HUD 当讲义且舞台没人做事 / 底白同义复读。

故事 densest 额外交：角色卡 + 冲突→翻盘表（每格对应可见画面变化）+ 3s motion 里至少一次床状态差。

## Award / Gate after densest
1. densest ships **type ladder table + 3s motion list** beside frames（故事片再加冲突→翻盘表）。
2. Run Pre-score Gate **G0–G7** (`docs/AWARD-SCORECARD.md` §0)；print `crop-bottom mute: pass|fail`。**G7**：故事/hybrid 须有冲突→翻盘表 + 同一角色可认回；故事选题纯卡墙 → 不得 Pass。
3. Score /55 with **frame cites** for any C/G/T/N/X/D ≥4. If L/M≤3, soft-cap N/X/H/G/K at 4 (no inflate-to-44). **D**：命中 `moyou-story-percolation` BANNED（422/838、渗到底了+113→334、松手傍晚、面具钩、mini-TV+cream+金路径 gestalt）→ D≤2 Fail。
4. Write `qa/HUMAN-CHECK.md`：通用三问 + 故事片必填 **戏感三问**（谁跟谁较劲？10s局势变了吗？换文案同一道具还能演吗？）；任一 No → near-pass max。
5. **Vanity Pass ban**: no contact sheet / densest stills → Fail even if ≥44.
6. Hard-fail **G/T**: lecture only on bottom strip **or** on-canvas text echoed by continuous bottom white captions (六层 2026-10-31).
7. Hard-fail **故事选题用纯卡墙**（STORY-SCENE 反模版门 / G7）即使字好看。
8. `tools/award_score_check.py` numeric pass ≠ claim 获奖级. **勿宣称「获奖级」**：near-award process；Pass 仍要 densest 物证 + Gate 全绿。

## Progress / duration / mode
UPGRADE.md + PROGRESS-LADDER. Full **5–15 min dense** (not slow). Densest 10s. Mode from ref first. silent → we-never.
Story-lane full cuts still dense-edit（多拍），不是拖慢演戏；钩 ≤3–4s；典型叙事拍 ≤4–6s，但 **机制床长持计数** 允许作为单道具连续态（不算 ~20s 死停字卡）。

## Defaults
PC `D:\\Vibe知识大赏-试做` 中文三件套 · `?norun` · Award: `docs/AWARD-SCORECARD.md` (G0–G7+HUMAN-CHECK戏感三问+Vanity ban+禁底白复读 · 2026-11-01) · distill: DISTILL-MULTIDIM 九项 + STORY-SCENE narrative_mode · 故事锚 `moyou-story-percolation`

## Steps
1 topic-pipeline（锁 narrative_mode） 2 distill 九项+故事检查 Gate 3 densest type+motion(+冲突表) Gate 4 densest 5 Pre-score G0–G7 + Award + HUMAN-CHECK(含戏感三问) 6 iterate 7 Full 8 PC 9 ladder
