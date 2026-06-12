# Changelog

本库版本演化记录。

## v2.0 — 千图计划：274 → 1000

- **模板规模扩展到 1000 个**：主清单、catalog、Python 模板、MATLAB 模板统一到
  v2.0 / 1000，保持双语入口和 `make_figure()` / 同名 MATLAB 函数约定
- **新增 `_batch_manifests/` 批次账本**：扩产条目先进入批次文件，再由
  `scripts/merge_batch_manifests.py` 检查格式、重复项和 Python/MATLAB 文件存在性后合并
- **新增共享生成内核**：
  `_utils/python/generated_patterns.py` 与 `_utils/matlab/generated_template_figure.m`
  覆盖监测、控制限、热力矩阵、等高线、聚类散点、雷达、瀑布、极坐标、相图、
  分布、气泡矩阵、森林区间、堆叠面积、阶梯、3D 曲面等 21 类表达方式
- **新增 clean-room 扩产脚本**：`scripts/generate_thousand_templates.py` 用领域包 +
  表达方式组合生成可维护模板，不复制 akun 原始源码、截图、二进制素材或第三方色值
- **收编 S1-S3 高价值手写模板**：高级时序、金融/SPC、关系网络、统计推断、
  电能质量、通信/雷达等 54 对 Python/MATLAB 模板进入主清单
- **发布面同步**：README、API 文档、ROADMAP、release state check、manifest 和 catalog
  统一到 v2.0 / 1000，防止审核者看到版本与数量漂移

## v1.8 — akun 资料库全集精读 + 22 个吸收/纵深模板（252 → 274）

- **五路精读完成**（docs/learning/ 六份文档）：
  绘图书系（Py 11 章 + MATLAB 13 章）、信号处理/3D/AI 三书、
  akun 模板资产（16+78+139 期全对照）、数学建模 43 算法（A12/B21/C8 评级 +
  国赛速查）、Origin/Fluent/Project/期刊版式参考
- **吸收移植 10 个**（书系与 akun 资产中库内缺失的图型，按思路重写）：
  pie_donut / treemap_basic / ternary_scatter / bar_progress_bead /
  cube_heatmap / bar_hatched / bar_overlay_mckinsey /
  pulse_compression / lms_adaptive / waterfall_3d
- **v1.8 电气纵深补齐 9 个**：
  switching_loss_breakdown / thermal_transient / emi_spectrum（电力电子三件套）·
  wake_heatmap / pv_mismatch_iv / battery_degradation（新能源三件套）·
  network_loss_map / motor_circle_diagram / differential_protection（电力系统三件套）
- 信号类彩蛋 3 个（断线智能体遗留成果收编）：kalman_tracking /
  spectral_estimation_compare / lfm_chirp
- origin_map 补 14_waterfall → waterfall_3d 徽章映射（Origin 徽章 15 个）
- 画廊 274 卡片，明暗双版全量；pytest 282 项全过、verify_all 5/5 全绿
- 许可结论：商业 .p 工具不可审计不入库；Rggsci（GPL）只记用法不抄色值

## v1.7 — 全绿验证 + Plotly 交互端 + 暗色画廊 + COMTRADE

- **里程碑：verify_all 首次 5/5 全绿，252/252 模板渲染零失败**
  - 依赖环境补齐后，29 个需要 scipy 的旧模板恢复全量渲染
- **Plotly 交互端**（templates/plotly/，12 个高频模板）
  - make_figure() → go.Figure，写出独立 .html（CDN 模式）
  - 配色直连库内 sci_palettes，数据与 Python 端同种子复刻
- **暗色画廊**：`python render_all.py --dark` → gallery/dark/ 252 张全量
  - 画廊新增 "🌙 暗色预览" 切换（页面与缩略图整体明暗互换）
  - 画廊语言徽章新增 Plotly（紫），现有 Py/MATLAB/Origin/Go/Plotly 五语
- **v1.8 电气纵深首发 4 对模板（248 → 252）**
  - phasor_diagram 三相相量图 / pq_injection_heatmap 节点 PQ 注入热力
  - dq_current_locus dq 电流轨迹（MTPA）/ protection_coordination 保护配合
- **data_loader 扩展**：纯 numpy COMTRADE 读取器（ASCII+BINARY，
  IEEE C37.111）+ load_tdms（可选 npTDMS）；新增 6 项 pytest 全过
- **release 状态检查**：新增 `scripts/check_release_state.py`，防止版本号、模板数量、
  gallery、README/API 和 palette 文档再次漂移

## v1.6 — 流程图模块 + 检索画廊 + 配色选择器

- **新增 9 个模板（25 → 26 类，239 → 248 个）**
  - 新增 diagram 大类：7 个流程图/框图/网络图模板
  - 流程图：算法流程图（判断+循环回边）/ 研究方法流程图
  - 框图：闭环控制框图 / 信号流图（Mason）/ 电气主接线单线图（110/10 kV）
  - 网络：带权有向图 / 无向图社团（纯 matplotlib，零额外依赖）
  - 吸收自资料库比对缺口：散点图矩阵 / 人口金字塔
  - 新增 `_utils/python/diagram.py`：box/diamond/oval/arrow/vflow 流程图积木
