# 绘图书系精读笔记（一）：Python 版 + MATLAB 版

> 精读对象：
> - 书 A：《Python语言科研绘图与学术图表绘制从入门到精通》配套代码（`Python语言科研绘图与学术图表绘制从入门到精通/code`，chapter1–11，Jupyter Notebook + 数据集）
> - 书 B：《MATLAB科研绘图》配套代码（`MATLAB科研绘图/code`，CH01–CH13，约 130 个 .m 文件 + data/ + 第三方工具 ggthemeviolin、kde2d）
>
> 对照基准：v1.7 的 `catalog.md`（252 个模板，26 大类）；本轮收编后为 v1.8（274 个模板）。
> 结论先行：两本书 90% 的图型本库已覆盖且实现质量更高（统一主题/色板/可复现种子），
> 真正的硬缺口是 **饼图/环形图、矩形树状图（treemap）、三元相图（ternary）、地理底图类**。
> 本次已移植前三个：`pie_donut`、`treemap_basic`、`ternary_scatter`。

---

## 第一部分：书 A（Python 版）逐章笔记

### A·第1章 Python 语言基础
- **内容**：变量/数据类型/分支循环/序列切片/列表推导式/字典集合/lambda/filter/map，纯语言入门，无绘图。
- **与库的关系**：无图型；无需吸收。库的 `_utils/python` 已按工程化标准组织，超出本章水平。

### A·第2章 NumPy 与 Pandas 数据准备
- **内容**:ndarray 创建/索引/花式索引、Series/DataFrame、读 CSV/Excel/SQLite（`database.db` 读苹果股票）。
- **可吸收技巧**：把"读数据→绘图"拆成两步的工作流（本库 `data_loader.py` 已实现，且多了 COMTRADE/TDMS）。
- **差距**：无。

### A·第3章 Matplotlib / Seaborn 入门
- **图型清单**：基础折线、自定义线型标签、多子图（`plt.subplots`）、Seaborn 五种 style（white/dark/whitegrid/darkgrid/ticks）、`set_palette` 控色。
- **可吸收技巧**：① Seaborn "先设全局风格再画" 的理念与本库 `apply_theme()` 同构；② 书中演示了 style 对比图，本库可考虑在文档里加一张"主题前后对比"示意。
- **差距**：无图型缺口。

### A·第4章 统计分布图（直方/箱线/密度/小提琴/饼）
- **图型清单**：直方图（含空气温度实例）、箱线图/分类箱线图（婴儿出生数据）、KDE 密度图（德国电力消耗）、小提琴图、**饼图**（`plt.pie` + autopct）、**环状图**（pie + `wedgeprops={'width':…}`）。
- **可吸收技巧**：环状图 = 饼图设 wedge 宽度，一行参数完成；`autopct='%1.1f%%'` 自动百分比标注；`explode` 强调扇区。
- **与库差距**：histogram/box/violin/kde 全覆盖（且库多 notch/split/raincloud 等变体）；**饼图与环形图整库 252 个模板竟然一个都没有** —— 这是基础缺口。✅ 已移植为 `pie_donut`。

### A·第5章 关系与趋势图（散点/折线/面积/柱状/热力/回归/联合）
- **图型清单**：散点、带状散点 `stripplot`、**蜂群散点 `swarmplot`**、分类散点、折线/分类折线、面积图、柱状/条形、热力图、双变量 KDE、线性回归图 `regplot`（钻石数据）、联合图 `jointplot`、峰峦图（joypy）。
- **可吸收技巧**：seaborn `hue=` 一参数完成分类着色；jointplot 的"主图+边缘分布"布局。
- **与库差距**：全部已有对应（`swarm_plot`、`scatter_regression`、`joint_marginal`、`ridgeline`、`heatmap_basic`）。stripplot 可视为 `box_jittered` 的退化形态，不值得单独立模板。

### A·第6章 多变量图（气泡/堆积/平行坐标/矩阵图/分面）
- **图型清单**：气泡图（空气质量）、堆积折线、堆积面积（苹果股票 OHLC）、堆积柱状（玻璃成分）、平行坐标图、相关性矩阵热力图、散点矩阵 `pairplot`、密度矩阵、分面网格 `FacetGrid`。
- **可吸收技巧**：FacetGrid 按制造商分面的写法 → 库 `small_multiples` 已体现；相关矩阵用遮罩只画下三角（库 `double_triangle_heatmap` 更进一步：上下三角放两种统计量）。
- **与库差距**：无缺口（`scatter_sized`、`area_stacked`、`parallel_coordinates`、`correlation_matrix`、`scatter_matrix`/`pairs_plot`、`matrix_correlogram`）。

### A·第7章 专业图（雷达/矩形树状图/三元相图/峰峦）
- **图型清单**：雷达图（问卷调查）、**矩形树状图 squarify**（车辆分类）、**三元相图 plotly `scatter_ternary`**（铜锌镍合金）、峰峦图 joypy（车型里程）。
- **可吸收技巧**：① treemap 用面积编码占比，比饼图可读类目更多；② 三元相图是材料/地质/化工论文刚需，plotly 实现依赖重 —— 本库可用纯 matplotlib 重心坐标投影实现，零依赖。
- **与库差距**：雷达、峰峦已有；**treemap 和 ternary 双缺口**。✅ 已移植为 `treemap_basic`（自实现 squarified 算法，不依赖 squarify 包）与 `ternary_scatter`（纯 matplotlib，零依赖）。

