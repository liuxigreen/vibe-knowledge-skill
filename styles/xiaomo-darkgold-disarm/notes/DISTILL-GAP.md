# DISTILL-GAP · xiaomo-darkgold-disarm（2026-10-31 · 九项重蒸后）

> 对照 `docs/DISTILL-MULTIDIM.md` + `docs/BASES-GAP-AUDIT-2026-10-31.md` xiaomo 行。  
> 本轮：**文档底座**升到九项；**未**重渲染 sample。  
> 别名：`zhanwai-darkgold-huashu` → 本底座（见 `../zhanwai-darkgold-huashu/DIFF.md`）。

## Audit before → after

| Dim | Audit 2026-10-31 | After harden |
|---|---|---|
| A Argument | LOCK | LOCK（六层路径 + 撞车句） |
| T Type ladder | SOFT | **LOCK**（≥4：HUD/hero/callout/narrative/foot · 约 px@1080） |
| P Palette roles | LOCK | LOCK（金正路 / 红错路） |
| M 3s motion | **MISS** | **LOCK**（钩/层卡/WrongRight densest/底牌/CTA · `t+0…`） |
| I In-frame | LOCK | LOCK（crop-bottom 硬门槛保留） |
| R Props | LOCK | LOCK（表加 twin 列） |
| B Beat density | SOFT | SOFT→偏 LOCK（表已写；长片加密仍软） |
| D BANNED twins | SOFT | **LOCK**（B1–B9） |
| Mo Mode | SOFT | **LOCK**（听轨一句 + 密帧一句；底栏=designed_narrative） |
| K 知识锚 | SOFT | **LOCK**（互惠暴露 · Voss · FBI Elicitation · 示意 · 易杠） |

## What we got wrong (v1–v2 · 保留备忘)

| Wrong assumption | Where it lived | Why wrong |
|---|---|---|
| Bottom band = VO **字幕** | 旧 `type.subtitle` / 「字幕：衬线 48px」 | 帧上是**设计叙事句**（脚本 UI），不是口播转录 |
| `under_voice` duck | 旧 bgm | 无 VO；duck 无意义 |
| 「每句口播换标题」 | density / ep prompts | Silent = 论证拍推进道具，非语音句 |
| 只锁色板 / 无字阶+动势 | melody 反思同病 | Award 虚高 Pass |

## Locked this pass（证据）

- Mode：无 VO 听轨惯例 + `01`/`08`/`24`/`30` 密帧 → `silent_text_first` · 底栏 `designed_narrative`
- Type：1080 源帧 + yaml → HUD≈32–40 · 层卡 hero≈120–150 · bubble callout≈32–40 · narrative≈44–56 · foot≈22–28
- Motion：钩盾 · 层卡呼吸 · densest WrongRight（sample t24–t30）· HoleCards · DualVote
- BANNED：六划 HUD、六层卸防双语卡、脸+防御盾钩、错对堆叠、嫌贵/竞品双卡、情商心机 CTA、六层名序列、站在外面 gestalt、换皮三联
- 知识锚：互惠暴露 / Voss 镜像 / FBI Elicitation · 四条易杠 · 示意免责
- 别名一句：`zhanwai-darkgold-huashu` 不另开底座

## Still open（勿虚高 Pass）

| Gap | Status | Note |
|---|---|---|
| Sample Gate 像素 / chrome | SOFT | v5 near-pass：泡辉光/金属金标题渐变仍薄；无「两人一起扛」窗 |
| 字阶精确 OCR bbox | SOFT | 表内「约」；未做像素级量字 |
| 全片逐秒动势 | SOFT | 已锁五段；其余层例未逐秒 |
| BGM 版权核验 | SOFT | we-never 工作床 |
| 长片 beat 加密样例 | SOFT | 规则已写，无 5–15 min 样片 |
| zhanwai 目录 | 挂起薄 | 只留 DIFF；新 ep 一律 `base: xiaomo-darkgold-disarm` |

## Silent 10s sample Gate v5（未重跑）

Densest cut: **弱点献祭 wrong/right → 风险>收益** ≈ ref t24–t30。  
Artifacts: `sample-silent-10s/out/sample_silent_10s_bgm.mp4` · `qa/contact_matched.png` · `qa/stills_v5/`。

**Matched：** silent；LayerHUD+pill；错对 FSM；NarrativeLine；RiskBenefit；mute-readable；WCAG≈ref。  
**Still short：** avatar/chrome；dust 暖度；后段桌戏未进 10s。  
→ **near-pass**，不是满分。

## Gate checklist（蒸馏完成 · 文档层）

- [x] 8 维有密帧证据句
- [x] Mode 两句表
- [x] 知识锚 出处+示意+易杠+免责
- [x] 字阶表 + 3s 动势贴 densest
- [ ] 自己静音连看 densest 不划走 — **样片仍 near-pass，新片须重验**
- [ ] Award 预评禁虚高 — 对照 B1–B9 / 字阶 / 动势再打

## Next（parent queue）

1. 补丁队列：`dianzi-info-surprisal` / 其余 SOFT 底座（若未完）。  
2. 新社交卸防集：新隐喻 + N≥1；禁 B1–B9；`base: xiaomo-darkgold-disarm`。  
3. 可选：sample v6 加厚泡辉光（**非本任务**）。
