# Technique: how Vibe知识大赏 films are built

Code-driven pages and tools — **no stock explainer kits as the lecture**. Pair with [`DIRECTOR.md`](DIRECTOR.md) and one `styles/<slug>/STYLE.md`.

```
topic → narrative_mode lock → distill/KEEP
   → densest 10s (frames + tables)
   → G0–G7 + Award /55
   → full cut (dense edit)
   → mux BGM (silent) → deliver PC
```

## 1. Requirements

- Python 3.11+ for `tools/award_score_check.py` and QA helpers
- ffmpeg for mux
- Browser for HTML samples; use **`?norun`** so autoplay does not fight editing
- Fonts: `assets/fonts/` (NotoSansSC-VF, NotoSerifSC-VF, GeistMono-VF)
- Silent BGM: `assets/bgm/we-never.mp3`

## 2. Paths

| Role | Path |
|---|---|
| Library | `$LIB` = this repo root |
| Styles | `$LIB/styles/<slug>/` |
| Docs | `$LIB/docs/` |
| Tools | `$LIB/tools/` |
| PC deliver (owner) | `D:\Vibe知识大赏-试做\<episode>\` |

Never write episode renders into `styles/`.

## 3. Picture rules

- Deterministic frames preferred (`render(t)` mindset when using HTML/canvas).
- Vertical 1080×1920 unless STYLE locks otherwise.
- In-frame show wins: [`docs/INFRAME-SHOW.md`](docs/INFRAME-SHOW.md). Crop-bottom mute must still teach.
- Ban continuous bottom-white captions that echo on-canvas text.

## 4. Sound

- Silent-text-first: designed on-screen copy **is** the script; BGM bed only.
- If VO mode is proven in STYLE.md, duck music under voice; still keep in-frame argument.

## 5. Award tooling

```bash
cd "$LIB"
python3 tools/award_score_check.py "L4 M4 C4 N5 T5 X4 H4 D5 G4 K4 F4"
```

Pass rules: [`docs/AWARD-SCORECARD.md`](docs/AWARD-SCORECARD.md) (≥44; N/X/D≥4; L/M/F≥4; story also clears 戏感 / G7).

Other helpers: `tools/compare.py`, `tools/contrast_scan.py`, `tools/qa_partial.py`, `tools/rubric.py`.

## 6. Skill install

Copy or link:

- `plugin/skills/vibe-knowledge-film/`
- `plugin/skills/vibe-topic-pipeline/`

into the agent's managed-skills / workflows. Then follow [`AGENTS.md`](AGENTS.md).

## Lemomo submodule

Upstream toolbox lives at `vendor/lemo-opuscar/` (git submodule). Init: `git submodule update --init --recursive`. Overlap bridge: `styles/_LEMO-BRIDGE.md`.
