# Changelog

本库版本演化记录。

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
