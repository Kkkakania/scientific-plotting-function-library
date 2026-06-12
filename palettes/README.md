# 科研配色库

不只是一堆 hex 码——这是一套**完整的色彩科学工具链**：79 套精选调色板 + 程序化生成器 + 色觉缺陷模拟 + 自动体检 + 双变量编码。

## 核心理念

配色不是设计师的玄学。它是有数学的：

- **CIE Lab 空间感知均匀** → 相同距离≈相同的视觉差异
- **色觉缺陷可以模拟** → 用 Brettel/Viénot/Mollon 矩阵预测红/绿/蓝色盲下的样貌
- **WCAG 对比度有定标** → 白底黑字 21:1（AAA）vs 灰底浅字（FAIL）
- **灰度可读性可测量** → 看 L 通道（明度）两两差是否 > 15

本库的所有调色板和工具都建立在这些公开标准上，可独立审核。

## 文件总览

| 文件 | 做什么 |
|---|---|
| `python/sci_palettes.py` | 79 套调色板 + 取色 API |
| `python/color_lab.py` | sRGB↔Lab↔LCh 转换 / CIEDE2000 / WCAG / CVD 模拟 |
| `python/palette_generator.py` | HCL 程序化生成 + 色相和声学 |
| `python/palette_extractor.py` | 从任意图片用 Lab 空间 k-means 榨色 |
| `python/palette_validator.py` | 调色板自动体检（色差/CVD/灰度/WCAG）|
| `python/bivariate.py` | 双变量调色板（X×Y 2D 颜色编码） |
| `python/palette_showcase.py` | 真实图表预览（折线+热力）|
| `python/stress_test.py` | **79 套 × 4 视角（正常/红盲/绿盲/灰度）压力测试图** |
| `matlab/sci_palettes.m` + `_list.m` | 79 套 MATLAB 镜像（`scripts/sync_matlab_palettes.py` 自动生成） |
| `matlab/color_lab.m` | MATLAB 色彩科学工具 |
| `matlab/palette_generator.m` | MATLAB 程序化生成 |
| `matlab/palette_validator.m` | MATLAB 体检报告 |

## 79 套预设调色板

**分类（30 套）** wong · okabe_ito · duo_warm_cool · duo_blue_red · muted5 · bright6 · earth7 · deep6 · gray5 · paper4 · nature_soft · science_bold · ieee_tech · bio_dna · high_contrast8 · pastel6 · ggplot_like · **dark_bright7 · dark_muted6 · vivid6 · safe10 · mono_blue4 · mono_warm4**（v1.5）· **guofeng5 · shuimo4 · morandi6 · econ5**（v1.6）· **reviewer6 · electric8 · system10**（v2.1）

**顺序（29 套）** blues · oranges · greens · purples · reds · gray_to_blue · warm_lava · inferno_like · turbo_like · glacier · thermal · ocean_depth · plasma_like · material_blue · **forest · wine · amber · teal_deep · violet_night · steel · cool_warm_seq · dark_lumen**（v1.5）· **ink_wash · cinnabar · bamboo**（v1.6）· **storm_current · copper_heat · aqua_density · graphite_gold**（v2.1）

**发散（16 套）** blue_white_red · blue_white_orange · purple_white_green · brown_white_teal · cool_dark_warm · aurora · cream_to_teal · **teal_white_rose · olive_white_indigo · earth_div · berry_lime · dark_div**（v1.5）· **guofeng_div**（v1.6）· **voltage_balance · residual_teal_magenta · soil_sky_balance**（v2.1）

**周期（4 套）** twilight_like · phase_classic · **cyclic_isoL**（v1.5，等亮度——相位图首选）· **phase_wheel_soft**（v2.1）

### v1.5 暗色模式套装

深色 PPT / dashboard / 网页用这一组（全部按 L≥60 设计，深底上保持可读）：

```python
from theme import apply_theme
apply_theme(dark=True)                       # matplotlib 深色主题
colors = get_palette('dark_bright7')         # 分类
cmap_s = get_palette('dark_lumen')           # 顺序（L 12→92 递增）
cmap_d = get_palette('dark_div')             # 发散（暗芯亮端）
```

MATLAB 端：`apply_theme(9, 'dark')` + `sci_palettes('dark_bright7')`。

实测指标（CIEDE2000 / 色盲模拟，见 `docs/palette_audit_report.md`）：
`dark_bright7` 正常 ΔE=19.9、色盲 ΔE=9.0，优于 okabe_ito（6.4）；
`safe10` 是全库唯一 10 色且 ΔE>20 的大类别集；
`mono_blue4` / `mono_warm4` 是全库唯二灰度打印全安全（ΔL≥15）的分类板。

### v2.1 工程科研扩展

v2.1 新增 11 套 clean-room 生成色板，目标不是复刻任何商业配色包，而是补齐千图库里常见的工程语义：

- `reviewer6`：论文审稿场景下的 6 色高区分分类板。
- `electric8`：电气/通信多曲线、设备类别和工况类别。
- `system10`：较多状态、策略或节点簇的系统级分类。
- `storm_current` / `aqua_density`：电流、流量、密度类连续场。
- `copper_heat` / `graphite_gold`：铜损、热负荷、工程报告热力图。
- `voltage_balance`：低压/过压偏差场。
- `residual_teal_magenta`：模型残差和正负误差。
- `soil_sky_balance`：地学、环境和合成栅格场。
- `phase_wheel_soft`：相位/角度类周期场。

