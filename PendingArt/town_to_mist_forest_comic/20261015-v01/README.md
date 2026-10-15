# 离镇入林转场漫画 v01

2026-10-15。内置 image_gen 生成。用户已确认两页六格分镜并验收画面，授权拆分接入游戏。已完成六帧拆分及归航镇出城转场；工作流已整理为 `homing-star-transition-comic` skill，源包位于 `homeing-star-doc/skills/homing-star-transition-comic/`，并安装到个人技能目录。

## 已确认分镜

起点：岚离开师傅。终点：森林入口，岚发现老松鼠正在低头找东西。统一白天，无旁白、对白或文字牌匾。

| 页/格 | 角色与动作 | 镜头、情绪 | 文字 |
| --- | --- | --- | --- |
| 1/1 | 岚迈步离开，师傅在身后目送 | 中景，师傅放松，告别克制 | 承接已有对白，不重复 |
| 1/2 | 岚穿过归航镇街道，发梢和披风随步伐摆动 | 侧面中景，行动感 | 无 |
| 1/3 | 岚走出城门，前方道路通向森林 | 横向大格，镇子在后，森林在前 | 无 |
| 2/1 | 岚沿旧路进入树荫渐密、薄雾浮动的森林 | 横向远景，白天林间散射光 | 无 |
| 2/2 | 岚放缓脚步，注意到路边身影 | 侧脸近景，略带好奇，视线朝下一格 | 无 |
| 2/3 | 榆婆在旧路标旁弯腰低头拨草寻找，岚从路上走近 | 中景，头巾、衣裙和低垂尾巴清楚可见 | 无，接后续初见对话 |

结尾不揭示所找物件，不画捡钉子，不提前播放初见交谈。

## 参考来源

以下路径均相对于 E:/HomingStar。

- 画风图：`homeing-star-temp-assert/PendingArt/comic_style_calibration/comic-style-calibration-v1.png`
- 画风提示词：`homeing-star-temp-assert/PendingArt/comic_style_calibration/correction-prompt-zh.md`
- 师傅：`homeing-star-game/assets/ui/portraits/dialogue_fit/master/smile.png`，当前对白情绪头像；未使用已废弃的 `assets/ui/boss/master-portrait.png`。
- 岚：`homeing-star-temp-assert/PendingArt/character/主角-岚/表情库/微笑.png`，并参考校正页的全身衣装。
- 榆婆：`homeing-star-temp-assert/PendingArt/forest_npcs/20261015-production/yupo/approved_body_source.png` 与 `approved_portrait_source.png`。
- 镇景：`homeing-star-game/assets/ui/comics/navigation_hall/exit_panels/01_city_and_rooftop.png`。
- 第二页额外引用已生成的第一页，延续人物衣装和画风。

实际完整生成提示词见 `page-01.prompt.txt`、`page-02.prompt.txt`。工具原始输出分别为 `exec-f23e5336-4ae5-412e-be48-65a05336dfe1.png`、`exec-6ccbc2c5-a08b-4a6a-8d97-ed7874ad69ce.png`，均复制保存为本目录的 page PNG。

## 目视检查与待验收

- 每页三格，合计六格；第一页左上→右上→下方，第二页上方→左下→右下。
- 无对白、旁白、可读牌匾文字；两页均为白天，从城镇日照自然转为林荫薄雾。
- 师傅留在原地，岚独自出发；第二页没有师傅跟随。
- 岚在各格保持金发猫耳、单条浅色尾尖尾巴、绿披风与既定衣装。
- 榆婆保留松鼠口鼻、灰紫头巾、浅色衣袖、旧棕裙和低垂尾巴；最后低头拨草，不抬头交谈。
- 用户已验收人物外形、漫画节奏及画风。

## 游戏接入

- 正式资源：`homeing-star-game/assets/ui/comics/forest_entry/` 下六张独立 PNG。
- 无损裁切工具：`homeing-star-test/tools/split_forest_entry_comic.py`；裁切坐标见本目录 `panel-crops.json`。
- 场景：`res://scenes/sideview/forest_entry_comic.tscn`，从归航镇右城门进入。
- 首次依序播放六帧，点击／E／空格／Enter 前进；后续仅显示第 4 帧（第二页第一格），入场淡入结束后停留 1 秒自动进入森林。
- 沿用 `STORY_C1_FOREST_ENTERED` 判断，实际森林加载时才记完成；中断完整漫画不提前记录。已进入森林的旧档使用单帧。
- 漫画期间续播城镇 BGM，实际切入森林时沿用原定的森林 BGM 切换。漫画显示在任务及辅助 HUD 上方、场景淡入淡出下方；画面等比显示。
- 验证：`homeing-star-test/artifacts/20261015-133216-088`，漫画 45、离镇 52、榆婆 34 项检查均通过，共 131 项，零失败。已查看六帧及再次进入的实机截图。
