# DISTILL-GAP · nexo-crowd-phone（2026-10-31 · 九项补丁后）

> 对照 `docs/DISTILL-MULTIDIM.md` + 高 ROI 补丁任务。  
> 本轮：**文档底座**升到九项缺维；**未**重渲染 sample。

## Audit before → after

| Dim | Before patch | After harden |
|---|---|---|
| A Argument | LOCK | LOCK（骨架保留 + 撞车句） |
| T Type ladder | SOFT（表有层、缺证据帧/≥4 硬级） | **LOCK**（hero·data_num·narrative·pill/callout·cite · 约 px@1080 · 证据帧） |
| P Palette roles | LOCK | LOCK |
| M 3s motion | **MISS** / 软叙事 | **LOCK**（密窗 A/B · `t+0…` · f0028–f0035） |
| I In-frame | SOFT / 散落 | **LOCK**（§5 INFRAME + crop-bottom mute Gate） |
| R Props | LOCK | LOCK（表加 twin 列） |
| B Beat density | SOFT | SOFT→偏 LOCK（密窗硬锁；全片时间码仍软） |
| D BANNED twins | SOFT / 禁止段散写 | **LOCK**（B1–B8 签名表） |
| Mo Mode | **LOCK** | **LOCK**（听轨一句 + 密帧一句表保留） |
| K 知识锚 | **MISS** | **LOCK**（Pew 出处 · 示意边界 · 易杠 · 免责） |

## Locked this pass（证据）

- Mode：bass-heavy 连续 BGM + 0 silence · 密帧底栏/图内字 = 脚本 → `silent_text_first`（先前已 LOCK）
- Type：1024×576 密帧 ×~1.875 → @1080 **约**值（hero≈88；narrative≈44；callout≈28；cite≈22）
- Motion：`keyframes/06-f0028`–`09-f0035` · 源 ~27–36s Self-focus HUD → PhoneShield
- INFRAME：裁底栏后注视/紧张表/盾仍须讲完机制；Gate 必写 `crop-bottom mute`
- BANNED：灰人群vs铜lone、双眼标+角框、紧张表签名位、三联自检原文、PhoneShield+安全行为句、自我关注底栏原文、序界 gestalt、换皮/串家族
- 知识锚：Pew 式社调须机构+年；HUD 示意；四条易杠；禁无脚注假数字

## Still open（勿虚高 Pass）

| Gap | Status | Note |
|---|---|---|
| Sample Gate 像素 / anatomy | SOFT | 既有 near-pass：pill 偏扁、眼标偏薄、盾/表液面未 pixel twin |
| 字阶精确到设计稿 px | SOFT 余量 | 源 576p → 表内一律「约」；未做 OCR bbox |
| 数据拍 timed 动势（~15s Pew+栅格） | SOFT | 签名但次密；episode 需要时再锁 |
| 翻盘拍全构图（~45s） | SOFT | 叙事已覆盖；全构图可选 |
| BGM 曲名版权核验 | SOFT | 听轨确认无 VO；曲名仍用 we-never 工作床 |
| 长片 beat 加密样例 | SOFT | 规则已写，无 5–15 min 样片 |

## Silent 10s sample Gate（未重跑）

Densest cut: ~27–36s / `f0028`–`f0035` self-focus → phone-shield.  
Path: `sample-silent-10s/`

**Matched（文档期望）：** silent；底栏 concept+narrative；PillCrowd/PillSelf；Gaze；Tension；Callouts；Shield 语法。  
**Still short（既有诚实缺口）：** pill anatomy、眼标 chrome、表液面、背景竖板、callout 引线半径。  
→ **near-pass**，不是满分。本轮**未**重渲染。

## Gate checklist（蒸馏完成 · 文档层）

- [x] 8 维有密帧证据句
- [x] Mode 两句表（先前 LOCK）
- [x] 知识锚 出处+示意+易杠+免责
- [x] 字阶表 ≥4 + 3s 动势贴 densest
- [x] INFRAME + crop-bottom mute 规则
- [x] BANNED B1–B8
- [ ] 自己静音连看 densest 不划走 — **样片仍 near-pass，新片须重验**
- [ ] Award 预评禁虚高 — 对照 B1–B8 / 字阶 / 动势再打

## Do not claim

- Full pass / pixel twin while sample anatomy gaps open.
- 未重跑 sample 却宣称本轮 craft Pass。

## Next（parent queue）

1. 新社交集：新隐喻 + N≥1；禁 B1–B8。  
2. 可选：补 pill anatomy / 眼标后再跑 sample（**非本任务**）。  
3. 并行队列：dianzi 补丁 / xiaomo 重蒸（若仍开）。
