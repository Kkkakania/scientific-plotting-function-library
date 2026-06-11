# 03 akun（阿昆的科研日常）MATLAB 模板资产精读

> 资料路径：本地 `17 akun/Matlab/`（只读参考）。对照基准：v1.7 的 `catalog.md`（252 模板）；本轮收编后为 v1.8（274 模板）。
> 精读日期：2026-06-10。
> 资产总览：个性化绘图 16 期、进阶绘图 78 期、论文插图模板 139 期 ×3 版本
> （纯净版 / 便捷版 / TheColor 版，图型相同，仅取色方式不同）、期刊风格参考 5 期、
> aktoolbox、Rggsci、颜色补充包 14 套。
> 通用提醒：akun 全系依赖其加密的 `TheColor.p` / `colorplus.p` 等取色函数，
> 我们移植时一律换成库内 `palette`/`cycle`，**不携带任何 .p 依赖**。

---

## 一、Matlab 个性化绘图（16 期）逐期点评

| 期 | 图型 | 技法核心 | 库内覆盖 |
|---|---|---|---|
| 1 | 麦肯锡商务风叠加柱状图 | 同一基线画两层 `barh`（宽 0.7 灰底对比组 + 宽 0.35 彩色主组）形成"叠加"而非堆叠；`axis off` 后全部用 `text` 手工排版双行类目标签和柱内数值；`ShowBaseLine='off'`、`hLegend.ItemTokenSize=[7 7]` 缩小图例色块 | **未覆盖** → 本次移植 `bar_overlay_mckinsey` |
| 2 | 棒棒糖图(Nature) | `plot` 短线 + `scatter` 端点，按显著性 `ind` 0/1 向量分色；横向排布、值标注在端点外侧 | 已覆盖（`bar_lollipop`） |
| 3 | 带三维球标记的折线图 | 2D 折线 + `drawball.m` 在标记点画带光照的三维球（surf 球面+camlight），依赖 geom3d 工具箱和加密 `Shadow.p` | 未覆盖；装饰性强、依赖重，**不建议移植**（低优先级） |
| 4 | 带三维球标记的三维折线图 | 第 3 期的 plot3 版本，球标记 + 地面投影阴影 | 未覆盖，同上不移植 |
| 5 | 三维分层柱状图 | 自写 `barIn3D`/`bar3level`：用 patch 手工搭 3D 柱体，把 m×n×l 数据按层堆叠到同一 3D 场景 | 部分覆盖（`bar_3d`），分层堆叠变体低优先级 |
| 6 | 带标记面的三维折线图 | `addPlane.m`：取 `xlim/zlim`，在指定 y 处 `fill3` 半透明竖直平面作"标记面"，分隔多条 3D 折线 | 未覆盖；技法可学（fill3 + facealpha 做参考面），低优先级 |
| 7 | 带标记面的三维多组折线图 | 第 6 期多组版（`addPlane_m`） | 同上 |
| 8 | 进度柱状图 | "背景 100% 灰柱 + 前景值柱"双 bar 叠画，配 90° 旋转 text 标值 — akun 最常被模仿的技法之一 | **未覆盖**，并入第 10 期移植 |
| 9 | 带抖动点的箱线图 | boxplot + 按组横向加 jitter 的 scatter 叠加 | 已覆盖（`box_jittered`） |
| 10 | 滑珠进度柱状图 | 第 8 期升级：灰底柱 + 彩色进度柱 + 顶端白底彩边圆点（"滑珠"），`scatter(...,'MarkerFaceColor','w','MarkerEdgeColor',C)` | **未覆盖** → 本次移植 `bar_progress_bead` |
| 11 | 哑铃图 | `patch` 一次画所有连线（NaN 截断技巧：X/Y 末行补 NaN 使 patch 退化为折线组）+ 两端 scatter | 已覆盖（`bar_dumbbell`）；NaN-patch 批量画线技巧值得记住 |
| 12 | 渐变折线图 | 核心一行：`patch(X,Y,Y,'edgecolor','interp')` —— 用 patch 的顶点色插值实现按 y 值渐变的折线（climate-stripes 风格），配 colorbar | **未覆盖**（库内折线均单色）；中优先级，Python 端对应 `LineCollection` |
| 13 | 个性化渐变折线图 | 第 12 期 + 黑色背景主题（`BlackBack.m` 反转前景色） | 未覆盖；我们已有统一 dark 主题，无需单独模板 |
| 14 | 密集三维柱状图 | `bar3(Z,1)` 后逐 series 改 `cdata=repmat(max(zdata),1,4)` 实现按高度赋色 + `edgecolor none`，大矩阵当 3D 直方图用 | 部分覆盖（`bar_3d`）；"bar3 按高度赋色"技法记入笔记即可 |
| 15 | 中英混合标注图 | 不是新图型：密度散点图（`ksdensity` 着色）+ 'TimesSimSun' 字体实现中文宋体/英文 Times 混排 | 图型已覆盖（`scatter_density`）；混排字体属排版技巧，与库"避免硬编码中文"方针冲突，仅记录 |
| 16 | 魔方热图 | M×M×M 三维矩阵 → 对每个体素 `plotcube`（6 面 patch）按值插值取色，缩小边长 s<1 留缝形成"魔方"；额外画一层透明 scatter3 仅为撑出 colorbar 数据映射；`XRuler.Axle.LineStyle='none'` 隐藏轴线 | **未覆盖** → 本次移植 `cube_heatmap` |

