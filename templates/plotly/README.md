# templates/plotly — Plotly 交互模板

本目录是函数库的 **Plotly 交互端**：将库中高频 Python（matplotlib）模板移植为
`plotly.graph_objects` 实现，输出可缩放、可悬停、可切换图例的独立 HTML 文件，
适合放入网页、汇报材料或画廊在线预览。

## 用途

- 与 `templates/python/` 下的同名模板**一一对应**：合成数据逻辑（含随机种子）、
  系列数量与标签均保持一致，仅渲染后端从 matplotlib 换成 Plotly。
- 每个文件都暴露 `make_figure(...) -> plotly.graph_objects.Figure`，
  可传入自己的数据替换内置演示数据；直接运行则用确定性合成数据出图。

## 运行方式

依赖：`plotly`（开发时版本 6.8.0）、`numpy`，以及库内 `palettes/python/sci_palettes.py`（自动通过相对路径导入，无需安装）。

```bash
pip install plotly

# 单个模板：在任意目录下运行均可，HTML 输出到本目录
python templates/plotly/line_multi.py        # -> templates/plotly/line_multi.html

# 全部模板
for f in templates/plotly/*.py; do python "$f"; done
```

HTML 通过 `include_plotlyjs='cdn'` 引用 CDN 上的 plotly.js（约 20 KB/文件），
离线查看需改为 `include_plotlyjs=True`（内嵌，约 3.5 MB/文件）。

## 统一规范

- 布局：`template='plotly_white'`，全局字号 12，图例无边框（`borderwidth=0`），
  标题与轴标签必填。
- 配色：分类色一律取库内色板 `get_palette('wong')`（Wong/Okabe-Ito 色盲友好 8 色）；
  顺序色取 `sci_palettes.PALETTES_SEQ`（RGB 0-1 浮点元组）并就地转为
  Plotly colorscale（见 `heatmap_basic.py` / `duck_curve.py` 内的小工具函数）。
- 数据：numpy 固定种子，所有输出可复现。

## 与 Python 端的对应关系

| Plotly 模板 | 对应 matplotlib 模板 | 说明 |
|---|---|---|
| `line_multi.py` | `templates/python/line_multi.py` | 4 条相移正弦折线（seed 0） |
| `scatter_grouped.py` | `templates/python/scatter_grouped.py` | 3 类高斯散点（seed 0） |
| `bar_grouped.py` | `templates/python/bar_grouped.py` | 5 类 × 3 系列并排柱状（seed 0） |
| `heatmap_basic.py` | `templates/python/heatmap_basic.py` | 8×12 均匀随机热力图，库内 blues 顺序色 |
| `box_basic.py` | `templates/python/box_basic.py` | 5 组正态分布箱线（seed 3） |
| `bode_diagram.py` | `templates/python/bode_diagram.py` | 二阶系统幅频+相频两子图，4 个阻尼比 |
| `three_phase_waveform.py` | `templates/python/three_phase_waveform.py` | 三相时域波形 + 极坐标相量图 |
| `harmonic_spectrum.py` | `templates/python/harmonic_spectrum.py` | 1~25 次谐波幅值条状谱（seed 0） |
| `wind_power_curve.py` | `templates/python/wind_power_curve.py` | 设计功率曲线 + SCADA 散点 + 切入/额定/切出标注 |
| `duck_curve.py` | `templates/python/duck_curve.py` | 5 个年份净负荷曲线，blues 顺序色渐变 |
| `pareto_front.py` | `templates/python/pareto_front.py` | 400 点非支配排序 Pareto 前沿（seed 2） |
| `training_curves.py` | `templates/python/training_curves.py` | loss + accuracy 双子图，图例联动（seed 5） |

实现差异备注：

- `heatmap_basic`：Plotly Heatmap 的 y 轴做了 `autorange='reversed'`，
  保证行序与 matplotlib `imshow` 一致。
- `three_phase_waveform`：matplotlib 端用 annotate 画相量箭头；Plotly 端用
  `Scatterpolar` 射线 + `symbol='arrow'`（`angleref='previous'`）端点标记实现，
  时域曲线与相量按相别共用图例（legendgroup）。
- `bode_diagram` / `training_curves`：上下/左右子图同色系列通过 legendgroup
  绑定，点击图例可同时显隐两个子图中的对应系列。

> 注册说明：本目录尚未写入 manifest / 画廊索引，注册工作由主会话统一进行。
