# Style base · game-show (节奏综艺)

Reference: lemo-opuscar/styles/game-show (game-show.mp4, "AI 进化节拍 1997→2026"), teardown from 149 frames at 1 fps (refs/game-show, sheets /tmp/gs_sheet0–4.jpg).

## Teardown (what the reference does)
- **Sets:** full-bleed single-hue grounds: yellow sunburst (title), orange diagonal stripes (chess), blue stripes (quiz), lilac stripes (art), purple curtain (chat choir), red curtain (price war), navy sunburst (finale). Each new round = new hue; never repeats on neighbours.
- **Round card:** cream rounded card with ink outline + hard offset shadow, tilted −3°…+3°, pill tag "GAME n" on top edge, icon on the left, black CJK title, small year line. Pops on a bar line with a flash, holds ~1 bar.
- **Corner banner:** top-left, blue (or set-contrasting) rounded rectangle with ink outline + shadow, white bold year/name + small subtitle line.
- **Floor band:** darker same-hue band at y≈860–900 with an ink top line; characters/props stand on it (tables, podiums, lecterns).
- **Cast:** bean mascots (8px ink outline, oval eyes with catch-light, belly patch, one antenna accessory, name tag under). Crowds drop in one per beat; idle hop ripples.
- **Judgement words:** "Perfect!", "第37手!" — yellow/pink fill, thick ink stroke, ±8° tilt, pop with back-ease at centre-top.
- **Stats as game UI:** podium scoreboards with digits, price tags hammered, counters, a timeline ribbon of year chips at the top in the finale.
- **Question panel:** dark green board with white text centred top (quiz rounds), thought bubbles above podiums.
- **Ending:** navy sunburst, all cast lined up on the floor, report card typewriter, "Super!" stamp, credit card.
- **Camera:** frontal locked proscenium; only beat punches and hard cuts. No travel.
- **No subtitles** in the reference — the telops carry it. For our narrated series we add a bottom telop plate (ink pill, white Noto Sans SC 900) at y 928–1004, which is in the style's own telop language (STYLE.md §4).

## Our adaptation for Vibe知识大赏
- Tempo comes from the BGM grid (we-never, 112.36 BPM, downbeat 0.4 s); VO beats snap to downbeats (snap_vo), so each beat = one "round step"; chapter openers get a round card.
- Each chapter = one set hue: 1 sky (subway), 2 yellow (切分), 3 orange (鼓机大赛), 4 blue (倒U), 5 purple (补空拍), 6 green → navy finale.
- Every beat: 2–4 props popping on [[a]]/[[b]]/[[c]] cues (cues are on grid subdivisions after snapping).
- Contrast: subtitles white on #1B1B1B plate (≥15:1); footnote ink on cream chip (≥14:1); telops ink-stroked.
- Numbers only from facts.md (2014, 50, 34, 14, 2, 120, 66, 1–5). No % anywhere. Curves are labelled 示意.
