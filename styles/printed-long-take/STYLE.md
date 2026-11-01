# Lemo「印刷长镜头 / printed-long-take」teardown (spec)

Source frames: `gate_refs/printed-long-take/f001–f060` (1 fps), contact sheet `sheet_01.jpg`. Engine kit: `lemo-opuscar/styles/printed-long-take/demo/src` (three.js; look.js / textures.js).

## 1. Visual style
- **Look**: a woodcut / scratchboard print. There are two inks only: near-black #16171B and warm paper #EDE5CD. Every surface is carved with knife lines (hatching that follows the form), not shaded with gradients. Sky = black with long horizontal carved streaks (star trails); ground = paper snow with carved furrows.
- **Spot colour**: one warm yellow/ochre #DFA443 (sunset glow, lamp light, highlighted figures) plus a print red #C4332B for the single "key" item (a chapter number, the one wrong/right option). Both are used on <10% of pixels.
- **Scenery**: faceted white mountains in the back, black pine/tree billboards, reeds and fence posts in the foreground, a road or river leading to the vanishing point. Foreground silhouettes pass close to the lens for depth.
- **Print pass**: paper fibre, slight 12 Hz ink flicker, vignette, no bloom, no DOF.

## 2. Layout and typography
- **Info boards**: black roadside signboards on two posts, a double paper border, a serif title row, then big serif numerals (33 / 1,927) with small unit labels. Boards always stand at the roadside facing the road, read at about 3/4 of the frame width.
- **Sky type plates**: big serif paper type printed into the black sky for the title (三十三只 / sub-title EN small caps), used for the open and close.
- **Subtitle**: a centered grey/ink translucent band low in frame, serif paper text. The series tag sits top-left.
- **Type**: one serif family (Noto Serif SC 700–900) throughout; numerals use the same serif.

## 3. Animation logic
- Board content is printed in left→right on cue (cut-paper reveal), and numbers count up in place (33 → 1,9 → 1,927).
- Flocks and figures are carved sprites that move along the ground plane; the world never cuts.
- Ink flicker and slow drifting sky streaks keep every shot alive.

## 4. Transition rhythm
- One continuous take with zero cuts. The camera travels along the road (or river) and stops at each board. Each stop = one VO idea, about 6–12 s; the glides between stops take 1.5–3 s.
- Chapter changes go through a physical gate/arch or over a ridge, never a wipe.

## 5. Camera language
- Eye height about 3 u, slight downward look, fov ≈ 34. Holds frame the board at 60–75% width, with a slow push-in (about 15% of the distance) during the hold.
- Openers and finales tilt up to the sky plate, then sink to the road (or the reverse at the end).
- There's a subtle handheld drift (sub-0.1 u) and no rolls.

## 6. Reuse rules (enforced in qa_style)
- Palette as style-base.yaml: clusters within ΔE 6 of ink/paper/yellow/red or their blends. The accent hue (OpenCV) is 0–22, covering both red and ochre.
- No invented numbers. Every board has a footnote (author + year, or 示意).
- Subtitle band y 905–1005, footnote y > 1015 on the ink band, contrast ≥ 4.5.
