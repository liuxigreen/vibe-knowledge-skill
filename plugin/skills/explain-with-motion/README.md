# Explain with Motion

知识视频的参考研究、导演规划与代码动画制作 skill。重点是用画面解释关系和变化，同时保留空间、体量、材质、光影、镜头与文字的完整视觉规格。

当前包括22条案例文字证据、风格选型、导演方法、制作流程、提帧工具、时间检查器，以及可运行的Python逐帧渲染入口和水滴示意工程。它不是一键生成任意高完成度视频的模型；three.js/WebGL后端仅有接入说明，尚未在本项目集成。

## 使用skill

将本仓库目录作为一个skill目录，或让支持本地文件读取的AI先读 [SKILL.md](SKILL.md)。分析参考片时按需读证据，制作新选题时先写导演方案、选风格，再进入具体后端。不要把复制demo里的词语当作新作品。

## 本地运行

需要Python 3.11+和PATH中的ffmpeg。推荐在项目虚拟环境安装依赖：

```sh
python -m venv .venv
# 激活虚拟环境后：
python -m pip install -r requirements.txt
python scripts/check_project.py examples/water-journey/project.json
python scripts/render.py examples/water-journey --preview --font /path/to/CJK-font.ttf
python scripts/render.py examples/water-journey --start 6.8 --end 7.8 --font /path/to/CJK-font.ttf
python scripts/render.py examples/water-journey --font /path/to/CJK-font.ttf
```

Windows PowerShell将字体参数换成已有的本地中文字体，例如 `--font C:/Windows/Fonts/msyh.ttc`。不随仓库分发字体；需要足够的中文覆盖。示例构图固定1280×720、30fps、10秒、无音轨；输出在工程的 `out/`，被Git忽略。依赖固定为本次实跑版本，不等于所有系统组合都已验证；测试环境版本见 [VALIDATION.md](VALIDATION.md)。

## 目录

```text
SKILL.md               AI入口
references/            导演、风格、证据、制作、工具规范
scripts/               提帧、清单检查、逐帧渲染
examples/water-journey/ 专题示意工程与构建命令
requirements.txt       Python运行依赖
```

导演和技术受 [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) 的分层组织启发。我们静态核对了它的文档和部分工具接口，没有安装、执行或声称复现其所有风格，也不把它针对特定模型的调优视为跨模型质量保证。

公开版不含用户下载的视频、原片截图、音轨、私人目录或凭据。22条研究可通过ID与PTS查来源；本地研究图包若需要应由使用者另行提供。见 [参考媒体说明](references/reference-assets.md) 与 [CREDITS.md](CREDITS.md)。当前仓库尚未指定开源许可，不自动继承参考项目的许可。

已验证的范围与仍有缺口的功能分别记录。编码通过不等于观感通过；方案通过不等于成片通过。
