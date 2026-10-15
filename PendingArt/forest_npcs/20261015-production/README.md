# 森林四 NPC 制作交付

2026-10-15，用户批准四人静态候选板后制作。沿用榆婆、小穗的松鼠祖孙关系，阿砾为河狸，铃尾为兔子；没有重新设计已批准外形。

## 预览与原稿

- `forest_npcs_overview.png`：地图精灵放大预览，以及 12 张实际 120×107 运行头像。
- `forest_npcs_idle_preview.gif`：4 人同步待机预览，帧持有与 Godot SpriteFrames 一致。
- 各角色目录：批准种子、透明参考画布、完整待机原稿、三表情原稿与初版保留。
- `source_manifest.json`：来源与尺寸；`package_report.json`：打包参数、脚底和显示比例。
- `generation_manifest.json`、`portrait_refinement_manifest.json`：内置 image_gen 的完整提示词、输入与原始生成路径。

所有新绘制、背景去除和表情变化由内置 image_gen 完成。Python 仅用于技能要求的参考画布、裁切、全条统一缩放、脚底对齐、图集与预览排版。四条待机分别一次生成，没有逐帧独立画四个人物。

## 正式资源

游戏仓库 `assets/sideview/characters/forest_npcs/<id>/`：四帧横排图集、独立帧、SpriteFrames、元数据。

游戏仓库 `assets/ui/portraits/dialogue_fit/<id>/`：常态、担忧、放松，共 12 张透明 120×107；大图放在 `assets/ui/portraits/forest_npcs/<id>/`。

`id` 为 `yupo`、`ali`、`lingwei`、`xiaosui`。实际地图与剧情没有接入新 NPC。

## 验证入口

游戏预览场景：`res://scenes/dev/forest_npc_art_gallery.tscn`。

测试仓库：`run-tests.ps1 -Visual -Test test_forest_npc_art`。覆盖真实资源加载、帧节奏、脚底落地、12 张运行头像、左右 TutorialDialogue 及存档不变；截图写测试运行器 artifacts 目录。
