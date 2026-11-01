# STYLE-BASE · yingxian-tenon（应县木塔榫卯 / 斗栱）

**Mode (locked):** `silent_text_first` — zero VO; we-never continuous; mute-readable Chinese + short English.  
**Family:** warm timber craft-showcase 3D (not dark-gold CAD overlay double-draw; not elevator-shaft cement).  
**Source craft lock:** https://yingxian.huaye.art/cn/topics/structure + locked scholarly facts below.  
**Do not invent** extra academic citations.

## Argument
一座辽代木塔如何按真结构逻辑「长」出来：台基 → **内外双筒柱网** → **梁枋榫卯** → **斗栱铺作**（栌斗→栱→散斗→枋）→ 斜撑暗层刚性环示意 → 屋檐出挑 → 逐层叠。

## Facts baked into craft (must appear in densest 10s or be marked out-of-scope)
| Fact | On-screen |
|------|-----------|
| 外观五层六檐；内部 5 明层 + 4 暗层 = **9 结构层** | DayProgressHUD / MingAnLayerHint / end ghost |
| **内外双筒**（内槽柱 + 外槽柱），非单圈柱 | DualCylinderGrid |
| **榫卯 ≠ 斗栱**：榫卯=接合方式；斗栱=斗+栱+昂叠置铺作 | TenonJoin macro then DougongSet; subtitle contrast |
| 柱按层短粗，上层柱脚搭接下层柱头（非通高一木） | short storey shafts + ghost upper |
| 54 种斗栱 — 样片只清晰展示 **一组转角/柱头铺作** 再 Instanced 绕八角 | DougongSet |
| 刚柔相间：明层空旷可登，暗层斜撑成环 | MingAnLayerHint |

## Build order (screen chronology)
台基 → 立柱(外槽→内槽) → 梁枋榫卯搭接 → 斗栱铺作(栌斗→栱→散斗→枋) → 暗层斜撑示意 → 屋檐出挑 → 上层虚影

## Visual grammar (award-v2 — festival short bar)
- **Cinematography:** slow push + gentle orbit; shallow DOF / tilt-shift default ON; strong vignette; hero lighting (warm key from low side, cool rim, soft bounce); optional volumetric haze; never flat studio.
- **Materials:** high-quality wood grain (albedo+roughness+normal+AO), darker museum timber (avoid plastic toy wood), stone micro-relief, soft AO in joints, contact shadows under dougong.
- **Joinery hero:** macro of 榫头→卯口 tactile — bevels, fiber direction, dust on seat, golden-hour rim on tenon edge.
- **Dougong:** each piece (栌斗/栱/散斗/枋) readable silhouette & thickness; layered grow + slight settle bounce; densest window = museum CGI short, not CAD demo.
- **Composition:** rule of thirds; negative space for mute Chinese titles; titles as designed UI ink (large, high contrast), never cluttered HUD.
- **Grade:** warm amber midtones, deep but not crushed blacks, filmic contrast; bloom restrained on wood highlights only.
- One authoritative contour — CAD elevation fades before solid timber owns silhouette.
- Octagonal podium (not square toy box). Accent `#FF6A3A` only for chapter chip / keyword / hot counters.
- **Silent type (hard):** bottom narrative / mute script = white–near-white (`#FFF`–`#F5F0E8`), bold/semibold, large (≥48–52px ZH); role colors separated (title cream, accent `#FF6A3A`, step white); phone arm-length readable — no dim gold-on-brown.


## Props (implemented)
1. **DualCylinderGrid** — 外槽 8 + 内槽 8 short columns on octagon rings.
2. **TenonJoin** — 榫头滑入卯口 macro (beam↔column), brief accent glow optional.
3. **DougongSet** — ordered grow 栌斗→华栱/泥道栱→散斗→枋; corner set readable then instanced.
4. **MingAnLayerHint** — 明层空旷 vs 暗层斜撑 ring (schematic).
5. **DayProgressHUD** — chapters / days / bilingual sub / counters (外柱·内柱·榫卯·铺作件).

## Camera densest window (~3–7.5s)
Push into **TenonJoin** → soft orbit / crane on **DougongSet** stack. Soft pull for eaves + ghost upper.

## Audio
`we never` continuous · no under_voice / duck.

## Out of 10s sample scope
Full five exterior storeys, six eaves, iron finial, 54 dougong variants, exact survey dimensions, metal fasteners debate — see DISTILL-GAP.md.
