# 给电气工程师的色彩科学速通

从光的物理量到屏幕上像素，从"画好看"到"投顶刊不被打回"。
全程能在本库里跑通，**不空谈，不背理论**。

## 0. 先建立直觉

颜色是**光（物理量）经过人眼锥细胞的响应（生理量）再被大脑解读（感知量）**。
任何谈颜色的工具都在这条链上的某个位置工作：

```
光谱 → XYZ (CIE 1931) → sRGB (屏幕) → Lab/OKLab (感知均匀) → LCh/OKLCh (人话)
 物理       生理             设备             感知                直觉
```

这套库的每个文件对应链上一段：

| 文件 | 处理的环节 |
|---|---|
| `color_lab.py` | 整条链的转换 + CVD（人眼故障）+ WCAG（可读性） |
| `apca.py` | 现代心理物理对比度（WCAG 3 草案） |
| `gamut.py` | sRGB 边界处理（设备能不能显示） |
| `white_point.py` | D65 屏幕 → D50 印刷 |
| `palette_generator.py` | 反向从感知量生成 sRGB |
| `palette_validator.py` | 综合体检 |

---

## 1. sRGB ≠ RGB

`#0072B2` 这个 hex 是 **sRGB 编码后的值**。屏幕实际显示需要先做"伽马解码"：

```python
from color_lab import _gamma_inv
import numpy as np
sRGB = np.array([0.0, 0.45, 0.7])     # 编码值（人看着线性）
linear = _gamma_inv(sRGB)              # 物理线性强度
# → [0.0, 0.170, 0.448]
```

物理线性的值才能做加法、乘法、平均。**直接对 sRGB 数值做插值，颜色会"暗一档"**。matplotlib 和大多数科学库都已经处理好；但你自己写代码混合两个颜色取中点时一定要先 `_gamma_inv` 再插值再 `_gamma`。

## 2. CIE Lab：感知均匀（但不完美）

人眼对蓝色变化更敏感，对绿色变化最弱。Lab 空间就是为了"L、a、b 上的距离 ≈ 人眼觉得的差异"而设计的。1976 年那一版（CIE 76）在蓝色域略挤，2000 年的 CIEDE2000 公式修正了这点。

```python
from color_lab import hex_to_rgb, srgb_to_lab, delta_e_2000
import numpy as np
c1 = srgb_to_lab(np.array(hex_to_rgb('#0072B2')))
c2 = srgb_to_lab(np.array(hex_to_rgb('#D55E00')))
dE = delta_e_2000(c1, c2)              # 39.2 → "差得很远"
```

**经验法则**：

- ΔE < 1：肉眼几乎认不出
- ΔE 1-5：靠在一起能看出区别
- ΔE 5-15：易分辨
- ΔE > 15：**两个独立颜色**（科研图分类色的下限）
- ΔE > 30：**强对比**

## 3. OKLab：2020 后的新标准

Björn Ottosson 2020 年发表的 OKLab 修正了 CIE Lab 的几个老问题：
- 蓝色域不再"挤"
- 色相变化不再有"波纹"
- 数值更稳定

```python
from color_lab import srgb_to_oklab, oklab_to_oklch
import numpy as np
ok = srgb_to_oklab(np.array(hex_to_rgb('#0072B2')))
lch = oklab_to_oklch(ok)
# OKLab L ∈ [0, 1]（CIE Lab 是 [0, 100]），a/b 约 ±0.4
```

**新项目优先用 OKLab**。CSS Color 4 / Tailwind v4 / Apple 系统都在转向 OKLab。本库的生成器有 `oklch_qualitative` / `oklch_sequential` / `oklch_diverging`，比对应的 CIE Lab 版本视觉更匀。

## 4. CVD：8% 的男读者看不见你这张图

世界上约 8% 男性、0.5% 女性是色觉缺陷者（CVD）。最常见的是绿色盲/弱（deuteranopia），其次是红色盲/弱（protanopia），蓝色盲（tritanopia）罕见。

```python
from color_lab import simulate_cvd, simulate_cvd_partial
sim_full = simulate_cvd(np.array([0.85, 0.15, 0.15]), 'deuteranopia')
sim_weak = simulate_cvd_partial(np.array([0.85, 0.15, 0.15]),
                                'deuteranopia', severity=0.5)
# 用矩阵法（Brettel/Viénot/Mollon）模拟 CVD 下看到的颜色
```

投顶刊（Nature/Science/IEEE）越来越多要求"配色对 CVD 友好"。
**红绿对比是最不友好的**（红绿色盲看二者完全相同）。
推荐替代：**蓝-橙、紫-绿、棕-蓝**。

## 5. WCAG vs APCA：对比度的两代标准

