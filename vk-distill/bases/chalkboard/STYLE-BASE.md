# Base: chalkboard (黑板粉笔 · 纠错课)

Reference: Lemo `chalkboard` demo 《汉字的故事》 (refs/lemo-demos/chalkboard.mp4, 49.3 s; dense frames refs/chalk-dense/ at 1 fps, sheet1.jpg, hi_grid.jpg).
Engine: lemo-opuscar/styles/chalkboard/demo (MIT, LemoLab). chalk.js/hand.js/stage.js/post.js reused; per-episode film.js + app.js (multi-erase).

## Teardown
- World: one classroom wall. Wooden-framed green slate 6400x1700 (front panels FL|FR + back board BK behind FL), chalk tray with sticks, cream wall, window light from the left (warm patch low-left, cooler right), vignette.
- Palette: slate deep green (#1d2b24 to #24352c, never black); chalk white #ECEAE0 for structure and all text; ONE accent chalk orange #E8893A only for the tracked thing (circle, component, path); second-hand pale yellow #E6D58A for the student question; faint tan grid boxes.
- Type: subject chars 230-380u in grid boxes; labels 60-90u chalk; EMS single-line Latin 40-55u under labels; header 70u top-left, date top-right. Board = keywords only; explanation is in the voice.
- Animation: every glyph WRITTEN in stroke order with pressure and grain; bright grain front at the tip; nothing fades in. Wrong idea -> wipe band with damp haze -> rewrite in the same place. Accent circles a part, then a long path across the panel seam links two ideas. Underlines/ticks are drawn.
- Camera: always frontal. Close write (s 1.4-2.2) -> slow lateral dolly (2-4 s ease) -> medium pull-back (s~0.85) -> one wide classroom shot (s~0.55) with frame, tray, wall. Short whip (~0.35 s) when the panel slides. Motion blur only on moves.
- Rhythm: a new written element every 2-4 s, starting 0.1-0.3 s before the word it names; camera moves sit in VO gaps; holds <= 3 s.
- Subtitles: dark rounded plate (#0a0f0c @0.62) bottom-centre, WenKai 38 px, cream.

## Rules for Vibe知识大赏 episodes
1. Board text = keywords and numbers (<=12 chars/line); every number gets a chalk footnote (year + source) in that board area, cream 70%.
2. Orange = the tracked thing (here: the guess / wrong answer). Yellow = the viewer's myth/question.
3. Each VO sentence adds a written element or an erase/circle/underline; primary prop type changes every beat.
4. Must have: one write-wipe-rewrite in place (the reversal), one cross-panel accent path, one panel slide or wide reveal, one wide shot.
5. Contrast: chalk >= 9:1 on slate, orange >= 4.5:1, footnotes >= 3:1.
6. Forbidden: fade-in text, overlay cards (except subtitles), emoji, drop shadows, 3D rotation, a second accent hue.

## Known gaps vs reference
- Most stroke data is auto-derived from makemeahanzi medians (Arphic PL) with geometry-classified stroke types, not hand-authored.
- No child hand / wet streak moments; wipe haze kept.
