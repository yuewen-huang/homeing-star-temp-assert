# 地涌藤鞭：曲线造型与局部贴图试验

2026-10-13，按用户提出的墙面地块和根区悬挂树根拼接方案制作。

`vine_bark_tile.png` 是内建 image_gen 生成的 788×1997 RGB 局部藤皮贴图，保留原输出；完整提示词见 `prompt.txt`。材质没有叶片、泥土、根尖或完整藤轮廓。首尾不预设完全相同，预览着色器使用纵向镜像重复保持采样连续。

`motion.json` 从测试仓库 `tools/build_vine_ground_slam_v2.py` 读取原有六个切线控制角、30 个姿态、生长长度与原始时长，未修改原序列帧。

实现位于测试仓库：

- `tools/lash_tiled_ribbon_preview.gd`：沿曲线绘制三角带，依据累计弧长铺设局部贴图，参考游戏 `RootCaveShell._draw_textured_root()`；长度和新造型粗细分别控制。
- `tools/preview_deer_lash_tiled.gd`：在开发房或正式第四阶段镜头内做无伤害显示，存档服务仅存在内存中。
- `tools/run-lash-tiled-preview.ps1`：动态预览与截图入口。

在 PowerShell 中执行：

```powershell
& D:\HomingStar\homeing-star-test\tools\run-lash-tiled-preview.ps1
# 使用正式第四阶段 0.8 镜头
& D:\HomingStar\homeing-star-test\tools\run-lash-tiled-preview.ps1 -Production
# 输出左右方向的关键帧截图并退出
& D:\HomingStar\homeing-star-test\tools\run-lash-tiled-preview.ps1 -Production -Capture
```

动态预览：Space 暂停/继续，左右方向键减小/增加粗细，Esc 退出。它验证重复贴图、弯曲与细长轮廓；正式攻击、原画稿和伤害判定没有替换。默认主藤根部宽 56 世界像素，副藤宽度为 76%，长度沿用原动作的扫屏范围；地面约束防止藤身穿地后看起来断开。

用户反馈修订：藤身两侧增加疏密、长短不一的小倒钩毛刺，沿固定的藤身长度位置附着并使用同一藤皮材质；尖端逐渐减少。根部锚点固定在地下，先以竖直切线出土，再通过三次曲线圆滑连接摆动藤身，消除直接抬高首段造成的直角。毛刺和根部均为程序几何调整，原始贴图没有改动。

正式接入时还需要让胶囊跟随这两条新曲线，再同步拍地反馈与招式控制。这一试验不冒充完整战斗技能。