- **画廊 v2**：搜索框 + 分类下拉 + **Python/MATLAB/Origin/Go 语言筛选与徽章**
  - 新增 `templates/origin/origin_map.json`（Origin 脚本 ↔ 模板映射）
- **交互式配色选择器** `palettes/palette_picker.html`
  - 68 套全部可搜索/筛选，点色块复制 hex，一键复制四语调用代码
  - 由 `scripts/build_palette_picker.py` 从 Python 源生成，永不漂移
- **配色 60 → 68 套（风格化系列）**：guofeng5（国风）/ shuimo4（水墨+朱砂，
  deut ΔE=19.9 全库最优）/ morandi6 / econ5 + 顺序 ink_wash / cinnabar /
  bamboo + 发散 guofeng_div，全部 HCL 生成 + validator 实测
- **Origin 工作流补全**：`render_all_origin.py` 一键批量出图（Windows）+
  README 写清 "Origin 无 CLI、仅 Windows" 的结论与可行路径
- 资料库学习结论：商业工具（TheColor/GEOColor 等）为加密 .p 文件不可、
  也不应复刻；已对照其 139 个模板清单补齐缺口图型

## v1.5 — 配色革新 + 双新类 + Go 语言端

- **配色大升级**：40 → 60 套
  - 新增暗色模式套装：dark_bright7 / dark_muted6 / dark_lumen / dark_div
  - 新增大类别集 safe10（10 色 ΔE>20）、灰度全安全 mono_blue4 / mono_warm4
  - 新增顺序 8 套（forest / wine / amber / teal_deep / violet_night / steel / cool_warm_seq / dark_lumen）
  - 新增发散 5 套 + 等亮度周期色 cyclic_isoL（相位图首选）
  - 全部经 palette_validator 实测（CIEDE2000 + 色盲模拟 + 灰度），指标进 audit 报告
- **主题暗色模式**：`apply_theme(dark=True)`（Python）/ `apply_theme(9,'dark')`（MATLAB）
- **MATLAB 色板自动同步**：`scripts/sync_matlab_palettes.py`，单一数据源根治双语漂移
  （顺带修复了 MATLAB 端长期缺失 v1.4 色板的问题）
- **新增 2 大类 23 个模板（216 → 239）**
  - power (10)：摇摆曲线 / P-V 鼻形 / 等面积法则 / 保护 TCC / 故障录波 /
    经济调度 / 馈线电压 / 频率响应 / 发电机运行极限 / 线路负载热力
  - energy (10)：风功率曲线 / 风玫瑰 / 辐照度 / 储能调度 / 鸭子曲线 /
    能源结构 / EV 负荷 / Ragone / 承载力 / 光伏温度特性
  - electrical (+3)：电机转矩-转速 / 变压器效率 / 变流器效率 MAP
- **Go 语言端**（templates/go/）：sciplot 共享包（主题+配色与 Python 同源）
  + 8 个 gonum/plot 模板（⚠ 待本机编译验证）
- **Origin +5 脚本**（14~18）：瀑布图 / 双Y柱线 / 风功率曲线 / 谐波谱 / v1.5 调色板应用
- 新增 ROADMAP.md 长期路线图（v1.6 → v3.0）

## v1.3 — 主题大扩展

- 新增 80 个专业模板（120 → 200）
  - electrical (15), control (10), signal (10), rf (8), ml (10),
    multivar (6), distribution (5), specialty (10), 3d (6)
- 新增 16 个补缺模板（200 → 216）
  - cfd (5), optimization (5), nn (6)
- 新增 27 套调色板 `palettes/python/sci_palettes.py` + MATLAB 对照
- 新增 14 个 Origin Python 脚本 + 2 个 LabTalk
- 新增可筛选 HTML 画廊 `gallery/index.html`
- 新增配色实战预览（折线 + 连续色条）
- 新增 `data_loader` 助手（CSV / Excel / MAT）
- 新增 4 份文档：chart_selection / quick_start / api_reference / style_guide
- 新增 CHANGELOG / CONTRIBUTING / LICENSE / requirements / tests

## v1.2 — 扩展到 200

- 新增 80 个专业模板覆盖电气、控制、信号深度、RF/通信、ML、多变量、分布族
- 分类数从 15 扩到 20

## v1.1 — 扩展到 120

- 新增 40 个模板覆盖 stat / matrix / time / polar / 3d / signal / electrical
- 增加 `dendrogram` / `heatmap_dendro` / `contour_3d` / `polar_heatmap` 等

## v1.0 — 首个完整版

- 80 个模板（Python + MATLAB 双语）
- 6 个分类：基础 / 进阶 / 三维 / 信号 / 电气 / 论文级
- 统一主题、调色板、导出工具
- catalog.md / manifest.json / render_all 入口
- 画廊渲染流程
