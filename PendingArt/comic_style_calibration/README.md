# 过场漫画画风矫正页 v1

用途：后续漫画画风偏移时，作为附图参考，校正人物、线条、材质与光照。不承载剧情，不作为游戏内过场资源自动接入。

## 文件

- `comic-style-calibration-v1.png`：无文字七格矫正漫画页，PNG，1024 × 1536；已逐格目视检查。生成提示中的理想尺寸为 2048 × 3072，工具实际返回上述尺寸，保留原始输出，未插值放大。
- `correction-prompt-zh.md`：日后配合该页使用的中文矫正提示词。
- `generation-prompt.txt`：本页生成时使用的完整原始提示词；使用内置 imagegen。

## 本页观察顺序

1. 首排左格：岚的脸型、蓝眼睛、猫耳、金发线条和日光肤色。
2. 首排右格：风的犬科口鼻、垂耳、杂色毛发与表情简化程度。
3. 第二排两格：岚与风的全身轮廓、相对身高、披风、靴子和尾巴。
4. 第三排通栏：城镇石木建筑、旗帜、纵深、细节密度与日光阴影。
5. 末排左格：相同人物在蓝灰夜色与琥珀灯光下的画法。
6. 末排右格：布料、皮革、旧金属的边缘、笔触与反光强度。

## 使用方法

生成新页时，把矫正页作为“画风参考”附图，同时附上新页所需角色的已确认设定或原过场截图。角色身份与服装仍以各自原始设定为准。新角色可以借用绘制语言，不需继承岚或风的外形。

修改已有页时，同时附上“待修改页”和“矫正页”，明确两者的角色。使用 `correction-prompt-zh.md`，再补充需要保留的分镜、对白和动作。

比较时优先检查脸型和头身比例，再看线条与材质，最后检查整体冷暖关系。矫正页是参考样本；若其某个细节与游戏原图冲突，游戏中已接入的原漫画优先。

## 已核对的游戏原图

以下路径均相对于相邻的 `homeing-star-game/`，于 2026-10-15 根据运行脚本确认接入：

- `assets/ui/comics/back_alley/entry_panels.png`
- `assets/ui/comics/back_alley/hangover_pill_panels.png`
- `assets/ui/comics/navigation_hall/entry_panels.png`
- `assets/ui/comics/navigation_hall/exit_panels/01_city_and_rooftop.png`
- `assets/ui/comics/navigation_hall/exit_panels/02_wind_tail.png`
- `assets/ui/comics/navigation_hall/exit_panels/03_lan_notices.png`
- `assets/ui/comics/aberration/black_cloak_master_sword_cut_in.png`
- `assets/ui/comics/aberration/black_cloak_escape_page_1.png`
- `assets/ui/comics/aberration/black_cloak_escape_page_2.png`

实际生成参考采用其中五张，具体顺序及作用见 `generation-prompt.txt`。
