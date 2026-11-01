# DIFF · zhanwai-darkgold-huashu → reuse xiaomo-darkgold-disarm

## Verdict

**Do not ship a second `style-base.yaml`.** Craft is the same as
`/workspace/vk-distill/bases/xiaomo-darkgold-disarm/`.

## Evidence

| Check | Result |
|---|---|
| Source bytes | `md5(vk-huashu/ref/source.mp4) == md5(vk-emotion-shelf/ref/source.mp4)` = `2624958785b1402165b63d4c62fee9c9` |
| On-screen title | Both 《六层卸防》 / `SIX LAYERS OF DISARMING` |
| Six layers | 弱点献祭 → 切口降维 → 影子投射 → 回音留白 → 视线解绑 → 错位激将 |
| HUD / props | LayerMeter · ChatStack · WrongRight · SilenceTimer · ArcMeter · HoleCards · DualVoteCTA |
| Structure | 生活钩子 → 片名 → 六层机制 → 升华 → YOUR CALL |
| Duration / canvas | 180.33s · 1920×1080 · 30fps |

## Attribution correction

| Field | emotion-shelf prior label | huashu (authoritative caption) |
|---|---|---|
| Creator | 设计一切的小墨（user short-link guess; page stuck loading） | **站在外面** |
| Douyin series | 「情绪的保质期」（mislabeled short-link） | **话术博弈｜如何优雅的社交** 第1集 |
| On-screen title | 六层卸防 ✅ | 六层卸防 ✅ |
| Pipeline `base` id | `xiaomo-darkgold-disarm`（keep for stability） | same — episodes set `base: xiaomo-darkgold-disarm` |

`xiaomo-darkgold-disarm` id stays: already referenced by `episodes/emotion-shelf`. Lineage note in that YAML already says folder/user label may be wrong; this DIFF + `episodes/huashu` document the correct creator.

## Thin deltas (topic copy only — not a new base)

- Collection marketing title: 《话术博弈》 vs screen 《六层卸防》
- Caption has full 6-layer blurb + Chris Voss / FBI Elicitation footnotes in text (not always on-screen)
- Engagement dump present under huashu caption only

## Remix rule

New 社交卸防 / 话术多层课 → `base: xiaomo-darkgold-disarm`.  
Music×brain → `moyou-darkgold-music`.  
Do not fork `zhanwai-darkgold-huashu` YAML unless a future clip diverges in palette/prop grammar.

## Pointers

- Human distill: `/workspace/vk-huashu/STYLE-BASE.md`
- Timed beats: `/workspace/vk-huashu/beats.yaml`
- Shared machine base: `/workspace/vk-distill/bases/xiaomo-darkgold-disarm/style-base.yaml`
- Twin prior stub: `/workspace/vk-distill/episodes/emotion-shelf/`

## Silent mode (2026-10-31)

Same craft file is now **`mode: silent_text_first`** on
`/workspace/vk-distill/bases/xiaomo-darkgold-disarm/` (v3).
Bottom on-screen lines = designed narrative UI, not VO captions.
Do not add a VO fork under `zhanwai-darkgold-huashu/`.
See `xiaomo-darkgold-disarm/DISTILL-GAP.md`.
