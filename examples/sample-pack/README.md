# 免费 sample pack

这个目录是仓库的轻量入口，用来快速理解“公开样例、合成数据、模板源码、导出结果”之间的关系。它不是完整资料包，也不包含任何论文截图、课程资料、私有数据或商业模板。

## 包含什么

| 文件或模板 | 用途 |
|---|---|
| [`sample_measurements.csv`](sample_measurements.csv) | 一份很小的合成测量数据，字段为 `time`、`voltage`、`current`、`temperature` |
| [`templates/python/line_basic.py`](../../templates/python/line_basic.py) | 单条趋势线样例 |
| [`templates/python/scatter_regression.py`](../../templates/python/scatter_regression.py) | 散点 + 拟合样例 |
| [`templates/python/bar_error.py`](../../templates/python/bar_error.py) | 柱状 + 误差棒样例 |
| [`docs/beginner_20_plots.md`](../../docs/beginner_20_plots.md) | 继续扩展到 20 个常用图 |
| [`examples/csv-workflow/`](../csv-workflow/) | 从合成 CSV 到 PNG/PDF 导出和投稿前检查报告的完整流程 |

## 快速运行

在仓库根目录运行：

```bash
python templates/python/line_basic.py
python templates/python/scatter_regression.py
python templates/python/bar_error.py
```

这些命令会使用模板内置的合成数据，并在模板目录旁边生成 PNG。生成图仅用于本地预览，不需要提交回仓库。

## 用 sample CSV 跑一张图

```python
from _utils.python.data_loader import load_xy
from templates.python.line_basic import make_figure

x, y = load_xy('examples/sample-pack/sample_measurements.csv',
               x_col='time',
               y_col='voltage')
fig = make_figure(x=x, y=y, title='Synthetic voltage response')
fig.savefig('sample_voltage_response.png', dpi=300)
```

如果要换成自己的数据，先把字段整理成简单 CSV，再替换 `x_col` 和 `y_col`。建议先导出 PNG 预览，最终投稿或报告再导出 PDF/SVG。

如果你想同时看 Python/MATLAB 双语脚本、PNG/PDF 导出和检查报告模板，继续看
[`examples/csv-workflow/`](../csv-workflow/)。

## 公开发布边界

- 可以公开：原创模板、合成数据、生成脚本、可审计文档。
- 不要提交：真实学生/实验室数据、论文截图、付费课程图、`.fig`、`.mat`、Office 文件、压缩包或本地生成的大量预览图。
- 不承诺：论文录用、审稿通过、比赛结果或商业收益。
