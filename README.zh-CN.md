# Vibe知识大赏 · vibe-knowledge-skill

**用代码做抖音知识片的风格工具箱**：蒸馏底座 + Award 门禁 + 人物故事型 KEEP。  
布局对齐常见「风格库」用法（`AGENTS.md` / `styles/<slug>/` / `plugin/skills/`），**内容是我们自己的大赏工艺**，不是照搬其他风格片库。

仓库：https://github.com/liuxigreen/vibe-knowledge-skill

## 怎么用

### 方式一：装 skill（推荐）

把下列目录拷进 Agent 的 managed-skills / workflows：

- [`plugin/skills/vibe-knowledge-film/`](plugin/skills/vibe-knowledge-film/)
- [`plugin/skills/vibe-topic-pipeline/`](plugin/skills/vibe-topic-pipeline/)

然后读 [`AGENTS.md`](AGENTS.md)。

### 方式二：clone

```sh
git clone --recurse-submodules https://github.com/liuxigreen/vibe-knowledge-skill.git
cd vibe-knowledge-skill
# 若已 clone 过但没拉子模块：
# git submodule update --init --recursive
```

把仓库根当作 `$LIB`。

## 目录

| 路径 | 用途 |
|---|---|
| `AGENTS.md` | Agent 入口 |
| `DIRECTOR.md` | 导演圣经（车道 / densest / Award / 故事 KEEP） |
| `TECHNIQUE.md` | norun、字体、BGM、PC 交付、工具 |
| `styles/` | 每个底座一个 slug：`STYLE.md` + `style.yaml` + 可选 poster/notes |
| `docs/` | AWARD、DISTILL-MULTIDIM、STORY-SCENE-CRAFT… |
| `assets/fonts` · `assets/bgm` | 字体 + we-never |
| `tools/` | Award 校验等 |
| `plugin/skills/` | 可安装 skill |
| `core/` | 渲染约定 stub |
| `vendor/lemo-opuscar/` | **上游 Lemomo（lemo-opuscar）子模块**：可参考或直接用他们的 STYLE.md / demo 代码（黑板课、孟菲斯、桌面穿梭等） |

## 与 Lemomo / lemo-opuscar

- 本库 `styles/` = **Vibe知识大赏** 蒸馏底座（Award / 人物故事 KEEP）。
- `vendor/lemo-opuscar/` = 上游 [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) 工具箱（MIT），钉死提交见 `.gitmodules` + `git submodule status`。
- **可以参考，也可以直接按他们的模版拍**（chalkboard、memphis-diorama、desktop-flythrough…）——拍前明确选「我们的 distill 车道」还是「lemo 原版 STYLE.md+demo」。
- **勿把 Lemomo demo / 成片说成我们的作品**；保留其 LICENSE 署名。
- 同名 slug 对照：[`styles/_LEMO-BRIDGE.md`](styles/_LEMO-BRIDGE.md)。


## 风格索引

见 [`styles/README.md`](styles/README.md)。人物故事型锚：`styles/moyou-story-percolation/`。

## 校验

```bash
python3 tools/award_score_check.py "L4 M4 C4 N5 T5 X4 H4 D5 G4 K4 F4"
```

Pass 规则：`docs/AWARD-SCORECARD.md`（G0–G7；故事另过戏感）。

## 英文

[README.md](README.md)
