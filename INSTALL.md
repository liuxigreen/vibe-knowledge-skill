# 安装说明（全量 ALL-IN-ONE · 2026-11-01）

目标：解压后即可安装并跑选题→蒸馏→densest→Award→全片。  
**本包已含字体与 we-never BGM，不需要旧的 Oct 31 zip。**

## 1. 解压

解压到例如 `D:\Vibe知识大赏-试做\vk\`、`C:\vk\` 或 `/workspace/`。  
根目录应有 `skills/` 与 `vk-distill/`。

## 2. 安装 skills

把下列文件夹写入 Agent 的 workflows / managed-skills（保持文件夹名）：

- `skills/vibe-knowledge-film/`
- `skills/vibe-topic-pipeline/`

## 3. 挂上 vk-distill

将包内 `vk-distill/` 放到约定根（默认 `/workspace/vk-distill`）。路径不同则改 skill 内路径或做符号链接。

文档权威：`vk-distill/docs/`（九项蒸馏 + STORY-SCENE-CRAFT + AWARD-SCORECARD）。

## 4. 字体 / BGM（已内置）

- `vk-distill/assets/fonts/` → 渲染脚本或 sample 的 `fonts/` 指向这里
- `vk-distill/assets/bgm/we-never.mp3` → silent 全片默认曲

## 5. 校验

```bash
python3 vk-distill/tools/award_score_check.py "L4 M4 C4 N5 T5 X4 H4 D5 G4 K4 F4"
```

Pass 规则见 `docs/AWARD-SCORECARD.md`（≥44；N/X/D≥4；L/M/F≥4；story 另过戏感 / G7）。

## 6. 给目标 AI 的指令（可整段粘贴）

解压 `vibe-knowledge-full-install.zip`（2026-11-01 全量）。安装 `vibe-knowledge-film` 与 `vibe-topic-pipeline`。管线根为包内 `vk-distill/`（含 assets/fonts 与 we-never）。打分只用 `docs/AWARD-SCORECARD.md`。蒸馏按 `DISTILL-MULTIDIM.md` + `STORY-SCENE-CRAFT.md` 先锁 story_scene / diagram_bed / hybrid。人物故事型锚 `bases/moyou-story-percolation/`（语法可学，道具必须 SWAP，禁抄 twin 签名）。densest→评分→near-pass 先抬 L/M/F→再全片。

## 7. 相对旧包

- 现行 skill + STORY-SCENE-CRAFT + moyou-story-percolation + Award 打磨文档
- **并入** Oct 31 同款 fonts + we-never；不必再找旧 zip
- 仍不打包各集 densest 大 mp4 / QA 静帧（体积控制；规则与底座文本已够另一 AI 开工）
