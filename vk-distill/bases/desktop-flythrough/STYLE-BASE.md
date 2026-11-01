# Lemo「桌面穿梭 / desktop-flythrough」demo teardown (spec)

Source: `refs/lemo-demos/desktop-flythrough.mp4` (59.95 s, 1920×1080/30). Dense frames: 1 fps in `ref/frames/`, sheets in `ref/dense_0..4.jpg`.
Engine source: `lemo-opuscar/styles/desktop-flythrough/demo/src` (three.js r170). Everything below is measured from the frames or the source.

## 1. Visual style
- **Set**: one dotted paper mat (#E2E8F5 paper, #C4CDE3 dots every 0.03 u) on a light-oak desk (#DECCB2 planks). The desk appears at the frame edges in wide shots only. That edge is the depth cue: the mat has a thickness and a cast shadow.
- **Light**: one low warm sun from the back-left (about 20° elevation). Shadows are long, soft and blue-grey and fall toward the camera's right. There is a cool sky/hemisphere fill, warm additive "window light" patches on the paper, and exp fog (the haze matches the paper, so the far desk dissolves into light).
- **Materials**: cards are near-white (#FBFCFF) rounded slabs about 5–9 mm thick with a visible bevel and edge highlight. Print sits on top: a canvas at 3.4×, with fine grain. Voxel toys are bevelled cubes with plastic roughness .48. Thickness grows from the silhouette inward, and the eyes stand proud.
- **Colour economy**: paper/white + ink #171C2E + ONE accent cobalt #2F5BFF. Cobalt is used for route dots, pills, "now" items and the accent text. Red appears only for failure. Mustard and orange appear only on characters/props. Saturation is low everywhere else.
- **Depth**: a physical DOF background blur (the focus sits a little behind the subject). There's a slight vignette and a warm grade, and bloom only on emissive lamps.

## 2. Layout and typography
- **Subtitle**: a DOM bar centred at the bottom on a dark 72% box. The ZH line is bold, about 26 px in the demo, with a small EN line under it. The subject is framed 110 px above centre via a view offset, so the bar never covers the action.
- **In-world type hierarchy (on cards)**:
  - a mono caps tag with an accent square (`■ SHRINK`)
  - a CJK bold sub-head
  - a hairline rule
  - big CJK bold body (原图) plus big mono numerals (4.2 MB)
  - accent text for the "result" column (压缩后 / 300 KB)
- **Pills**: camera-facing cobalt capsules (`1 压小`, `2 服务器`, `3 通知`). They pop with a back-ease and sit above the station, top-right of the subject.
- **Tent card**: a standing folded title card (叮之前 / BEFORE THE DING) with an accent bar on the left. It opens and closes the film. The finale drops a big flat copy of it.
- **Plates**: name plates printed flat on the paper under each station. They show only in wide shots.

## 3. Animation logic (how things are born, grow and transform)
- **Sticker → toy "pop"**: pixel art lies flat on a card. It hinges up (back-ease) while the voxel columns extrude in a ripple from the centre, with a small hop and squash.
- **Hops**: characters travel by arcs, with squash on landing and stretch on take-off. Between moves they bounce on the beat (beatBounce).
- **Route of cobalt dots**: these are drawn dot by dot (≈0.1 s per 10 dots), so the journey is literally "derived" on screen. Later the same dots light up in a wave to recall the path.
- **Transformations, not cuts**:
  - The big cat is squashed by a press and debris cubes fly out. The small cat pops out of it.
  - The drawer slides out, the cat goes in, and a window lights.
  - The bell rises from the server and flies on a mustard trail.
- **Counters**: numerals tick down on the beat (4.2 MB → 300 KB).
- **Impacts**: each one has a thin cobalt ring on the paper, a dot ripple, a tiny camera shake and a sound event.
- **Life**: blinks every ~2 s, the antenna lamp blinks on beats, the server windows flicker on 8ths.

## 4. Transition rhythm vs beats
- It's one take with zero cuts. There are about 40 camera keys in 60 s, so the camera changes intent every 1–2 s and never sits still for more than ~3 s.
- Each VO sentence gets one "stop", and the action inside a stop lands on the words (cue times from the VO). Between stops there's a glide (0.6–1.5 s) that rides a moving subject (the camera follows the cat's leap). A **whip** (0.2–0.5 s) arcs UP over the desk, so stations pass through frame instead of bare paper.
- Pops, hops and badges land on beats (120 BPM in the demo, so .5 s per beat). Badge pops come about 0.4 s after the word.

## 5. Camera language
- **Reading shots**:
  - elevation 0.9–1.0 rad (52–57°), fov 34–36, distance 0.45–0.65 u for one card
  - top-down-ish, card upright (azimuth ≈ 0)
- **Hero/character shots**: elevation 0.4–0.55, close at 0.5 u, slight azimuth 0.3–0.6 (three-quarter), with half-orbits around 3D objects (the server).
- **Wides**: distance 2.3–2.6, elevation 1.0–1.05, showing all stations and the route. These are used for "the whole relay" moments and for the finale pull-back.
- **Moves**:
  - Hermite target paths that track live subjects
  - a breath of noise drift (0.6% of the distance)
  - banking into lateral moves
  - micro shakes on impacts
- **Finale**: a long rise and pull-back until every station is in frame. Everything hops once left to right, the characters bow, the title card drops, then the credit.

## Rules adopted for 《Chat和Agent差在哪一桌》 3D
1. Same engine, same light, mat, materials and post. The story, props and layouts are new: three stations on one desk.
2. The type is **bigger than Lemo's** (the brief requires large, high-contrast CN):
   - subtitle ZH 46 px bold, white on an 80% ink box
   - card body ≥ 34 canvas-px CJK bold in ink #171C2E
   - no mute-grey body text
   - accent text only ≥ 40 px bold on white
3. Every VO phrase group gets one stop. Every new element is born from the previous one (it pops from a sticker, is carried by the helper, runs along the dots, or flips off a card). There are no unmotivated appearances.
4. Beat grid: **112.35 BPM** (BEAT = .534 s, downbeat 0.4 s). Pops and landings snap to the nearest beat within 0.15 s of their word cue.
5. The camera re-keys every 1–3 s. Reading stops are at el 0.9–1.05. Station changes are whips that arc over the desk. The opening and finale are wides.

## Addendum (ep08 lost-in-middle, 2026-10-30)
- Data episodes: put honest 3D bars on the mat in front of the slot they measure (height ∝ value, axis from 0, k = 0.004 u per point), join the tops with a cobalt tube drawn progressively, and use red only for the "worse" / baseline items.
- Keep the answer/“now” object cobalt (not mustard), because qa_style's single-accent-hue gate counts saturated yellow as off-hue.
- Render: three.js + SwiftShader, `render_frames.mjs` (resumable jpg frames) with `?n=1&sm=2048` on the shared box (≈4 s/frame per worker under load).
