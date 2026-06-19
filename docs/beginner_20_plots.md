# 新手 20 图路径

这个页面只放最常用、最容易复用的 20 个入口。每个条目都对应现有的 Python/MATLAB 对照模板，适合先跑通，再替换成自己的实验数据。

## 怎么使用

```bash
# Python：先跑一个模板
python templates/python/line_basic.py

# MATLAB：在仓库根目录运行
addpath(genpath('templates/matlab'));
addpath(genpath('_utils/matlab'));
fig = line_basic();
```

如果你还不知道该选哪个图，先看“想表达什么”，再打开对应模板源码。所有模板默认使用合成数据；替换数据时保留模板的主题、配色和导出方式即可。

## 20 个推荐入口

| 场景 | 推荐模板 | 适合表达 | Python | MATLAB |
|---|---|---|---|---|
| 单个变量随时间变化 | `line_basic` | 趋势、衰减、响应曲线 | [`templates/python/line_basic.py`](../templates/python/line_basic.py) | [`templates/matlab/line_basic.m`](../templates/matlab/line_basic.m) |
| 多组曲线对比 | `line_multi` | 多算法、多工况、多传感器 | [`templates/python/line_multi.py`](../templates/python/line_multi.py) | [`templates/matlab/line_multi.m`](../templates/matlab/line_multi.m) |
| 两个变量相关性 | `scatter_regression` | 实测值与拟合关系 | [`templates/python/scatter_regression.py`](../templates/python/scatter_regression.py) | [`templates/matlab/scatter_regression.m`](../templates/matlab/scatter_regression.m) |
| 均值和误差 | `bar_error` | 组间均值、标准差、标准误 | [`templates/python/bar_error.py`](../templates/python/bar_error.py) | [`templates/matlab/bar_error.m`](../templates/matlab/bar_error.m) |
| 分组柱状对比 | `bar_grouped` | 多组指标横向比较 | [`templates/python/bar_grouped.py`](../templates/python/bar_grouped.py) | [`templates/matlab/bar_grouped.m`](../templates/matlab/bar_grouped.m) |
| 组成占比 | `bar_stacked` | 构成、累计贡献、能量分解 | [`templates/python/bar_stacked.py`](../templates/python/bar_stacked.py) | [`templates/matlab/bar_stacked.m`](../templates/matlab/bar_stacked.m) |
| 二维矩阵 | `heatmap_basic` | 参数扫描、混淆矩阵、相关强度 | [`templates/python/heatmap_basic.py`](../templates/python/heatmap_basic.py) | [`templates/matlab/heatmap_basic.m`](../templates/matlab/heatmap_basic.m) |
| 带数值标注的矩阵 | `heatmap_annotated` | 小尺寸热力图、表格型结果 | [`templates/python/heatmap_annotated.py`](../templates/python/heatmap_annotated.py) | [`templates/matlab/heatmap_annotated.m`](../templates/matlab/heatmap_annotated.m) |
| 分布形状 | `histogram_basic` | 误差分布、残差、测量噪声 | [`templates/python/histogram_basic.py`](../templates/python/histogram_basic.py) | [`templates/matlab/histogram_basic.m`](../templates/matlab/histogram_basic.m) |
| 分组分布 | `box_basic` | 不同条件下的离散程度 | [`templates/python/box_basic.py`](../templates/python/box_basic.py) | [`templates/matlab/box_basic.m`](../templates/matlab/box_basic.m) |
| 分布密度 | `violin_basic` | 小样本分布形态对比 | [`templates/python/violin_basic.py`](../templates/python/violin_basic.py) | [`templates/matlab/violin_basic.m`](../templates/matlab/violin_basic.m) |
| 均值和置信带 | `confidence_band` | 重复实验均值、时序不确定性 | [`templates/python/confidence_band.py`](../templates/python/confidence_band.py) | [`templates/matlab/confidence_band.m`](../templates/matlab/confidence_band.m) |
| 单点误差棒 | `errorbar_basic` | 测量误差、估计置信区间 | [`templates/python/errorbar_basic.py`](../templates/python/errorbar_basic.py) | [`templates/matlab/errorbar_basic.m`](../templates/matlab/errorbar_basic.m) |
| 控制系统频响 | `bode_diagram` | 幅频/相频特性 | [`templates/python/bode_diagram.py`](../templates/python/bode_diagram.py) | [`templates/matlab/bode_diagram.m`](../templates/matlab/bode_diagram.m) |
| 状态轨迹 | `phase_portrait` | 非线性系统、动态行为 | [`templates/python/phase_portrait.py`](../templates/python/phase_portrait.py) | [`templates/matlab/phase_portrait.m`](../templates/matlab/phase_portrait.m) |
| 角度/方向数据 | `polar_basic` | 方向响应、周期信号 | [`templates/python/polar_basic.py`](../templates/python/polar_basic.py) | [`templates/matlab/polar_basic.m`](../templates/matlab/polar_basic.m) |
| 等值线 | `contour_lines` | 二维函数、参数面投影 | [`templates/python/contour_lines.py`](../templates/python/contour_lines.py) | [`templates/matlab/contour_lines.m`](../templates/matlab/contour_lines.m) |
| 三维曲面 | `surface_3d` | 响应面、空间场、优化结果 | [`templates/python/surface_3d.py`](../templates/python/surface_3d.py) | [`templates/matlab/surface_3d.m`](../templates/matlab/surface_3d.m) |
| 多变量降维 | `biplot_pca` | PCA 载荷和样本关系 | [`templates/python/biplot_pca.py`](../templates/python/biplot_pca.py) | [`templates/matlab/biplot_pca.m`](../templates/matlab/biplot_pca.m) |
| 日历型数据 | `calendar_heatmap` | 每日负荷、活跃度、实验批次 | [`templates/python/calendar_heatmap.py`](../templates/python/calendar_heatmap.py) | [`templates/matlab/calendar_heatmap.m`](../templates/matlab/calendar_heatmap.m) |

## 替换数据的顺序

1. 先运行模板默认的合成数据版本。
2. 再把自己的数据整理成简单数组、CSV 或矩阵。
3. 只替换模板开头的数据构造部分，先不要改主题和导出逻辑。
4. 导出前检查字号、线宽、单位、图例和目标期刊尺寸。

## 边界

这个页面是选图导航，不是论文结果保证。模板只帮助你把已有数据表达得更清楚；科学结论、实验设计和投稿结果仍需要你自己负责。
