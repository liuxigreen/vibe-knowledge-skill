# core/ · render conventions (stub)

This library is **Award-first knowledge-film craft**, not a full headless Chrome render suite yet.
Episode code usually lives on the machine under `D:\Vibe知识大赏-试做\<episode>/` (or `$LIB/../episodes/`).

Conventions agents must keep:

| Item | Rule |
|---|---|
| Canvas | Prefer **1080×1920** Douyin vertical unless STYLE.md locks another size |
| Preview | Use `?norun` on HTML samples so pages don't auto-play while editing |
| Silent BGM | Default bed: `assets/bgm/we-never.mp3` |
| Fonts | `assets/fonts/` — NotoSansSC-VF, NotoSerifSC-VF, GeistMono-VF |
| Award check | `python3 tools/award_score_check.py "L4 M4 C4 N5 T5 X4 H4 D5 G4 K4 F4"` |
| Deliver | PC Chinese three-pack under `D:\Vibe知识大赏-试做\` |

When render helpers land here later, they will follow deterministic `render(t)` style pages like other code-film toolboxes — without copying their styles.