小结：16 期里 7 期为 3D 装饰/字体类（3/4/5/6/7/13/15）参考价值有限；
真正值得吸收的是 1、8+10、12、16 四个图型 + NaN-patch、patch-interp 两个技法。

---

## 二、Matlab 进阶绘图（78 期）逐期点评

> 命名规律：函数文件 = 可复用绘图核心，`*Plot.m` = demo 脚本。
> 第 39 期之后部分文件夹多套一层同名目录。

| 期 | 图型 | 技法核心 | 库内覆盖 |
|---|---|---|---|
| 1 | 山脊图 | `joyPlot.m`（File Exchange 改写）按行偏移 + fill | 已覆盖（`ridgeline`） |
| 2 | 线型热图 | 与个性化 12 期同源：patch edgecolor interp 渐变线 | 未覆盖（同"渐变折线图"，中优先级） |
| 3 | 方块热图 | scatter 方形 marker 按值着色，留缝 | 已覆盖（`heatmap_basic` 风格差异） |
| 4 | 三维堆叠柱状图 | patch 手搭 3D 堆叠柱 | 部分覆盖（`bar_3d`），低 |
| 5 | 风玫瑰图 | File Exchange `WindRose.m`（功能很全） | 已覆盖（`wind_rose`） |
| 6 | 雷达图 | `spider_plot`（File Exchange） | 已覆盖（`radar_chart`） |
| 7 | 条带热图 | climate-stripes：单行色条按年着色 | 未覆盖（低-中；与渐变线同主题可合并考虑） |
| 8/9 | (三维)聚类散点图 | gscatter / scatter3 分组着色 | 已覆盖（`scatter_grouped`/`tsne_scatter`） |
| 10 | 带填充纹理的柱状图 | **hatchfill2.m**（File Exchange）：对 bar/patch 对象叠加角度/密度/颜色可调的纹理线，黑白印刷友好；配 legendflex 自定义图例 | **未覆盖** → 本次移植 `bar_hatched`（Python 用原生 hatch，MATLAB 自写线段裁剪，不复制 hatchfill2） |
| 11 | 方块热图灵活版 | 同 3，参数化方块尺寸/缝隙 | 已覆盖 |
| 12 | 局部放大图 | `BaseZoom.m`：交互框选 + 自动画放大子轴和连接线 | 已覆盖（`zoomed_inset`，我们是声明式非交互） |
| 13 | 带填充纹理的堆叠图 | hatchfill2 用于 stacked bar | 覆盖方式同 10（hatch 技法一套通用） |
| 14 | 相关性方块热图 | 方块大小 = |r|，颜色 = r | 已覆盖（`matrix_correlogram` 气泡版；方块版属变体） |
| 15 | 华夫图 | 自写 waffle：unique 分类 → reshape 网格 → surf/grid | 已覆盖（`waffle_chart`） |
| 16 | 三维填充折线图 | fill3 把每条折线下方填成竖直彩带 | 接近覆盖（`line_collection_3d`） |
| 17/18 | (相关性)气泡热图 | scatter 网格，大小+颜色双编码 | 已覆盖（`bubble_matrix`/`matrix_correlogram`） |
| 19 | 三角气泡热图 | 上三角 mask 的气泡热图 | 变体未覆盖，低 |
| 20 | 带类别标签的三维柱状图 | bar3 + 顶部 text3 | 低 |
| 21 | 三角方块热图 | 上/下三角方块热图 | 接近覆盖（`double_triangle_heatmap`） |
| 22 | 不等宽柱状图 | `uwbar`：逐柱 patch，x 间隔即柱宽（Marimekko 单轴版） | **未覆盖**（中优先级；139 期第 91 期同图） |
| 23 | 密度散点图 | `density2D_KD`（KD 树估计密度）+ scatter 着色 | 已覆盖（`scatter_density`） |
| 24 | 悬浮柱状图 | `Floatingbar`：patch 画 [zl,zu] 区间柱（range bar/简易甘特） | **未覆盖**（中-高优先级，工程里常用区间柱） |
| 25 | 三维密度散点图 | density3D_KD + scatter3 | 低 |
| 26/27 | (水平)双向堆叠图 | 正负两向 stacked（Likert 式） | 已覆盖（`likert_diverging`/`bar_diverging`） |
| 28 | 带回归趋势线的密度散点图 | 23 期 + polyfit 趋势线 | 组合可由 `scatter_density`+`scatter_regression` 拼出 |
| 29 | 三角热图 | 单三角 mask 热图 | 接近覆盖 |
| 30 | 冲击图 | `Fbarstacked`：stacked bar + 读取 `YEndPoints` 在相邻柱间 fill 半透明梯形连接带（alluvial 风格） | **未覆盖**（中优先级；`YEndPoints` 连接带技法漂亮） |
| 31 | 桑基图 | `SankeyChart.m` 自写类 | 已覆盖（`sankey_basic`） |
| 32 | 小提琴图 | violin.m（File Exchange） | 已覆盖 |
| 33/36/41/43 | 双曲面/双网格/双三角网格/双三角曲面 | **freezeColors + colorbar_k2**：同轴两个 colormap 的经典 hack | 图型低优先级；"双 colormap"技法已被 R2023b+ `colormap(ax)` 取代，笔记记录即可 |
| 34 | 双三角热图 | 上下三角两套配色 + 双 colorbar | 已覆盖（`double_triangle_heatmap`） |
| 35/42/48/51 | 特征渲染三维散点系列 | scatter3 CData + 投影 pcolor/等高线组合 | 部分覆盖（`scatter_3d`、`contour_3d`），低 |
| 37 | 多色悬浮柱状图 | 24 期逐柱配色版 | 随 24 期一起考虑 |
| 38/39/40 | (分组/堆叠)蝴蝶图 | 左右对称 barh | 已覆盖（`population_pyramid`/`bar_diverging`） |
| 44–50 | 气泡柱状图/蝴蝶气泡/气泡堆叠系列 | bar + bubblechart 顶端气泡的排列组合 | 未覆盖但属"组合创意"，单独模板价值低 |
| 52–58 | 纹理填充柱状图全家桶（单组/多色/横向/横向堆叠） | 全部是 hatchfill2 的应用变体 | 本次 `bar_hatched` 一个模板覆盖技法本体 |
| 59 | 棒棒糖图 | 同个性化 2 期 | 已覆盖 |
| 60 | 带伪彩图的曲面图 | surf + 底面投影 pcolor | 接近覆盖（`contour_filled_3d`） |
| 61 | 滑珠散点图 | `BubbleScatter`：数据排序后沿 y=1..N 排布，点压在灰色导轨线上 | 接近覆盖（`dot_plot_grouped`），排序导轨样式可借鉴 |
| 62/66 | 滑珠气泡图（特征渲染） | 61 期 + bubblechart 大小/颜色编码 | 低 |
| 63 | 带标记线的三维填充折线图 | 16 期 + 竖直标记线 | 低 |
| 64 | 三维分组针状图 | stem3 分组着色 | **库内无 stem 系列**（见 139 期清单，中优先级） |
| 65/68/76/77 | 带分组折线段的(分区)柱状图系列 | bar 顶端叠加分组折线段强调趋势 | 未覆盖，组合型，低-中 |
| 67 | 分区柱状图 | `BlockBar`：按区块分色 + 区块分隔线/标签 | 未覆盖，低-中 |
| 69 | 同步坐标图 | `tiledlayout` + `linkaxes` 双图联动 | 接近覆盖（`small_multiples`；linkaxes 技法记录） |
| 70 | 正负面积图 | 正负分色 area | 已覆盖（`area_signed`） |
| 71/72 | 棒棒糖气泡图（特征渲染） | 棒棒糖 + bubblechart | 低 |
| 73 | 双组堆叠图 | 两组 stacked bar 并排（grouped×stacked 复合） | **未覆盖**（中优先级，论文中常见需求） |
| 74 | 叠置热力图 | 多层小热图沿对角错位叠放 | 未覆盖，低 |
| 75 | 分段折线图 | 按段变色折线 | 接近覆盖（渐变线家族） |
| 78 | 带填充等高线的曲面图 | surf + contourf 底面投影 | 已覆盖（`contour_filled_3d`） |

