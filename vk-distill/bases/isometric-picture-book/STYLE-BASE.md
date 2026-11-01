# Isometric Picture Book (real 3D) — Vibe知识大赏 base

Teardown source: Lemo `isometric-picture-book` demo "Seventy-Two Seats" (refs/lemo-demos/isometric-picture-book.mp4, 59.8 s; 1 fps frames in refs/iso-book/, sheet refs/iso-book/sheet.jpg, full frames full_13.jpg, full_30.jpg).

## 1. What the reference does (teardown)
- **Look:** one real place drawn full bleed (an aircraft cabin cut open + its gate). Flat warm paper ground (#EDE5D6-ish), solids in three flat tones (top light, left face base, right face dark umber), **no outlines, no shadows, no gradients, no textures**. Subject hue: deep green seats (#2F6B57 / #3D6B59); accent persimmon (#D0573A) used only for the rule word / the active marker; marking ginger (#E2AE3A) for the floor line.
- **People:** slim faceless figures from behind, ~1.7 m, round dark head, four muted tops (ochre, fog blue, grey violet, oat), dark trousers. They move only when the rule says so. Crowds read as a four-colour weave.
- **Type:** big serif Chinese (Noto Serif SC 700) lying on the floor, reading along the up-right axis; one accent character per phrase in persimmon; secondary small serif word beside it in grey. Characters land one by one ~0.14 s apart (ghost → ink, scale 1.22 → 1).
- **Layout:** ~60 % of every frame is calm empty ground; the floor phrase sits on clear ground beside the action, never under people; subtitle on a pale paper bar centred low (zh 30 px over en 22 px).
- **Animation logic:** cabin roof lifts off like a paper flap; people step in order; seat rows light up in order (order lighting); a black arrow grows ahead of the walkers.
- **Rhythm:** a new mark/word every ~2–3 s, a shot change every ~5–8 s; cuts are continuous moves (drift, push, rise to wide), never wipes or black frames; the final verdict frames are locked.
- **Camera:** fixed iso angle (az 45°, el ~30°), long lens, slow drift/push 6–8 %, rise to wide for reveals; follows the head of the line.

## 2. Our rules (reproducible)
1. **Real 3D:** three.js scene rendered in headless Chrome (SwiftShader). Perspective camera with a long lens (fov 14–22°) at azimuth 45° ± 8°, elevation 28–40°, so it reads iso but has true parallax when it travels. Camera moves are translation + zoom + small azimuth swings (≤ 8°), all eased; travel along the ground between zones = "穿梭".
2. **One continuous floor** for the whole episode: zones are laid out along the up-right axis (phone plaza → jam aisle → scale field → lanes) and the camera travels between them; no separate boards.
3. **Solids:** MeshBasicMaterial, per-face colours from `tri(c)` = [top lifted to paper, +z face base, +x face dropped to umber]. No lights, no shadows, no outlines.
4. **Palette:** paper #F1E8D8 (ground), concrete #E9E0CF, ink #2A2E29, accent persimmon #D0573A (rule only), subject green #3D6B59 / #A7C2B2, marking ginger #E2AE3A, tops ochre #C98A4B, fog blue #7F9DB8, grey violet #8E86A6, oat #D9C7A3; jam reds/purples are muted (#9E3B3B, #6E4A6B, #C47A3A) so they never compete with the accent.
5. **Floor type:** Noto Serif SC 700 ink #2A2E29 on paper ground (contrast ≥ 10:1); accent characters persimmon (≥ 3.5:1 on paper, used only at ≥ 1 m glyph height); one phrase per beat; landing 0.14 s per character. Numbers on the floor always have a footnote.
6. **Subtitles:** zh only, 40 px Noto Serif SC 700, ink on a paper plate rgba(251,247,238,.94) centred, plate top ≥ 940 px. **Footnote:** bottom-left 20 px ink on paper plate, baseline 1066 (box top > 1015).
7. **Tag:** top-left "Vibe知识大赏 · 章节名" ink on paper plate.
8. **Motion density:** something new every 2–4 s (a jar lands, a figure steps, a scale tips, a gate rises); no static stretch > 3 s; people walk ≤ 1.6 m/s, legs scissor.
9. **Transitions:** continuous camera travel along the ground, lid-off reveals, or a cut on the beat at the same angle. Never black/blank/wipe.
10. **Forbidden:** drop shadows, gradients, glow, outlines, neon, emoji, flat cards facing the lens, second accent hue, a dark background.
