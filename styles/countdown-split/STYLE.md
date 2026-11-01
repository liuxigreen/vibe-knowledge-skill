# STYLE-BASE · countdown-split（倒计时分屏）

Gate teardown of `/workspace/lemo-opuscar/styles/countdown` — STYLE.md, DEMO.md, demo stills, plus 1 fps frames in
`gate_refs/countdown/` (quad.jpg = f012 / f028 / f033 / f041). Made for ep07 *planning-fallacy*. Machine-readable
twin: `style-base.yaml`.

## 1 · 视觉风格 Visual style
- Broadcast **multi-camera wall**: hard rectangles on near-black ground `#06080A`, panels `#0E1318`, 1 px border
  (`#2C343B`, = ref rgba(222,232,238,.16)). **No rounded corners, no shadows, no glow** on cells.
- One pointing hue **orange `#FF5B1F`** (synced dot, active segment, T−, new-cell flash). **Red `#FF3B30`** only for the
  "actual / overrun / speaking" state. Text `#F2F5F7`, secondary `#8C979D`.
- Ref is footage-driven; we have no footage → every cell is a **drawn feed**: desk + laptop building slides, the cited
  paper as a light document (`#E8E4DA`, dark ink), a 37-dot cohort, timeline axis, bar rows. Feeds stay lit and busy
  (high contrast; never a dark, sparse frame — deliberate deviation from the ref's dim footage).

## 2 · 排版体系 Layout system
- 24 px margin, 8 px gutters. Top area `[24,24,1872,820]` holds 1 / 2 / 3 / 4 / 6 cells (presets full, L2/R2, BL+RT+RB,
  q1–q4, s1–s6, T/B bands). Bottom row is fixed: **clock cell** `[24,852,616,204]` + **transcript box**
  `[648,852,1248,204]`.
- Each cell carries a **camera chip** top-left: square dot (orange = synced) · mono code `CAM 4` · CN name · EN name.
- Clock: condensed fixed-slot digits (Barlow Condensed 700, 132 px) `T−1:59`, grey tenths, a 10-segment sub-second bar.
- Transcript box (ref: EN word-by-word + CN line) = our subtitle: speaking light + `旁白 VO` + current CN line, footnote
  line at the bottom of the box. Subtitles never float over the picture.

## 3 · 动画逻辑 Animation logic
- **The layout is the edit**: cells keep their `id` across beats and re-layout with easeInOutCubic 0.34 s; a new cell
  opens from its left edge with a 3 px orange flash; a leaving cell collapses to its left edge.
- **Cell count rises toward zero**: 2–3 cells (hook) → 4 → 6 (反直觉 chapter) → **zero beat B13: all cells merge into
  one full card and the clock inverts** (orange block, dark digits, `T+`). After zero: 2–3 cells, final single card.
- The clock always runs (accelerated, labelled 示意): T−2:00 at t=0 hits 0:00 exactly at the zero beat, then counts
  T+ overtime. Tenths + sub-second bar keep every frame moving.
- Numbers: readouts appear **only when settled** (pop + flash), never rolling; the single exception is the `Counter`
  type (days), whose OCR window is declared to QA.

## 4 · 转场节奏 Transition rhythm
- Beat cuts are snapped to the BGM grid (chapter openers on downbeats: B03 B06 B10 B14 B20 B27); prop cues snap ±0.3 s.
- No crossfades between beats: persistent cells morph, others open/close. Ref native moves used: control strip
  segments, planned-vs-heard checklist, event flag (orange bar, black type), dashed standby cells, sync badge.

## 5 · 镜头语言 Camera language
- Locked-off "cameras"; motion lives *inside* feeds (cursor, typing, dots lighting, playheads) and in the relayout.
- Re-framing = a cell growing (push-in) rather than a camera move; the zero merge is the one big "cut to wide".

## Forbidden
Rounded/shadowed cards · centered floating titles over empty bg · second pointing hue · rolling intermediate numbers
(non-Counter) · emoji · same primary prop two beats running · dark sparse frames.
