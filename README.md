# Vibe知识大赏 · vibe-knowledge-skill

**A code-driven toolbox for Douyin knowledge films**: distilled style bases, Award gates, and story-scene KEEP grammar.  
The **folder shape** follows a familiar style-library layout (`AGENTS.md`, `styles/<slug>/`, `plugin/skills/`). The **craft is ours** — nine-item distill, G0–G7, story KEEP — not a copy of another studio's look library.

Repo: https://github.com/liuxigreen/vibe-knowledge-skill

## Use

### Skill install (recommended)

Copy into your agent's managed-skills / workflows:

- [`plugin/skills/vibe-knowledge-film/`](plugin/skills/vibe-knowledge-film/)
- [`plugin/skills/vibe-topic-pipeline/`](plugin/skills/vibe-topic-pipeline/)

Then read [`AGENTS.md`](AGENTS.md).

### Clone

```sh
git clone --recurse-submodules https://github.com/liuxigreen/vibe-knowledge-skill.git
cd vibe-knowledge-skill
# If already cloned without submodules:
# git submodule update --init --recursive
```

Treat the repo root as `$LIB`.

## Layout

| Path | Role |
|---|---|
| `AGENTS.md` | Agent entry |
| `DIRECTOR.md` | Directing bible (lanes / densest / Award / story KEEP) |
| `TECHNIQUE.md` | norun, fonts, BGM, PC deliver, tools |
| `styles/` | One slug per base: `STYLE.md` + `style.yaml` + optional poster/notes |
| `docs/` | Award scorecard, DISTILL-MULTIDIM, STORY-SCENE-CRAFT… |
| `assets/` | fonts + `we-never` BGM |
| `tools/` | Award scripts |
| `plugin/skills/` | Installable skills |
| `core/` | Render-convention stub |
| `vendor/lemo-opuscar/` | **Upstream Lemomo (lemo-opuscar) submodule** — reference or film directly from their STYLE.md / demo code |

## Lemomo / lemo-opuscar

- Our `styles/` = **Vibe知识大赏** distilled bases (Award / story KEEP).
- `vendor/lemo-opuscar/` = upstream [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) (MIT), pinned commit via submodule.
- You may **reference or shoot with their templates** (chalkboard, memphis-diorama, desktop-flythrough, …). Pick explicitly: our distill/Award lane vs their STYLE.md+demo.
- **Do not claim Lemomo demos as ours**; keep their LICENSE attribution.
- Overlapping slugs: [`styles/_LEMO-BRIDGE.md`](styles/_LEMO-BRIDGE.md).


## Styles

Index: [`styles/README.md`](styles/README.md). Story-lane anchor: `styles/moyou-story-percolation/`.

## Check

```bash
python3 tools/award_score_check.py "L4 M4 C4 N5 T5 X4 H4 D5 G4 K4 F4"
```

Rules: `docs/AWARD-SCORECARD.md`.

## 中文

[README.zh-CN.md](README.zh-CN.md)