小结：78 期的"新意"集中在 **hatch 纹理（10/13/52–58）**、**冲击图（30）**、
**悬浮柱状图（24/37）**、**不等宽柱状图（22）**、**双组堆叠（73）**、**滑珠家族（61/62/66）**；
其余大半是"双特征渲染/气泡组合"的排列组合，覆盖判断以技法为准。

---

## 三、论文插图绘制模板 139 期：库内未覆盖清单

> 三个版本图型相同，仅浏览纯净版。139 期中绝大多数（折线/柱状/箱线/曲面/
> 等高线/极坐标/图论等）库内已有对应或更优实现，此处**只列未覆盖项**，按优先级排序。

### 高优先级（论文常用、库内空白）

| 期 | 图型 | 说明 |
|---|---|---|
| 25/26/27 | 针状图 / 多组针状图 / 三维针状图 | `stem`/`stem3` 整个家族库内缺失；离散信号、采样序列展示刚需（进阶 64 期同需求） |
| 38/40 | 饼图 / 带偏移扇区的饼图 | 库内无任何 pie；虽非"科研首选"但需求频繁，建议补 `pie_basic`+exploded 参数 |
| 10 | 叠加柱状图 | 即麦肯锡叠加柱（本次已移植 `bar_overlay_mckinsey`） |
| 91 | 不等宽柱状图 | 柱宽编码第二维度（Marimekko 单轴版），经济/能源结构图常用 |

