# Vibe知识大赏: instructions for agents

This repository is a **library of knowledge-film styles** for the Vibe知识大赏 series (Douyin vertical, usually silent-text-first, code-driven). Each style has `styles/<slug>/STYLE.md` (KEEP grammar) plus machine form `style.yaml`. People pick a style and ask for a film about **their own** topic. Your job is to direct and produce that film under Award gates — not to clone a twin reference.

| The request | Go to |
|---|---|
| Any request / no topic yet | **Start** below |
| A film about the user's topic | **Style and story**, **Workflow** |
| "Which styles?" | **Finding the style** · [`styles/README.md`](styles/README.md) |
| Directing: lanes, densest, Award, story KEEP | [`DIRECTOR.md`](DIRECTOR.md) |
| Building: norun, fonts, BGM, PC deliver, tools | [`TECHNIQUE.md`](TECHNIQUE.md) |
| Tool / path conventions | [`core/README.md`](core/README.md) |
| User wants their own style folder | [`MY-STYLES.md`](MY-STYLES.md) |
| Adding a style to this library (owner) | [`MAINTAINING.md`](MAINTAINING.md) |
| Lemomo templates (reference / direct use) | [`vendor/lemo-opuscar/`](vendor/lemo-opuscar/) · [`styles/_LEMO-BRIDGE.md`](styles/_LEMO-BRIDGE.md) |

**Films outside `styles/` are the user's.** Do not watermark. Do not edit library styles while shooting an episode.

## Start

- Talk in the user's language (中文 default for this series).
- Before picking what to film, prefer skill `vibe-topic-pipeline` unless the topic is locked.
- Offer: (1) film in a library style; (2) distill a new reference into a base; (3) use a saved style under `~/vibe-my-styles/` when present.

## Style and story

- **`STYLE.md` is fixed**: KEEP / BANNED, mode evidence, type ladder, props, beat density, knowledge-anchor. Keep all of it.
- **Topic is yours to direct**: story, settings, gadgets (SWAP twin signatures), timings. Never bend the topic toward densest notes as a copy.
- Lock **`narrative_mode`**: `story_scene` / `diagram_bed` / `hybrid` per [`docs/STORY-SCENE-CRAFT.md`](docs/STORY-SCENE-CRAFT.md).
- Distill is **九项** ([`docs/DISTILL-MULTIDIM.md`](docs/DISTILL-MULTIDIM.md)), not palette-only.
- Never build inside `styles/`: copy KEEP into the episode folder.

## Finding the style

Look up English / Chinese / folder names in [`styles/README.md`](styles/README.md). Suggest 2–3 that fit the topic; list story-lane anchors first when the topic is interpersonal / plateau / bias.

<!-- style-list:start -->
Library styles (see styles/README.md for the table):

- **Story & Scene · 人物故事**: moyou-story-percolation, xiaomo-darkgold-disarm, nexo-crowd-phone, sanhao-halo-effect, bite-red-queen, zhongshan-learn-fast
- **History Paper · 历史纸偶**: lailong-xuanzang-passport, lailong-zhaoyun-infant
- **Silent Diagram · 静音图解**: moyou-darkgold-music, dianzi-info-surprisal, yingxian-tenon, andy-3d-building, andy-3d-construction-sim
- **Craft Grammar · 工艺语法**: chalkboard, circuit-board, circuit-board-pcb, countdown-split, desktop-flythrough, game-show, isometric-picture-book, memphis-diorama, printed-long-take, transit-map
- **Notes · 备注**: zhanwai-darkgold-huashu (alias DIFF → xiaomo-darkgold-disarm)
<!-- style-list:end -->

## Lemomo upstream (`vendor/lemo-opuscar`)

Pinned **git submodule**: [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) (MIT / LemoLab). Init with `git submodule update --init --recursive` if the folder is empty.

| Lane | Path | Use when |
|---|---|---|
| **Ours** | `styles/<slug>/` | Vibe知识大赏 distill + Award / story KEEP |
| **Lemomo** | `vendor/lemo-opuscar/styles/<slug>/` (+ their `DIRECTOR.md` / `TECHNIQUE.md` / `plugin/`) | User wants that **look** as Lemomo ships it — reference **or** film from their STYLE.md + demo code |

- Offer Lemomo when the brief fits chalkboard / memphis-diorama / desktop-flythrough / etc., or when the user asks for "lemo / lemomo 模版".
- **Same slug, two folders**: ours = distill/Award lane; lemo = upstream STYLE.md+demo. Ask which; never mix silently. Bridge table: [`styles/_LEMO-BRIDGE.md`](styles/_LEMO-BRIDGE.md).
- Attribution: keep Lemomo LICENSE; **do not claim their demos or films as Vibe作品**.

## Workflow

1. **Brief** — topic, narrative_mode, length (full cuts often 5–15 min dense; densest 10s first), language, any must-have facts. Ask once.
2. **Treatment** — argument path + conflict→turn table (story/hybrid) before densest polish.
3. **Densest 10s** — type ladder table + 3s motion list (+ conflict table for story). Ship frames / contact sheet.
4. **Pre-score Gate G0–G7** + Award /55 ([`docs/AWARD-SCORECARD.md`](docs/AWARD-SCORECARD.md)). HUMAN-CHECK (+ 戏感三问 for story).
5. **Iterate** near-pass → raise L/M/F before claiming Pass.
6. **Full cut** — dense edit; silent default BGM `assets/bgm/we-never.mp3`.
7. **Deliver** to PC `D:\Vibe知识大赏-试做\<episode>\` Chinese three-pack when that is the user's machine.

## Where things go

- Library root = `$LIB` (this repo).
- Episode folder = `D:\Vibe知识大赏-试做\<name>\` on the owner's PC, or `<name>/` beside `$LIB` in skill mode.
- Run `python3 tools/…` from `$LIB`.
- Skills: `plugin/skills/vibe-knowledge-film/`, `plugin/skills/vibe-topic-pipeline/`.
