# 图型选择指南

数据进来，先问自己三个问题，找对图就一半到位。

## 第一步：你的核心信息是什么？

| 想表达的事 | 走哪个分支 |
|---|---|
| **变化/趋势**（随时间或自变量）| → 走 [A 趋势](#a-趋势) |
| **比较**（不同组、不同条件之间）| → 走 [B 比较](#b-比较) |
| **分布**（一组数据长什么样）| → 走 [C 分布](#c-分布) |
| **关系**（两个或多个变量之间）| → 走 [D 关系](#d-关系) |
| **构成**（整体被怎么分解）| → 走 [E 构成] |
| **空间/矩阵**（二维网格上的值）| → 走 [F 空间] |
| **流向/转化**（A→B→C 的流量）| → 走 [G 流] |

---

## A 趋势

| 数据形态 | 选什么 | 模板名 |
|---|---|---|
| 一条曲线 | 折线 | `line_basic` |
| 多条曲线对比 | 多折线 | `line_multi` |
| 离散事件计数 | 阶梯 | `line_step` |
| 想突出累计量 | 填充折线 | `line_filled` |
| 噪声大想看趋势 | 原始+滑动平均 | `line_smoothed` / `moving_average` |
| 跨度大（10⁻²~10²）| 对数轴 | `line_log` |
| 时间×多序列 | 多序列时间 | `timeseries_multi` |
| 正负贡献分布 | 正负面积 | `area_signed` |
| 多组分累计 | 堆叠面积 | `area_stacked` |
| 配合不确定性 | 阴影带 | `errorbar_filled` / `confidence_band` |
| 多分位数 | 扇形带 | `uncertainty_fan` |

## B 比较

| 数据形态 | 选什么 | 模板名 |
|---|---|---|
| 6 个以内类别 | 柱状 | `bar_basic` |
| 多系列同分组 | 分组柱状 | `bar_grouped` |
| 类别多/标签长 | 横向条形 | `bar_horizontal` |
| 想看排序 | 棒棒糖 | `bar_lollipop` |
| 正负对比 | 发散柱状 | `bar_diverging` |
| 主因排序 + 累计 | 帕累托 | `bar_pareto` |
| before/after 配对 | 哑铃 | `bar_dumbbell` / `paired_slope` |
| 多指标雷达 | 雷达 | `radar_chart` |
| 排名多个类别 | 点图 | `dot_plot_grouped` |
| 期初到期末分解 | 瀑布 | `bar_waterfall` |

## C 分布

| 数据形态 | 选什么 | 模板名 |
|---|---|---|
| 一组数 | 直方图 | `histogram_basic` |
| 多组叠加 | 阶梯直方 | `histogram_step` |
| 累计概率 | ECDF / 累积 | `ecdf` / `histogram_cumulative` |
| 跨度极大 | 对数分箱 | `histogram_log` |
| 多组紧凑 | 箱线 | `box_basic` |
| 数据点少 | 箱线+jitter | `box_jittered` |
| 想看密度形态 | 小提琴 | `violin_basic` |
| 左右两组 | 左右拆分 | `violin_split` |
| 多组堆叠 | 山脊 | `ridgeline` |
| 全要 | 雨云 | `raincloud` |
| 检验正态 | Q-Q | `qq_plot` |

## D 关系

| 数据形态 | 选什么 | 模板名 |
|---|---|---|
| 两个连续变量 | 散点 | `scatter_basic` |
| 带类别标签 | 分组散点 | `scatter_grouped` |
| 第三维数值 | 颜色编码 | `scatter_colored` |
| 第三维数量 | 气泡 | `scatter_sized` |
| 数据点多 | 密度散点 | `scatter_density` / `density_hexbin` |
| 想加拟合 | 散点+回归 | `scatter_regression` |
| 多变量两两 | 散点矩阵 | `pairs_plot` |
| 高维降到 2D | t-SNE 散点 | `tsne_scatter` |
| 高维曲线 | 平行坐标 / Andrews | `parallel_coordinates` / `andrews_curves` |
| 滞后自相关 | lag plot | `lag_plot` |

## E 构成

| 数据形态 | 选什么 | 模板名 |
|---|---|---|
| 占比 | 堆叠柱 / 100% 堆叠 | `bar_stacked` / `bar_percent_stack` |
| 漏斗流程 | 漏斗图 | `funnel_chart` |
| 整体 100 格 | 华夫饼 | `waffle_chart` |
| 列联表 | 马赛克 | `mosaic_plot` |

## F 空间/矩阵

| 数据形态 | 选什么 | 模板名 |
|---|---|---|
| 矩阵热度 | 热力图 | `heatmap_basic` |
| 想标数值 | 带标注热力 | `heatmap_annotated` |
| 想看聚类 | 聚类后热力 | `heatmap_clustered` / `heatmap_dendro` |
| 相关阵 | 相关矩阵 / 相关气泡 | `correlation_matrix` / `matrix_correlogram` |
| 连续函数 | 填充等高线 | `contour_filled` |
| 矢量场 | quiver / streamplot | `quiver` / `streamplot` |
| 圆形布局 | 环形热力 | `circular_heatmap` |
| 日历型 | calendar heatmap | `calendar_heatmap` |
| 三维曲面 | surface | `surface_3d` |
| 体积/切片 | 切片 / 等值面 | `slice_3d` / `isosurface` |

## G 流向

| 数据形态 | 选什么 | 模板名 |
|---|---|---|
| 流量分配 | 桑基 | `sankey_basic` |
| 决策树 | tree | `tree_diagram` |

---

## 加分项：选完图型再选配色

| 数据特征 | 推荐 |
|---|---|
| 几个离散类别 | `wong` / `muted5` / `paper4` |
| 单一连续数值 | `blues` / `warm_lava` / `glacier` |
| 围绕中心的正负 | `blue_white_red` / `purple_white_green` |
| 周期/角度 | `twilight_like` / `phase_classic` |
| 色盲友好 | `wong` / `okabe_ito` / `purple_white_green` |
| 黑白打印 | `gray5` |

完整 27 套见 [`palettes/README.md`](../palettes/README.md)。

## 反模式（少做）

- ❌ 同一张图用 5 种以上颜色（识别成本陡增）
- ❌ 3D 柱状（视觉欺骗，2D 热力图永远更准）
- ❌ 饼图分 6+ 块（角度比较远不如柱状）
- ❌ 折线图用一字排开的不同颜色（应该用顺序或多面板）
- ❌ 默认 jet/rainbow 色谱（感知不均匀且色盲不友好，已被科研社区淘汰）