### 中优先级（有场景、可后续补）

| 期 | 图型 | 说明 |
|---|---|---|
| 111–114 | 带线/阴影/箭头/图形标记的图 | 本质是"标注技法包"，建议做成一个 `annotation_showcase` 模板而非四个 |
| 115 | 带 LaTeX 公式的图 | interpreter='latex' 示范；可并入 annotation_showcase |
| 80 | 羽状图 | `feather`，矢量沿轴排布；信号相位展示有用 |
| 54 | 带帷幕的网格曲面图 | `meshz`；曲面边缘下垂帷幕 |
| 124–126 | 三维气泡图系列 | scatter3 + 大小编码（库 `scatter_3d` 无 size 维） |
| 52 | 三维分簇散点图 | swarm 的 3D 版 |
| 98 | 大小不同多子图 | gridspec 不等分布局示范（库 `small_multiples` 等分） |

### 低优先级（装饰性/小众/依赖重）

| 期 | 图型 | 说明 |
|---|---|---|
| 47/78 | 词云图 / 进阶词云图 | 依赖 Text Analytics Toolbox / wordcloud 库，且非定量图 |
| 13/14 | 三维柱状图高度赋色/渐变 | bar3 cdata 技法，已记笔记 |
| 57/59/73 | 光影曲面/光影伪彩/带等高线光影曲面 | `surfl`+camlight 渲染风格 |
| 62/63/64 | 水平三维柱状图系列 | 猎奇向，阅读性差 |
| 71 | 三维饼图 | chartjunk，不建议入库 |
| 117/120 | 气泡云图 / 分组气泡云图 | packed bubble，信息密度低 |
| 136/137 | 极坐标气泡图 / 分组版 | polarscatter 大小编码变体 |
| 128–135 | 函数绘图系列（fplot3/fsurf/fcontour/fimplicit…） | MATLAB 函数句柄绘图教学，对 Python 端无对应意义 |

