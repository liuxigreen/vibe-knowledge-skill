# transit-map — style base (Vibe知识大赏)

Engine: the real Lemo `styles/transit-map` engine (lemo-opuscar, MIT, © 2026 LemoLab): WebGL tilted
paper sheet with depth-of-field, octilinear lines, pen-tip growth, interchange capsules, dashed tunnels.
Episodes reuse `film.js` + `gl.js` verbatim and write their own `net.js` (geography) + `timeline.js`
(phases, camera, overlays) driven by `build/compiled.json` + `timings.json` cue times.

## Reference teardown (refs/lemo-demos/transit-map.mp4, 47 s, 2 fps dense sheet:
`refs/lemo-demos/frames/transit-map/dense/dense_sheet.jpg`)
| t | shot | grammar to keep |
|---|------|-----------------|
| 0–1.4 | tunnel, headlights, flare cut | cold open is already moving |
| 1.5–6 | pen tip draws first red section stop by stop; close tilted cam, DOF; dark odometer plate top-left | **growth = the narration**; numbers live on a plate, drum digits |
| 6–12 | pull back, ride line-2 tip, interchange slam, dashed dive under river | each new element is born from the previous line (tip → station → capsule) |
| 12–20 | network burst, zoom out | scale reveal once, mid-film |
| 20–31 | glide to flat time-line panel: horizontal lines on a year axis, bracket + stamp ellipse | comparison is drawn *as lines on the same sheet*, not a cut to a chart |
| 31–36 | low tilted sweep, foreground station sign | parallax hero shot |
| 36–41 | veil + "你在这里" marker + caption | the action step = a marker on the map |
| 41.5–47 | end card on the paper | |
Camera moves every 3–5 s; nothing is ever still; one red accent points, everything else ink/grey.

## Series rules on top
- Paper stays light (#F2EEE5); subtitles on a paper chip (ink, ≥4.5:1); footnote chip at y>1015.
- Odometer plate only ever **lands** on numbers from facts.md (Counter props = QA windows).
- Every VO sentence = one shot in beats.yaml `shot:`; the next shot starts from the element the last
  one left (tip position, last station, panel line).
- Saturated colour budget: red only; myth/secondary lines dark navy #1C2856 or grey #8A857B.