### A·第8章 3D 图
- **图型清单**：3D 散点（玻璃属性）、3D 线（鸢尾花）、3D 曲面/网格（伊甸火山 DEM）、plotly 交互式 3D（Surface/scatter_3d）。
- **可吸收技巧**：用真实 DEM（火山地形）做 surface 演示比 peaks 函数更打动读者；交互式版本与静态版本一一对应的"双轨制"——本库 Plotly 端已采用同思路。
- **与库差距**：`scatter_3d`、`surface_3d`、`wireframe_3d`、`contour_3d` 全覆盖；无缺口。

### A·第9章 地理可视化（folium）
- **图型清单**：folium 地图散点（加州城市）、地图热力图（人口密度）、等值线图（火山地形 contour）。
- **可吸收技巧**：CircleMarker 半径∝sqrt(人口) 的尺度处理。
- **与库差距**：**真地理底图类（瓦片地图散点/热力）是缺口**，但依赖在线瓦片服务与 folium/HTML 输出，和本库"静态出版图、零网络依赖"定位冲突 → 记入 backlog 低优先级，不在本次移植。contour 已有。

### A·第10章 Jupyter 撰写学术论文
- **内容**：notebook + markdown + 图文混排写论文的工作流，无新图型。
- **可吸收技巧**：无需吸收（库的 gallery/render_all 已是更自动化的出版流）。

### A·第11章 综合案例（t 检验药效 / 大豆数据集）
- **图型清单**：箱线+显著性对比、countplot、pairplot、相关热力、joyplot 组合应用。
- **可吸收技巧**：**"统计检验结果直接标在图上"**（p 值/星号标注）是论文高频需求 → 建议后续给 `box_basic` 系加 significance bracket 选项（记入优先级清单）。
- **与库差距**：图型本身无缺口。

---

## 第二部分：书 B（MATLAB 版）逐章笔记

### B·第1–5章 MATLAB 语言基础（CH01–CH05）
- **内容**：CH01 变量/字符串/显示；CH02 向量矩阵创建与索引；CH03 分支循环；CH04 函数定义与调用（addNumbers、嵌套函数、全局/局部变量）；CH05 数据导入导出（readtable 读 CSV/Excel、save/load MAT、JSON/XML）。
- **与库的关系**：无图型。注意书中示例随手 `clear`/`close all`，恰是本库 style_guide 的反模式，反向印证库规范。

### B·第6章 图形窗口与绘图基础（CH06）
- **图型清单**：figure 属性（Name/Position/Color）、线型颜色标记自定义、`colormap('jet')` 散点连续着色、2×2 `subplot` 布局、`saveas`/`print` 导出。
- **可吸收技巧**：导出环节书中只讲 saveas/print，本库 `save_figure.m`+`exportgraphics` 路线已更现代；jet 色图属于本库明确避免的"刺眼默认色"。
- **差距**：无。

### B·第7章 统计图（CH07：直方/箱线/密度/小提琴/饼）
- **图型清单**：histogram（含 BinWidth/Normalization）、boxplot、`ksdensity` 密度曲线、**第三方 violinChart + ggThemeViolin 主题皮肤**（solarized/light 等）、**pie 饼图**。
- **可吸收技巧**：ggthemeviolin 的"图型函数返回句柄 + 主题函数二次加工句柄"模式，与本库 `apply_theme` 先行的思路互补 —— 值得借鉴其"主题可后置换肤"概念（backlog）。
- **与库差距**：violin/box/hist 已有且无第三方依赖；**MATLAB 端同样没有饼图模板** → ✅ `pie_donut.m` 用 patch 自绘环形，顺带覆盖饼图。

### B·第8章 常用二维图（CH08）
- **图型清单**：scatter、gscatter 分组散点、折线（太阳黑子时序）、area 面积、bar/barh、**heatmap 表格热图**、**stem 火柴杆图**、stairs 阶梯图。
- **可吸收技巧**：`gscatter` 一行分组散点（库 `scatter_grouped` 等价）；用 datetime 轴画长时序。
- **与库差距**：stem 在库里以 `impulse_response`/谐波类模板形式存在，通用 stem 可由 `line_step`+`harmonic_spectrum` 拼出，不立新模板。无硬缺口。

### B·第9章 组合与多变量图（CH09）
- **图型清单**：气泡图（手动归一化气泡大小到 [minSize,maxSize]）、堆积折线（fill 置信带）、堆积面积（手动累加 y 再 area）、分组/堆积柱状、`parallelcoords` 平行坐标、`gplotmatrix` 散点矩阵（玻璃数据按 Type 着色）。
- **可吸收技巧**：气泡大小线性归一化公式值得写进 `scatter_sized` 注释；`bar(..., 'stacked')` 与手动累加两种堆积写法对照。
- **与库差距**：全覆盖，无缺口。

