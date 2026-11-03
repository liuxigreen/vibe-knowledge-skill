# 可复用场景组件

`engine/scene3d.py`提供透视相机、批量投影、方向性明暗材质、盒体、高度场和简化关节人物。水滴地形与交接人物两个不同题材共用Camera和Material，不再各自重写投影与受光公式。

Camera的fov是垂直视场角；project_many输入任意形状的[...,3]数组，输出屏幕x、y、相机深度。屏幕文字固定，世界标签应通过同一投影。眼睛与目标相同等非法参数会报错。

Material使用方向光明暗近似，roughness只调整示意阴影柔和度，**不是真实PBR粗糙度**。Scene按面深度排序，不含逐像素深度缓冲；相交几何、复杂透明与遮挡可能错误。人物脚底阴影是艺术近似。遇到这些需求应切换适当后端，不用此工具假装完成电影级渲染。

`examples/courier-handoff`为8秒无音轨组件测试：伸手、接触、交接、持物。它不代表已复现古代故事风格，只验证同一角色、持物和事件次序能通过统一入口渲染。

```sh
python scripts/render.py examples/courier-handoff --preview
python scripts/render.py examples/courier-handoff
```

水滴示例继续使用本地中文字体参数。两个示例都可单独取时刻渲染；输出媒体在out目录，不提交原片或私人素材。