**未覆盖统计**：139 期中确认未覆盖 **31 期**（≈22%），合并同类后约 **17 个图型/技法组**；
其中高优先级 4 组（stem 家族、pie 家族、叠加柱、不等宽柱）。
加上个性化/进阶系列特有图型（滑珠进度柱、魔方热图、hatch 纹理、冲击图、悬浮柱、
双组堆叠、渐变折线、条带热图），akun 全资产对库的真实增量约 **25 个图型/技法组**。

---

## 四、Rggsci 与颜色补充包：色板来源与许可

### Rggsci（`Rggsci.p`，加密）

- 功能：复刻 R 包 **ggsci** 的期刊配色（NPG/AAAS/NEJM/Lancet/JAMA/JCO/UCSCGB/D3/
  LocusZoom/IGV/UChicago/Star Trek/Tron/Futurama/Simpsons/GSEA/Material…），
  `C = Rggsci(idx)` 按索引返回 N×3 RGB；demo 用 `colororder(C)` 整体换色环，
  cheatsheet 图给出全部索引。
- **许可红线：ggsci 为 GPL-3。色值数组若从 ggsci/Rggsci 抄出即构成衍生，
  不得放进我们 MIT 库。** 本笔记只记录用法。需要期刊风配色时：
  (a) 引导用户自装 ggsci/Rggsci；(b) 库内继续使用我们自有的 Okabe-Ito 及
  自建色板；(c) 若要"期刊感"，从期刊官网公开品牌色/论文图中独立取色并注明出处
  （见 `docs/provenance_policy.md`）。
- 附带 `注释乱码问题解决方法.txt`：GBK 编码注释在新版 MATLAB 乱码，
  提醒我们库内 .m 一律 UTF-8 + 英文注释是对的。

### Matlab 颜色补充包（14 套，全部 .p 加密，GEOColor/TheBestColor 按指示跳过）

| 包 | 来源 | 许可注意 |
|---|---|---|
| 270addcolor / 450colorplus | akun 自集（科研常用色+补充） | .p 加密无法审计来源，**不抄色值** |
| 51/320 中国传统颜色、336 法国、206 欧洲、176 美国、328 英国、249 和风 | 各国传统色谱书籍/网站汇编 | 传统色名+色值本身多为事实数据，但该打包实现加密、出处未标，引用需回到原始公开色谱（如《中国传统色》、Nippon Colors 等）自行整理 |
| MHonor / MGenshin / MStarRail / MJay | 游戏（王者荣耀/原神/星穹铁道）与专辑封面取色 | 娱乐 IP 取色，论文场景慎用；不入库 |
| Rmetbrewer | 复刻 R 包 MetBrewer（艺术名画配色） | MetBrewer 上游许可需核实（GitHub 标注 CC0，但 .p 封装不可验证）；如要类似风格，可由我们直接从公有领域画作独立取色 |

