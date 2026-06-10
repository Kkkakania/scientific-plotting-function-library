# Origin 集成

用 Origin 官方提供的 **`originpro`** Python 包驱动 Origin 画图。这是 OriginLab
官方文档公开的标准接口（需要 Origin 2021 及更高版本，与 Python 3.8+）。

## 运行方式

### 方式 A：在 Origin 内嵌 Python 里运行

1. 打开 Origin
2. Window → Script Window → Code Builder（或 `Edit Python Code`）
3. 把任一 `.py` 文件粘贴进去运行

### 方式 B：外部 Python 调用 Origin（需要装 originpro）

```bash
pip install originpro
```

```python
# launcher.py
import originpro as op
op.set_show(True)        # 启动 Origin 可见模式
exec(open('python/line_plot.py').read())
```

退出时记得 `op.exit()`。

## 文件清单

| 文件 | 做什么 |
|---|---|
| `python/00_setup_data.py`   | 创建工作表 + 写入合成数据 |
| `python/01_line_plot.py`    | 折线 |
| `python/02_scatter.py`      | 散点（带回归线） |
| `python/03_bar_grouped.py`  | 分组柱状 |
| `python/04_errorbar.py`     | 误差棒 |
| `python/05_box_plot.py`     | 箱线图 |
| `python/06_dual_yaxis.py`   | 双 Y 轴 |
| `python/07_heatmap.py`      | 矩阵热力图 |
| `python/08_contour.py`      | 等高线 / 三维瀑布 |
| `python/09_3d_surface.py`   | 三维曲面 |
| `python/10_polar.py`        | 极坐标 |
| `python/11_multi_panel.py`  | 2×2 多面板 |
| `python/12_apply_palette.py`| 把我们的 sci_palettes 套到 Origin 图上 |
| `python/13_export_pub.py`   | 论文级导出（PDF/EMF/PNG, 300 dpi） |
| `labtalk/import_csv.ogs`    | LabTalk: 批量导入 CSV |
| `labtalk/batch_replot.ogs`  | LabTalk: 批量重新绘图 |

## 与本库其他模块的关系

Origin 不是必须的。如果你只用 Python/MATLAB，可以完全忽略 `templates/origin/`。
但如果你的实验室惯用 Origin（电气/化工/材料常见），这套脚本让你能：

- 把 Python 处理好的数据无缝送到 Origin 出图
- 用我们的 `sci_palettes` 配色（脚本 12 演示）
- 一键导出符合期刊规范的矢量图（脚本 13）
