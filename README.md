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
git clone https://github.com/liuxigreen/vibe-knowledge-skill.git
cd vibe-knowledge-skill
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

## Styles

Index: [`styles/README.md`](styles/README.md). Story-lane anchor: `styles/moyou-story-percolation/`.

## Check

```bash
python3 tools/award_score_check.py "L4 M4 C4 N5 T5 X4 H4 D5 G4 K4 F4"
```

Rules: `docs/AWARD-SCORECARD.md`.

## 中文

[README.zh-CN.md](README.zh-CN.md)
