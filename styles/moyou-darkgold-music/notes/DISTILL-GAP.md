# DISTILL-GAP · moyou-darkgold-music（2026-10-31 · 九项重蒸后）

> 对照 `docs/DISTILL-MULTIDIM.md` + `docs/BASES-GAP-AUDIT-2026-10-31.md` moyou 行。  
> 本轮：**文档底座**升到九项；**未**重渲染 sample。

## Audit before → after

| Dim | Audit 2026-10-31 | After harden |
|---|---|---|
| A Argument | LOCK | LOCK（骨架保留 + theory-family 撞车句） |
| T Type ladder | SOFT | **LOCK**（≥4 级 · 约 px@1080 · 色·重·位 · 证据帧） |
| P Palette roles | LOCK | LOCK |
| M 3s motion | **MISS** | **LOCK**（钩/DROP/脑/拖/倒计时 · `t+0…`） |
| I In-frame | LOCK | LOCK |
| R Props | LOCK | LOCK（表加 twin 列） |
| B Beat density | SOFT | SOFT→偏 LOCK（表已写；长片加密规则仍软） |
| D BANNED twins | SOFT | **LOCK**（B1–B7 签名） |
| Mo Mode | SOFT | **LOCK**（听轨一句 + 密帧一句表） |
| K 知识锚 | SOFT | **LOCK**（Salimpoor · 示意 · 易杠 · 免责） |

## What we got wrong (v1 · 保留备忘)

| Wrong assumption | Where it lived | Why wrong |
|---|---|---|
| 「Every VO sentence gets its own headline」 | 旧 STYLE-BASE | No VO. Headlines change per **argument beat**; bed persists |
| `type.subtitle` band 900–1000 | 旧 yaml | Dense frames **no** bottom caption strip |
| `under_voice` duck | 旧 bgm | 假口播混音 |
| 只锁色板/persist 口号 | melody 反思 | 缺字阶+动势 → Award 虚高 Pass |

## Locked this pass（证据）

- Mode：前 20s AAC 听轨 + `d_001`/`d_005` 密帧句 → `silent_text_first`
- Type：720p timed still 字高 ×1.5 → @1080 **约**值（hero≈106；kicker/yaml 40；callout≈32–40；foot≈22–28）
- Motion：`refs/motion-stills/t001_5|t003_5|t005_5|t015_0|t028_0` + moyou-dense
- BANNED：波形+DROP+peg、钩双句、BrainHUD 双条、尾状核/伏隔核+15s 窗、反直觉·06、墨有意思 gestalt、换皮三联
- 知识锚：Salimpoor 2011 · N=8 示意 · 四条易杠

## Still open（勿虚高 Pass）

| Gap | Status | Note |
|---|---|---|
| Sample Gate 像素 / luma | SOFT | v5 near-pass：luma sample~31.6 vs densest ref~39.7；高潮白线偏光滑；无 PET 等轴测真身 |
| 字阶精确到设计稿 px | SOFT 余量 | 源 720 + 密帧 480 代理 → 表内一律「约」；未做 OCR bbox |
| 全片逐秒动势表 | SOFT | 已锁 densest 五段；中段过渡拍未逐秒 |
| BGM 曲名版权核验 | SOFT | 听轨确认无 VO；曲名仍用 we-never 工作床 |
| IsoScanner 道具入库 | SOFT | 源 ~6–8s 有扫描仪拍；样片用 BrainOutline 代替 |
| 长片 beat 加密样例 | SOFT | 规则已写，无 5–15 min 样片 |
| ep2《美丽的神话》 | 挂起 | 同色板更多 A/B 音频 UI — 另开 props，不回 VO |

## Silent 10s sample Gate v5（未重跑）

Densest cut: hook → DROP ≈ ref 1.5–7.5s / `d_005`.  
Artifacts: `sample-silent-10s/out/sample_silent_10s_bgm.mp4` · `qa/contact_matched.png` · `qa/stills_v5/`.

**Matched：** silent；左上字阶；无底栏叙事；WaveformBed；ExpectDropCurves；BrainHUD；BrainOutline；脚注；WCAG 近。  
**Still short：** luma；曲线光滑；无 MRI iso；peg 粗；粒噪轻。  
→ **near-pass**，不是满分。

## Gate checklist（蒸馏完成 · 文档层）

- [x] 8 维有密帧证据句
- [x] Mode 两句表
- [x] 知识锚 出处+示意+易杠+免责
- [x] 字阶表 + 3s 动势贴 densest
- [ ] 自己静音连看 densest 不划走 — **样片仍 near-pass，新片须重验**
- [ ] Award 预评禁虚高 — 对照 B1–B7 / 字阶 / 动势再打

## Next（parent queue）

1. 必重蒸 #2 `xiaomo-darkgold-disarm`（同家族缺口）。  
2. 新暗金集：新隐喻 + N≥1；禁 B1–B7。  
3. 可选：补 IsoScanner + 提高床 luma 后再跑 sample v6（**非本任务**）。
