# 学习笔记总览 — akun 资料库全集精读

这组文档记录一次 clean-room 资料吸收：只把本地参考资料转化为图型需求、
设计判断和后续 backlog，不复制原始代码、截图、二进制素材或第三方色值。
本轮高优先级图型已重写进库（v1.8，Python+MATLAB 双语）。

## 五份笔记

| 笔记 | 覆盖资料 | 核心产出 |
|---|---|---|
| [01_绘图书系精读_PyMatlab](01_绘图书系精读_PyMatlab.md) | Python 科研绘图书（11 章）+ MATLAB 科研绘图书（13 章） | 逐章图型清单与差距；移植 pie_donut / treemap_basic / ternary_scatter |
| [02_信号处理与3D绘图精读](02_信号处理与3D绘图精读.md) | MATLAB 信号处理书（ch2-12）+ 3D 科研绘图书 + MATLAB×AI 书 | DSP 主题地图、3D 技法、AI 工作流；移植 pulse_compression / lms_adaptive / waterfall_3d |
| [03_akun模板资产精读](03_akun模板资产精读.md) | 个性化 16 期 + 进阶 78 期 + 纯净版 139 期 + Rggsci/颜色包/aktoolbox/期刊风格参考 | 31 期未覆盖清单；移植 bar_progress_bead / cube_heatmap / bar_hatched / bar_overlay_mckinsey；GPL 许可红线 |
| [04_数学建模算法精读](04_数学建模算法精读.md) | 43 个数学建模算法目录（>150 个算法） | 总览表+质量评级（A12/B21/C8）、按 10 类详解、国赛题型速查 |
| [05_Origin_Fluent_Project资料精读](05_Origin_Fluent_Project资料精读.md) | Origin 三套书 + Fluent 14 案例 + Project 2019 + 期刊版式参考集 | Origin 学习路径、电气相关 Fluent 案例三选、版式检索策略 |

## 关键结论（一页速记）

1. **akun 资产对库的真实增量 ≈ 25 个图型/技法组**，v1.8 已吸收最高优先级 10 个；
   剩余清单见笔记 03 末尾，可按需逐批移植。
2. **商业工具（TheColor/TheBestColor/GEOColor/450 配色）全部是加密 .p**，
   不可审计、不可复刻；Rggsci 色值属 GPL，不能进本 MIT 库。我们的 68 套
   HCL 自产色板 + validator 体检在工程上已是替代且可验证的方案。
3. **数学建模库质量分布 A:12 / B:21 / C:8**，最大坑：GB2312 注释乱码、
   libsvm 外部依赖、`newff` 已废弃；优先掌握插值三件套、SIR 族 ODE、图论三件套。
4. **Fluent 只精学 3 个案例**（变压器油流温升 / 功率模块水冷 / 机房散热），
   定位为"温度场数据上游"——出图回到本库 thermal_transient / 等高线模板。
5. **期刊版式参考只作"版式字典"用**：观察坐标、图例、标注和多面板组织方式，不复制图片、数据或像素布局。
6. 参考代码的反模式（`clear all`/`close all`/jet 色图/无 seed）恰好反向印证
   了本库 style_guide 的每一条规则。

## 维护提示

新移植模板必须走完整注册链：`_manifest_source.txt` → `build_manifest.py`
→ `render_all.py <name>`（+ `--dark`）→ `build_gallery_index.py` → pytest。
