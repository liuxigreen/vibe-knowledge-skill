# Maintaining the library

**Repository owner only.** Film agents: go back to [`AGENTS.md`](AGENTS.md).

## Add a style

Work in `styles/<slug>/` (lowercase, digits, hyphens).

| File | Holds |
|---|---|
| `style.json` | slug, num, en, cn, category_*, line, line_cn, uses |
| `STYLE.md` | KEEP grammar (from distill STYLE-BASE) |
| `style.yaml` | machine form |
| `DEMO.md` | optional densest notes pointer — not a story to copy |
| `poster.jpg` | optional contact sheet |
| `notes/` | DISTILL-GAP, keyframes, source notes |

Then update [`styles/README.md`](styles/README.md) and the style list in [`AGENTS.md`](AGENTS.md).

## Gates before merge

- Nine-item distill complete
- Mode evidence two sentences
- Knowledge-anchor (出处/示意/易杠)
- BANNED twin list non-empty when a reference exists
- Award docs still the only scorecard

## Do not

- Strip story KEEP into a chalkboard-only copy of another toolbox
- Commit huge densest mp4s by default (keyframes / contact sheet preferred)
- Commit tokens, `.env`, or private episode renders
