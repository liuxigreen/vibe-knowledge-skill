# Explain with Motion：研究与基础渲染模块

新增模块位于 [plugin/skills/explain-with-motion](../plugin/skills/explain-with-motion/README.md)。包含22条参考的文字定位、导演方法、统一渲染入口、时间检查器与共用相机/材质/人物组件。现有风格与Award规则保持适用；本模块的工程测试不代替Award或风格验收。

2026-11-03：12项测试通过。水滴示例完成渲染；人物交接示例完成8秒渲染与解码。共用组件以方向受光和面排序为近似，无逐像素深度缓冲或PBR，不宣称参考片观感达标。原片、音轨和私人目录不随模块发布。示例支持的画幅见各project.json；不是所有场景都支持直接改竖屏。

入口：[SKILL.md](../plugin/skills/explain-with-motion/SKILL.md)，工具：[render.py](../plugin/skills/explain-with-motion/scripts/render.py)，示例：[人物交接](../plugin/skills/explain-with-motion/examples/courier-handoff/scene.py)。
