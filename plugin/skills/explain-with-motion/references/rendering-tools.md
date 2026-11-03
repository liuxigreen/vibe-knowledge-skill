# 渲染工具与后端选择

## 随包可运行的Python后端

`scripts/render.py`支持项目中的Python场景模块：`configure(config)`初始化字体/画幅等依赖，`frame(t)`返回对应时刻的Pillow图像。每帧由明确视频时间驱动，不依赖播放速度。依赖Python 3.11+、Pillow，示例另需numpy；完整编码需PATH中的ffmpeg。

```text
python scripts/check_project.py <项目>/project.json
python scripts/render.py <项目> --preview --font <中文字体文件>
python scripts/render.py <项目> --start 6.8 --end 7.8 --font <中文字体文件>
python scripts/render.py <项目> --font <中文字体文件>
```

`--preview`给出按项目设定时间渲染的原尺寸PNG和联系表；片段与全片分别输出 `out/clip.mp4`、`out/film.mp4`。当前编码器只输出无音轨H264；不要声称已经实现混音、真实景深或音画同步。需要声音时另做音轨与合成方案，不静默代加。

场景模块在本机执行代码，项目应是自己正在制作或已检查的工程。工具不会联网安装包，也不会自动下载第三方资产。

## 场景契约与可复用组件

```python
def configure(config):
    # width, height, font, seed；检查该场景支持的画幅
    ...
def frame(t):
    # t为秒，独立返回这一时刻的图像，不累加上帧状态
    return rgb_image
```

统一 `world_to_screen`，灯光、路线和标签需要跟随物体时使用同一坐标变换。相机/地形/建筑/文字/状态应拆分为函数，下一主题需要重写故事数据而非复制整片顺序。水滴示例仅证明此入口能重建该示意片，并未证明组件对任意选题通用。

Git仓库随附 `examples/water-journey/`：高度场投影、实体建筑、土层管网、分层室内近景与柔和转场。默认1280×720；示例尚不支持任意画幅，改竖屏需要重新构图，不能直接拉伸。字体不随仓库分发，用命令显式传入有中文覆盖的本地字体。

## 需要更高空间质量时

- **完整三维、复杂遮挡、粗糙材质与阴影**：优先选择three.js/WebGL或Blender等适当后端。使用具体版本、真实几何/材质与测试帧验证，不把“建议用3D”当作已接入。
- **平面文字、路径、图形与界面**：Canvas或本包Python后端可合适；不要为了体积把本应稀疏的图解做成实体沙盘。
- **真实数据或照片**：先确认数据尺度、投影和资产，别拿程序噪声地形冒充实测。

可选参考引擎：[Lemo-Opuscar技术指南](https://github.com/lemomo-ai/lemo-opuscar/blob/main/TECHNIQUE.md)提供Canvas/WebGL逐帧渲染，页面暴露 `DUR/READY/render(t)`，并用统一事件与文字接口支持检查。其文档说明Windows采用WSL。当前项目只静态研读了接口，未安装或实跑该引擎；使用时以所选版本上游说明为准，不直接套本机原生PowerShell路径。

## 检查结果分栏

清单检查、PNG关键帧、完整编码/解码、实时观看、观感对照、声音听审分别记状态。`ffprobe`正确只证明媒体参数；读时检查通过只证明清单满足启发式；源代码含灯光变量不证明最终画面有真实体量。