- 通用用法模式（各 demo 一致）：`C = colorXXX(idx)` / `C = colorXXX('show')` 出速查图，
  返回 RGB 矩阵后配 `colororder` / `FaceColor` 使用。
- 结论：颜色补充包对我们的价值是 **"按主题组织色板 + 速查表 cheatsheet"的产品形态**，
  而非色值本身。我们的 `palette_picker.html` 已是同思路，可借鉴其"每包附 PNG 速查表"的做法。

---

## 五、aktoolbox 与期刊风格参考

### aktoolbox（`Matlab论文插图绘制模板/aktoolbox/`）

全部为加密 .p：

- `colorplus.p` / `addcolorplus.p`：450+270 色取色器（同颜色补充包），输入编号返回 RGB。
- `ColorMap.p`：连续 colormap 生成器（速查图 colorplus.png）。
- `Shadow.p`：给 3D 对象画地面投影阴影（个性化 3/4 期用到）。

可学之处：把"取色、colormap、阴影"做成极小 API（一个函数+一张速查图）的**工具箱袖珍化**思路；
但 .p 加密 + 公众号回复关键词获取的分发方式不可审计、不可移植，
我们坚持开源明文 `_utils` 是正确差异化。

### 期刊风格参考（5 期）

这些材料只作为版式观察对象，不进入公开仓库。可抽象出的做法是：

| 观察点 | 可公开重写的通用原则 |
|---|---|
| 分组柱状图的留白 | 用明确的 x 位置制造组间间距，避免挤在默认分类轴上 |
| 横向柱状图 | 必要时手画基线和参考线，弱化默认外框 |
| 散点与参考轴 | `box off` 后只保留需要的轴线，减少视觉噪声 |
| 小型图例 | 缩小图例 token，避免图例抢占主图空间 |
| 面积图叠置 | 透明度和层级顺序要服务数据对比，而不是装饰 |

核心可学（值得写进我们 style 检查清单）：

1. **`TickDir out` + 极短 `TickLength [.005 .005]`** —— 更轻的外向刻度。
2. **`Box off` 后用 `plot` 手画需要的轴/参考线**，比默认外框更克制。
3. **`hLegend.ItemTokenSize = [5~7, 5~7]`** 缩小图例色块（MATLAB 默认太大）。
4. **逐元素 `text` 标值 + `HorizontalAlignment` 控制**，数值直接长在图上。
5. **figure 用厘米定尺寸 + `PaperPosition` 同步 + `print -r300`**，保证出版尺寸可控
   （我们的 `save_figure.m` 已等效）。
6. 风格回归测试可以用自生成目标图，不需要保存或公开第三方截图。

---

## 六、本次移植决策

四个候选均确认库内未覆盖，全部按思路重写（非复制）入库：

| 新模板 | 来源期 | 重写要点 |
|---|---|---|
| `bar_progress_bead` | 个性化 8+10 期 | 灰底 100% 柱 + 主题色进度柱 + 白面彩边滑珠；Python/MATLAB 双语，颜色走 `cycle`/`palette` |
| `cube_heatmap` | 个性化 16 期 | 不用 plotcube 逐体素循环：Python 一次性组装 Poly3DCollection；MATLAB 单次 `patch`（Faces/Vertices/FaceVertexCData 向量化），体素留缝 s=0.82 |
| `bar_hatched` | 进阶 10/13/52–58 期 | Python 用原生 `hatch=`；MATLAB **不复制 hatchfill2**，自写矩形裁剪线段生成器（±45°/竖直/交叉），NaN 分隔一次 `plot` |
| `bar_overlay_mckinsey` | 个性化 1 期 | 双层 `barh` 叠加 + axis off + text 排版；标签改英文、配色走库色板 |

验证：Python 逐个直跑出 PNG；MATLAB 过 `scripts/check_matlab_syntax.py` 0 问题。
按任务约束，不改 manifest / 画廊 / 其它文件（后续由维护者统一注册：
`bar_progress_bead|categorical`、`cube_heatmap|matrix`、`bar_hatched|categorical`、
`bar_overlay_mckinsey|categorical`）。
