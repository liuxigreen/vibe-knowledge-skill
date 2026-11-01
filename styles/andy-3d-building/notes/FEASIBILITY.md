# Feasibility · andy-3d-building → our three.js pipeline

Status: distilled only. **No sample rendered yet.**
Baseline: `/workspace/vk-bridge-pier/poc2` (`scene.js` 463 lines, `render-gpu.mjs`; PC RTX 3060 at about 380 ms/frame, so a 300-frame 10s clip takes about 2 min of GPU time; box SwiftShader is about 2.7 s/frame, so about 14 min).
Libraries: `/workspace/vk-bridge-pier/PUBLIC-LIBS.md`.

## Technique → our code / library map
| Technique in ref | What we already have (poc2) | Best library / approach | Effort |
|---|---|---|---|
| One-take camera with time-driven scrub `t∈[0,DUR]` | ✅ deterministic `t` per frame, `render-gpu.mjs` frame dump | — | 0 |
| HUD: chapter chip, 第N天, counters, bilingual subtitle | ✅ day HUD and subtitles exist (bridge style); restyle to chip + 3 corners | DOM overlay (ours) | S (1–2h) |
| Light DOF instead of heavy tilt-shift | ✅ `TiltShiftEffect` toggle `?tilt=0`; bloom, ACES, vignette | postprocessing (MIT, already vendored) | 0 |
| HDR env, soil and concrete textures | ✅ poly-haven HDR and 1k textures in `poc2/assets` | reuse | 0 |
| **Bricks laid one by one, counter == count** | ❌ | **Own code**: `InstancedMesh` per wall course, instances sorted by (floor, course, along-wall); `mesh.count = N(t)`; last few instances drop-in with ease (matrix y offset). 3-storey house ≈ 30–100k instances, fine on GPU | S–M (3–4h) |
| Walls from plan polylines (with door/window openings) | ❌ | Own `planToWalls(rooms)` generator: 2D segments → brick slots, skip openings | M (included above) |
| Slab / foundation "pour fill" | ✅ clip plane helper `clipped()` in poc2 | Reuse clip-plane technique (MengTo/towers style, **reimplement, no copy**) or scale-in | S |
| Scaffold that follows height | ❌ | Own generator (pipes = instanced cylinders, boards, green net planes) | S (1–2h) |
| Excavator, mixer truck, workers | ❌ (pier had piling rig only) | **fanhuayishiy/ai-demo `voxel-construction-site` (MIT, verified via GitHub API)** — single-file three.js r160 with code-built excavator/mixer/loader/crane/workers; extract mesh builders, keep LICENSE notice | S |
| CAD lines → ground layout (HUD-to-world) | partially (edge line materials) | `LineSegments` drawn in an ortho overlay camera, then lerp the camera/matrix into the world ground plane | M (2–3h) |
| Stack of drawing sheets fanning out | ❌ | Planes with canvas textures, staggered rotation | S |
| X-ray MEP (translucent shell + glowing pipes) | bloom ✅ | Swap materials to `MeshBasicMaterial` with transparency and `EdgesGeometry`; pipes = `TubeGeometry` with `drawRange` growing | S–M |
| Exploded storeys with room labels | ❌ | Group per floor, y-offset tween; CSS2D-style projected labels | S |
| Seasons: leaves, snow, fireworks, roof snow | ❌ | `Points` particles; roof snow = white cap mesh scaling in; fireworks = burst sprite system | M |
| Village backdrop | ❌ | Low-poly box houses and instanced trees (voxel-site has props too) | S |
| Real BIM / IFC (ThatOpen, BIM OOTB) | — | **Not needed**: the ref is clearly procedural low-poly, and IFC would add weight and an "engineering software" look | skip |
| three-tunnel | — | Irrelevant to this ref (keep it for tunnel topics) | skip |

## Recommended route
1. **Fork poc2's shell** (renderer, post stack with `?tilt=0` default, HDR, HUD layer, `render-gpu.mjs`) into `/workspace/vk-building/`.
2. **Write our own procedural house kit**: `planToWalls`, `InstancedMesh` ordered brick reveal with a counter, slab clip-fill, scaffold, hip roof. This is the core of the look, and no public library does it.
3. **Borrow machines and props from `voxel-construction-site` (MIT)**: excavator and mixer mesh builders, plus trees and workers.
4. Do the clip-plane grow ourselves (towers technique only, no code reuse) for pours and the facade render coat.
5. Leave IFC (ThatOpen) for a later "real building" topic.

## 10s sample proposal (when approved)
**Beat: "每一块砖，都按真实顺序砌上去"** (ref 19–30s equivalent): ground slab is ready, then floor-1 bricks rise with a macro dolly that pulls out to a 3/4 orbit, scaffold follows, and the day counter runs 第26天 → 第59天 with the brick counter 0 → ~30k. The HUD shows chip `03 主体 STRUCTURE`, the right corner, the bottom-left counters, and one subtitle.
- This proves the hardest and most signature piece (ordered instanced growth tied to a counter) and works on mute.
- Effort: **about 1 working day** (house kit 4h, scaffold 1.5h, HUD restyle 1.5h, camera/post 1h, QA 1h). Rendering is minutes on the PC GPU (300 frames × ~0.4s plus encode). The box can preview at 960×540.
- Option B (cheaper, ~half a day): opener "sketch → CAD → layout on ground" 10s, which is mostly 2D lines and planes.
- Full 60s episode: about 3–4 days, mostly seasons/particles and the exploded interiors.

## Risks
- 100k instances with shadows on SwiftShader will be slow, so render finals on the PC only.
- The ref uses strong DOF; the user prefers sharp, so keep DOF subtle.
- The PC is intermittently reachable, so keep box fallback renders at half resolution.