### B·第10章 极坐标系图（CH10）
- **图型清单**：polarplot 极线图、雷达图（手工闭合多边形）、rose/`polarhistogram` 风玫瑰、极坐标散点、**极坐标时序轨迹图**（太阳黑子按日期卷到极轴，可视化周期性）。
- **可吸收技巧**："长周期时序卷到极坐标看周期"是个好叙事（库 `circular_heatmap`/`polar_rose` 已部分覆盖，思路可写进 chart_selection.md）。
- **与库差距**：`polar_basic/polar_scatter/polar_rose/wind_rose/radar_chart` 全有；极坐标时序轨迹算低价值变体，不立模板。

### B·第11章 三维图（CH11）
- **图型清单**：scatter3、plot3、surf/mesh（含 meshc）、bar3、**bar3h 水平三维柱**、**pie3 三维饼图**、**bubblechart3 三维气泡图**。
- **可吸收技巧**：bubblechart3 的"位置 3 维 + 大小 1 维 + 颜色 1 维"五通道编码思路，可作为 `scatter_3d` 的尺寸映射增强（backlog）。
- **与库差距**：pie3/bar3h 属于学术界公认的 chartjunk（透视失真），**有意不移植**；bubblechart3 记 backlog。其余全覆盖（`scatter_3d/surface_3d/bar_3d` 等）。

### B·第12章 地理与等高线（CH12）
- **图型清单**：geoscatter、geodensityplot 地理密度、geoplot/usamap 地理线图、geobubble 地理气泡、contour 等高线。
- **与库差距**：与书 A 第9章同一结论 —— 地理底图类是缺口但依赖 Mapping Toolbox/在线底图，与库的零依赖定位冲突；contour 已有。低优先级 backlog。

### B·第13章 综合（CH13.mlx）
- mlx 活脚本格式（二进制容器），内容为综合案例演练；无可静态精读的新图型。第三方目录 `kde2d`（二维 KDE，库 `density_kde2d` 已有同功能）、`ggthemeviolin`（见 B·第7章）。

---

## 第三部分：差距汇总与吸收优先级清单

### 缺口图型（书有、库无）

| 图型 | 出处 | 价值 | 处置 |
|---|---|---|---|
| 饼图/环形图 | A-ch4.6/4.7、B-CH07_5 | ★★★ 基础刚需，252 模板竟无 | ✅ 已移植 `pie_donut` |
| 矩形树状图 treemap | A-ch7.2 | ★★★ 占比类目多时优于饼图 | ✅ 已移植 `treemap_basic`（自实现 squarify 算法） |
| 三元相图 ternary | A-ch7.3 | ★★★ 材料/地质/化工论文刚需 | ✅ 已移植 `ternary_scatter`（纯 matplotlib/MATLAB 重心坐标） |
| 地理底图散点/热力/气泡 | A-ch9、B-CH12 | ★★ 依赖在线瓦片/工具箱 | backlog（与零依赖定位冲突，需先定方案） |
| 3D 气泡图 bubblechart3 | B-CH11_8 | ★ 可并入 scatter_3d 增强 | backlog |
| 带状散点 stripplot | A-ch5.1.3 | ★ box_jittered 已覆盖 | 不做 |
| 极坐标时序轨迹 | B-CH10_6 | ★ polar_basic 变体 | 不做 |
| pie3 / bar3h | B-CH11 | ✗ chartjunk | 明确不做（写入 chart_selection.md 反例更有价值） |

### 技巧类吸收（非新图型）

1. **显著性标注**（A-ch11）：箱线/柱状图上加 p 值括号线 —— 建议做成 `_utils` 辅助函数 `sig_bracket()`。
2. **主题后置换肤**（B-ggthemeviolin）：句柄式二次 restyle，可作为 `apply_theme(dark=…)` 之外的补充思路。
3. **气泡尺寸归一化公式**（B-CH09_1）：`s = (z-min)/(max-min)*(smax-smin)+smin`，写进 `scatter_sized` 注释。
4. **jointplot 布局**（A-ch5.9）：已有 `joint_marginal`，可补"六边形分箱"变体。
5. **真实 DEM 数据做 3D 演示**（A-ch8）：demo 数据叙事感 > 数学函数，后续给 `surface_3d` 换合成地形。

### 吸收优先级清单（Top-5）

| 优先级 | 事项 | 状态 |
|---|---|---|
| P0 | `pie_donut`（饼+环形，Py+MATLAB） | ✅ 本次完成 |
| P0 | `treemap_basic`（squarified treemap，Py+MATLAB） | ✅ 本次完成 |
| P0 | `ternary_scatter`（三元相图，Py+MATLAB） | ✅ 本次完成 |
| P1 | `sig_bracket()` 显著性标注辅助函数 + box/bar 示例 | 待办 |
| P2 | 地理底图方案调研（离线 shapefile vs 网格近似 choropleth 扩展） | 待办 |

> 注：按本次任务边界，新模板未登记进 `_manifest_source.txt`/manifest/画廊（由库维护流程统一收编）。
