# ROADMAP — 长期演进路线图

> 本库的长期目标：成为**电气工程方向最完整的开源科研绘图模板库**——
> 一份数据，四种语言（Python / MATLAB / Go / Origin），全部论文级出图。
>
> 维护节奏建议：每学期一个 minor 版本；每个版本聚焦一个主题，做完即验证（verify_all 全过才发版）。

## 版本现状

| 版本 | 主题 | 状态 |
|---|---|---|
| v1.0–v1.3 | 模板从 80 → 216，23 大类 | ✅ 完成 |
| v1.4 | 色彩科学工具链（color_lab / generator / validator / 40 套色板） | ✅ 完成 |
| **v1.5** | **配色革新（60 套+暗色模式）· power/energy 两大新类 · Go 语言端 · MATLAB 色板自动同步** | ✅ 完成 |
| **v1.6** | **diagram 流程图/框图大类 · 画廊语言检索 · palette_picker 选择器 · 配色 68 套 · Origin 批量出图** | ✅ 完成 |
| **v1.7** | **verify_all 全绿（252/252）· Plotly 交互端 · 暗色画廊 · COMTRADE 读取器 · v1.8 电气首发 4 模板** | ✅ 本次完成 |

## v1.6 — 巩固与验证（短期，1~2 周强度）

- [ ] 在本机（有 Go 工具链）编译验证 `templates/go/`，结果记入 verification_report
- [ ] 在本机 MATLAB 实跑 23 个新 .m 模板（沙箱只做了静态语法检查）
- [ ] 在本机 Origin 实跑 14~18 号新脚本
- [x] 把 `render_all.py --dark` 加入：一键渲染全库暗色版画廊
- [x] gallery/index.html 加"暗色预览"切换按钮
- [x] ~~scipy fallback~~ 直接装好 scipy 1.14.1，29 个模板复活，验证全绿

## v1.7 — 交互化（中期）

- [x] Plotly 端：首批 12 个高频模板（templates/plotly/，可继续扩到 30）
- [x] 画廊升级：搜索框 + 按语言筛选（py/m/go/origin）~~+ 复制代码按钮~~（复制按钮移到 picker）
- [x] `palette_picker.html`：68 套色板的交互选择器（已含 Origin 代码复制）
- [x] data_loader 支持 .tdms（可选 npTDMS）与 COMTRADE（纯 numpy，ASCII+BINARY）

## v1.8 — 电气专业纵深（中期，结合课程进度）

结合大三专业课（电机学、电力电子、电力系统分析、继电保护）逐步补齐：

- [x] 潮流可视化首发：相量图 + PQ 注入热力图（网损分布待补）
- [~] 电机：dq 轴电流轨迹 ✓（圆图法、效率云图实测版待补）
- [ ] 电力电子：开关损耗分解瀑布图、热仿真温升曲线、EMI 频谱模板
- [~] 继电保护：阶段式保护配合图 ✓（差动保护动作特性待补）
- [ ] 新能源：风电场尾流热力图、光伏阵列失配 I-V、储能寿命衰减曲线

## v2.0 — 生态化（长期，毕业设计前）

- [ ] 打包发布：PyPI（`pip install sciplot-ee`）+ MATLAB File Exchange
- [ ] 文档站：mkdocs-material，画廊在线托管
- [ ] `sciplot` CLI：`sciplot new bode_diagram --lang py --palette vivid6 --dark`
- [ ] AI 工作流：每个模板补一行"适用判据"元数据，让 agent 能按数据特征自动选模板
- [ ] 论文实战回填：把自己课程设计/竞赛/论文里实际用过的图回填成模板（最有价值的来源）

## v3.0 — 远景

- [ ] Typst/LaTeX 集成：模板直接出 PGF/TikZ 兼容输出
- [ ] 双变量/三变量编码图集（bivariate.py 已打底）
- [ ] 动画模板（matplotlib.animation：转子摇摆、潮流动态、MPPT 追踪过程）
- [ ] 与 wi-scientific-plotting-library skill 深度联动：一句话→选模板→替换数据→出图全自动

## 维护守则（给未来的自己和 agent）

1. **配色只改 Python 端**，然后跑 `python scripts/sync_matlab_palettes.py` 同步 MATLAB——不要手改 .m 色板
2. 新模板必须：注册 `_manifest_source.txt` → `build_manifest.py` → `render_all.py <name>` → `build_gallery_index.py` → pytest 全过
3. 每次发版跑 `scripts/verify_all.py`，报告进 `docs/verification_report.md`
4. 原始教程资料目录（书籍/视频/插图集）保持只读，所有原创工作只发生在本目录