### WCAG 2（旧）
公式简单：`(L1+0.05)/(L2+0.05)`，阈值 4.5（AA）/ 7（AAA）。
问题：暗色场景下经常误判，比如灰底灰字 WCAG 判读"过"但实际不可读。

```python
from color_lab import contrast_ratio
cr = contrast_ratio((0, 0, 0), (1, 1, 1))   # 21:1，AAA
```

### APCA（WCAG 3 草案，新）
基于心理物理学的"感知亮度差"。返回带符号的 Lc（-108 ~ +106）：

```python
from apca import apca, apca_grade
Lc = apca((0.13, 0.13, 0.13), (1, 1, 1))    # 93.5 → "excellent"
g = apca_grade((0.5, 0.5, 0.5), (1, 1, 1))   # "body"（可读，正文 12pt 够用）
```

**论文里**：正文要求 Lc ≥ 60，图注 Lc ≥ 45 就够。

## 6. 色域：屏幕能显示的颜色子集

OKLab 是设备无关的感知空间——里面有些颜色 sRGB 显示器**根本无法显示**。
比如 `OKLCh = (0.7, 0.22, 60°)` 这种鲜艳橙色就超出 sRGB。

直接 `np.clip` 会让颜色失去色相变化（看起来像被烧坏）。
**正确做法是沿色相轴减小彩度直到落入色域**：

```python
from gamut import map_to_gamut_oklch, max_chroma
import numpy as np
ok = np.array([0.7, 0.22, 60])
rgb = map_to_gamut_oklch(ok)     # 自动降彩度，保色相

# 也可以预查"给定 L 和 hue，最多多大 C 还在域内"
cmax = max_chroma(0.7, 60, 'oklab')   # 0.191
```

## 7. 白点：D65 vs D50

屏幕 sRGB 用 D65（6504K，中性日光），但印刷 ICC 标准用 D50（5003K，偏暖）。
直接送印刷会有 **可见的偏色**（特别是中性灰部分）。

```python
from white_point import adapt_rgb_for_print
out = adapt_rgb_for_print(np.array(hex_to_rgb('#0072B2')))
# 屏幕的 #0072B2 → 印刷的 #2A719C（保持视觉一致）
```

毕设 / 论文打印前对所有图过一遍 `adapt_rgb_for_print` 是良好习惯。

## 8. 配色生成的硬约束

参见 `docs/palette_theory.md` 的"不可能三角"。简言之：

- **2-3 色**：可同时做到 CB 安全 + 灰度安全
- **4-6 色**：放弃灰度，保 CB
- **7-8 色**：放弃灰度，CB 也只能勉强
- **>8 色**：换用 subplot/facet，别堆一张图

## 9. 实操流程（每画一张图都这么走）

```
1. 确定数据类型 → 选 chart 类型（→ docs/chart_selection.md）
2. 确定类别数 N → 选 N 色调色板
3. 跑一遍 palette_validator.validate_report(my_palette)
4. 看一眼 palettes/python/palette_stress_test.png 同行的 CVD/灰度对照
5. 如果要印刷 → adapt_rgb_for_print
6. matplotlib 用了 → 直接传 colors
   MATLAB 用了   → sci_palettes('name') 拿 N×3
```

## 10. 常用命令一行表

| 想做 | 命令 |
|---|---|
| 列出所有 68 套 | `python palette_cli.py list` |
| 取预设转 LaTeX | `python palette_cli.py get wong --format latex -o c.tex` |
| 生成自定义 8 色 | `python palette_cli.py gen qualitative --n 8 --model oklab` |
| 体检 | `python palette_cli.py audit "#0072B2,#D55E00,#009E73"` |
| 屏幕→印刷 | `python palette_cli.py adapt "#0072B2" --to D50` |
| 图片榨色 | `python palette_cli.py extract logo.png --n 6` |
| 看 68 套 CVD/灰度对照大图 | 打开 `gallery/_palette_stress_test.png` |

## 11. 再深入

- `docs/palette_audit_report.md`：68 套预设的详细体检数据
- `docs/palette_theory.md`：不可能三角的数学分析
- `palettes/README.md`：所有工具的 API 速查

## 参考

- **CIE Lab/LCh**：CIE 标准（公开规范）
- **OKLab**：Björn Ottosson, "A perceptual color space for image processing"（2020，公开）
- **WCAG 2**：W3C 公开标准
- **APCA**：Andrew Somers, WCAG 3 working draft（公开）
- **Brettel/Viénot/Mollon CVD**：公开发表的算法
- **Wong / Okabe-Ito 配色**：发表于 Nature Methods 2011 / 2008，公开推荐

所有数学都在本库里从零实现，可独立验证。
