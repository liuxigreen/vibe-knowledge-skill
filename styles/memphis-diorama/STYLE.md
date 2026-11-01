# Memphis Diorama · reusable production spec (teardown of gate_refs/memphis-diorama, 46 frames + demo source)

## Visual style
- Pastel toy-town built from flat-shaded primitives (no lighting model): fixed face tones, hard deep-indigo (#25214A) shadows, world-space patterns (dots, stripes, zigzag, hatching).
- Every silhouette is inked: normal + depth discontinuity outline, ~2px at 1080p, rendered at SS=2 then downsampled.
- The world sits inside a grainy, spray-painted rounded frame (cx 960, cy 468, hw 760, hh 372, r 34) on warm paper #FFFCF6. The frame edge wobbles slowly (±22px).
- Palette: paper FFFCF6, ink 25214A, yellow FFD234, pink FF7EB3, sky 5CC8FF, mint 5EDFB0, lilac B9A0FF, peach FF9C6B, cobalt accent 2F5BFF, coral FF5A5F, grass 8FD98A, path F4E3C3. Only cobalt is a "meaning" colour; the rest are toy colours.

## Layout and type
- All type lives on the paper, never over the 3D: top strip (series tag + Memphis marks: yellow dot, pink triangle, cobalt squiggle) and bottom strip (line 1 strong 25px, line 2 muted, line 3 mono).
- Knowledge-video adaptation: subtitles 46px/700 ink on paper at y≈962 (band 920–1015) with a thin yellow underline; footnote 22px muted at y≈1046; chapter tag top-left.
- In-world information goes on standing white sign cards (Memphis confetti corners, ink 18px rim, pills with offset ink drop shadow). Card text ≥ 56px on a 2048 canvas, so ≥ 30px on screen.

## Animation logic
- Everything is a pure function of t (deterministic, frame-resumable).
- Things pop in with a back-out ease (overshoot 1.6–2.8), walkers loop a walk cycle, and details stagger 0.05–0.3 s.
- Nothing cuts. Change happens as growth (bars, tufts, crates dropping), never as a crossfade.

## Rhythm and camera
- One continuous long take at fov 30, high angle (ref ≈ 35–40° from overview distance; knowledge edit 23° from 21–29u so card text reads).
- Each beat is a station: wide reveal (card + prop) → ease-in push to the card within the first 35% of the beat → slow drift.
- Between beats there is a 1.15 s glide with a 7u lift arc, so the town reads as a map between stations.
- Footnote/tag swap on beat boundaries; the end lifts and pulls back to an overview.

## Reuse rules
- Keep ≤ 1 accent hue (cobalt). Group colours are toy colours with labels, never bare colour coding.
- Numbers appear only on cards, never as floating 3D text; 3D props show magnitude (bars, stacks, meters) without labels.
- Contrast: ink on white/yellow/pink/mint; white on cobalt; coral is only a pill background with ink text.
