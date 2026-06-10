# 科研绘图函数库

English repository name: `scientific-plotting-function-library`.

当前库版本：`v1.7`。

252 个原创科研绘图模板，**Python + MATLAB 双语对照**（另有 Go 语言端 8 个、Origin 19 个脚本、Plotly 12 个交互模板），覆盖 26 大类。
配 68 套色板（含暗色模式与国风系列）、色彩科学工具链、可筛选 HTML 画廊和完整文档。

适用对象：电气工程及其自动化、信号处理、控制工程方向的本科 / 研究生 / 论文作者。

## 项目关系

这个仓库是“大型绘图函数库 / gallery 层”，负责沉淀大量可复用模板、配色和跨语言参考实现。

| 仓库 | 关系 |
|---|---|
| [`matlab-scientific-figures`](https://github.com/Kkkakania/matlab-scientific-figures) | 更小、更稳定的 MATLAB clean-room 主仓，适合用户直接从 `sftPlot*` API 入门 |
| [`matlab-figure-ci`](https://github.com/Kkkakania/matlab-figure-ci) | 质量门和发布检查工具，适合复用到多个绘图库 |
| [`matlab-plotting-skill`](https://github.com/Kkkakania/matlab-plotting-skill) | 面向 agent 的图型选择和渲染工作流 |
| [`ctgu-figure-lab`](https://github.com/Kkkakania/ctgu-figure-lab) | 上层 Web/AI 平台原型，只读审计本函数库，不混入原始素材 |

## 目录结构

```
科研绘图_函数库/
├── _utils/                 共享工具
│   ├── python/             theme · palette · export · demo_data · data_loader
│   └── matlab/             apply_theme · palette · save_figure · demo_data · load_data
├── templates/
│   ├── python/             252 个 <name>.py，每个含 make_figure()
│   ├── matlab/             252 个 <name>.m，每个是同名函数
│   ├── plotly/             12 个交互模板（写出独立 HTML）
│   ├── go/                 sciplot 包 + 8 个 gonum/plot 模板
│   └── origin/             19 个 originpro Python 脚本 + 2 个 LabTalk
├── palettes/               68 套调色板 + palette_picker.html 选择器 + 色彩科学工具链 + 实战预览
│   ├── python/sci_palettes.py
│   └── matlab/sci_palettes.m
├── gallery/                252 张模板 PNG + index.html（搜索+分类+语言筛选）
├── docs/                   完整文档集
│   ├── quick_start.md       5 分钟上手
│   ├── chart_selection.md   图型决策指南
│   ├── api_reference.md     API 参考
│   ├── style_guide.md       模板风格规范
│   └── provenance_policy.md clean-room 发布边界
├── scripts/                辅助脚本
│   ├── build_manifest.py    重生成 manifest.json + catalog.md
│   └── build_gallery_index.py  重生成画廊 HTML
├── tests/                  pytest 自动化测试
├── catalog.md              人读模板目录（按类别）
├── manifest.json           机器可读清单
├── render_all.py / .m      一键全库渲染
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE                 MIT
└── requirements.txt
```

## 26 大类一览

basic · categorical · distribution · statistical · relation · matrix · field ·
ranking · time · composite · flow · polar · 3d · signal · electrical · control ·
rf · ml · multivar · specialty · cfd · optimization · nn · **power · energy**（v1.5）· **diagram**（v1.6 流程图/框图）

完整清单见 [`catalog.md`](catalog.md)。

## 三步上手

```bash
# 1. 装依赖
pip install -r requirements.txt

# 2. 看效果（浏览器打开可筛选画廊）
open gallery/index.html

# 3. 用一个
python templates/python/bode_diagram.py
```

更多用法看 [`docs/quick_start.md`](docs/quick_start.md)。

## 用自己的数据

```python
from _utils.python.data_loader import load_xy
from templates.python.scatter_regression import make_figure

x, y = load_xy('measurement.csv', x_col='time', y_col='voltage')
fig = make_figure(x=x, y=y, title='V-t 实测')
fig.savefig('out.pdf')
```

## 暗色模式（v1.5）

```python
apply_theme(dark=True)                      # 深色主题
colors = get_palette('dark_bright7')        # 配套暗底色板
```

## 配色

```python
from palettes.python.sci_palettes import get_palette
colors = get_palette('wong')                  # 8 色色盲友好分类色
colors = get_palette('safe10')                # v1.5：10 大类别仍 ΔE>20
cmap   = get_palette('blue_white_red')        # 发散色谱
```

68 套配色全清单（交互选择器 palettes/palette_picker.html） + 选择建议见 [`palettes/README.md`](palettes/README.md)。

## 一键全库

```bash
python render_all.py                  # 全部 252 个
python render_all.py line_basic       # 指定一个
python render_all.py --tag heatmap    # 按 tag 过滤
```

```matlab
render_all                            % 全部
render_all('bode_diagram')            % 指定
render_all('--tag', 'heatmap')        % 按 tag
```

## 不知道用什么图？

打开 [`docs/chart_selection.md`](docs/chart_selection.md)，按"想表达什么"分支选。

## 添加自己的模板

看 [`CONTRIBUTING.md`](CONTRIBUTING.md) + [`docs/style_guide.md`](docs/style_guide.md)。

## 公开发布边界

本库只发布可审计的原创模板、合成数据和由公开代码生成的 gallery。
不收录 `.p/.fig/.mat/.opju`、课程资料、论文截图、私有路径、个人联系方式或
难以确认来源的二进制素材。发布前先跑：

```bash
python scripts/build_manifest.py
python scripts/build_gallery_index.py
python scripts/build_palette_picker.py
python scripts/sync_matlab_palettes.py
python scripts/check_publication_ready.py
python scripts/check_release_state.py
python -m pytest tests/
```

详细规则见 [`docs/provenance_policy.md`](docs/provenance_policy.md)。

## 设计致敬

`_utils/` 三件套（theme / palette / export）的架构理念取自
[Kkkakania/matlab-scientific-figures](https://github.com/Kkkakania/matlab-scientific-figures)
的 `sftTheme` / `sftPalette` / `sftExport`（MIT License）。
本库为完全独立的实现。

## License

MIT — 见 [`LICENSE`](LICENSE)。