## 用法速查

### 取一套配色

```python
from sci_palettes import get_palette, list_palettes
print(list_palettes())                      # 按类别列出全部 79 套

colors = get_palette('wong')                # 分类：list of hex
cmap   = get_palette('blue_white_red')      # 连续：LinearSegmentedColormap
```

### 程序化生成

```python
from palette_generator import (hcl_qualitative, hcl_sequential,
                                hcl_diverging, harmony)

# 自定义分类色（控制 L 和 C，色相均匀分布）
my_cat = hcl_qualitative(n=10, L=55, C=65)

# 自定义顺序色（指定色相 + 明度范围）
my_seq = hcl_sequential(n=256, hue=200, L_range=(95, 25), C_max=70)

# 自定义发散色
my_div = hcl_diverging(n=256, hue_neg=240, hue_pos=10)

# 从一个基色生成三色和声
trio = harmony('#0072B2', 'triadic')         # → 3 hex
```

### 从图片榨色

```python
from palette_extractor import extract_from_image
palette = extract_from_image('logo.png', n=6, sort='L')
# 自动用 Lab 空间 k-means 聚类，过滤背景灰
```

### 自动体检

```python
from palette_validator import validate, validate_report

# 一键判定（色盲 + 灰度 + 色差全过才返回 True）
ok = validate(my_palette)

# 详细报告
print(validate_report(['#0072B2', '#D55E00', '#009E73']))
```

样例输出：

```
— 色差体检（CIEDE2000，两两最小值，越大越易区分）
  正常视觉      : ✓ 38.2  优秀
  红色盲(proto.): ✓ 28.6  良好
  绿色盲(deut.) : ✓ 27.9  良好
  蓝色盲(trit.) : ✓ 31.4  优秀
— 灰度打印安全（L 通道两两最小差）: ✓ ΔL = 22.7
— WCAG 对比度（每色 vs 白/黑底）
  色号       vs 白底         vs 黑底
  #0072B2   5.19:1 AA    4.05:1 AA*
  #D55E00   3.87:1 AA*   5.43:1 AA
  #009E73   3.42:1 AA*   6.14:1 AA
```

### 颜色微调

```python
from palette_generator import lighten, darken, saturate, desaturate
new = lighten('#0072B2', 15)                # L +15
new = saturate('#D55E00', -10)              # 减彩度
```

### 双变量调色板（2D 色编码）

```python
from bivariate import bivariate_cmap, bivariate_legend
grid = bivariate_cmap(n=5, scheme='blue_red')   # 5×5 颜色矩阵
# 用法：grid[y_idx, x_idx] 给数据点上色
```

5 种内置方案：`blue_red` · `blue_yellow` · `cyan_magenta` · `green_red` · `tan_teal`

## 怎么挑

| 你的数据 / 场景 | 推荐 |
|---|---|
| 几条折线、几个柱子 | `wong` / `muted5` / `paper4` |
| 投顶刊（色盲安全是硬要求） | `wong` / `okabe_ito` / `high_contrast8` |
| 演讲/PPT 要够吸睛 | `bright6` / `science_bold` |
| 黑白打印 | `gray5` 或先跑 `validate()` |
| 期刊"高级"风 | `nature_soft` / `paper4` |
| 工业/技术报告 | `ieee_tech` / `material_blue` |
| 浓度/密度热图 | `blues` / `warm_lava` / `ocean_depth` |
| 误差/正负偏离 | `blue_white_red` / `purple_white_green`（色盲友好）|
| 温度场（科普直观） | `thermal` / `aurora` |
| 相位/角度 | `twilight_like` / `phase_classic` |
| 生物 DNA/RNA | `bio_dna`（A=绿 T=红 G=橙 C=蓝 约定俗成）|
| 同时编码两维数据 | `bivariate_cmap` |

## 压力测试图

`palette_stress_test.png`（79 行 × 4 列）是这套库最有价值的产物之一。
每行一个调色板，四列分别是：正常视觉 / 红色盲 / 绿色盲 / 灰度。
**一眼看出哪个调色板在投稿（色盲审稿人）或印刷（黑白）下会塌**。

生成或重生成：

```bash
cd palettes/python && python stress_test.py
```

## MATLAB 端

完全镜像：

```matlab
addpath('palettes/matlab');

% 取色
c    = sci_palettes('wong');                    % 8×3 RGB
cmap = sci_palettes('blue_white_red', 256);

% 色彩科学
lab  = color_lab('rgb2lab', [0 0.4 0.7]);
dE   = color_lab('deltaE2000', lab1, lab2);
cr   = color_lab('contrast', [1 1 1], [0 0 0]);
sim  = color_lab('cvd', [0 0.4 0.7], 'deuteranopia');

% 程序化生成
colors = palette_generator('qualitative', 'n', 10, 'L', 55, 'C', 65);

% 体检报告
palette_validator(colors);
```

## 设计参考

- CIE Lab/LCh 颜色空间：CIE 标准（公开规范）
- WCAG 2.1 对比度公式：W3C Web 标准（公开规范）
- Brettel/Viénot/Mollon CVD 模拟矩阵：公开发表的算法
- Wong 8 色：Wong 2011 发表于 Nature Methods 的色盲友好推荐
- Okabe-Ito 8 色：Okabe & Ito 2008 提出的等价方案

所有实现都从零写起，可独立审核数学。
