# 快速上手

5 分钟跑通第一张图，10 分钟用上自己的数据。

## 1. 环境

```bash
pip install -r requirements.txt
```

MATLAB 端不用装额外东西，确保有 Signal Processing + Statistics 工具箱即可。

## 2. 看效果

```bash
# 跑一张图
python templates/python/bode_diagram.py
# 跑全库（生成 gallery/*.png）
python render_all.py
# 浏览画廊（在浏览器打开）
open gallery/index.html        # mac
xdg-open gallery/index.html    # linux
```

## 3. 用自己的数据

每个模板的 `make_figure()` 都允许你传入数据。三种最常见情况：

**情况 A：已有 numpy 数组**

```python
import numpy as np
from templates.python.line_basic import make_figure

x = np.linspace(0, 10, 200)
y = np.sin(x) * np.exp(-x/5)
fig = make_figure(x=x, y=y, title='我的数据')
fig.savefig('my_plot.png', dpi=300)
```

**情况 B：CSV 文件**

```python
from _utils.python.data_loader import load_xy
from templates.python.scatter_regression import make_figure

x, y = load_xy('measurement.csv', x_col='time', y_col='voltage')
fig = make_figure(x=x, y=y, title='V-t 实测')
```

**情况 C：MATLAB 端用 Excel**

```matlab
addpath(genpath('templates/matlab'));
addpath(genpath('_utils/matlab'));

xy = load_data('measure.xlsx', 'xy', 'x_col', 'time', 'y_col', 'voltage');
fig = scatter_regression();        % 模板内部会用合成数据；要传你自己的数据，
                                    % 打开 scatter_regression.m 把开头的 demo 数据
                                    % 换成 xy.x, xy.y 即可
```

## 4. 套用配色

```python
from palettes.python.sci_palettes import get_palette
import matplotlib.pyplot as plt

colors = get_palette('wong')                # 分类
cmap   = get_palette('blue_white_red')      # 连续

# 用法：传给模板的 color/cmap 参数，或直接 ax.plot(..., color=colors[0])
```

MATLAB：

```matlab
addpath('palettes/matlab');
c = sci_palettes('wong');            % 8×3 RGB
cmap = sci_palettes('blue_white_red');
```

## 5. 论文级导出

模板默认输出 PNG 150 dpi（屏幕看够）。投稿时改 dpi 和格式：

```python
fig = make_figure(...)
fig.savefig('fig1.pdf')                    # 矢量
fig.savefig('fig1.png', dpi=600)           # 高分位图
fig.savefig('fig1.svg')                    # SVG 矢量
```

MATLAB：

```matlab
save_figure(gcf, 'fig1', '.', {'pdf','png','svg'});
```

期刊常见尺寸：

- 单栏 8.9 cm ≈ 3.5 in
- 双栏 18.3 cm ≈ 7.2 in
- 字号 8~10 pt，线宽 0.8~1.5 pt

模板里调 `apply_theme(font_size=8, fig_size=(3.5, 2.6))` 即可。

## 6. 找图技巧

- **不知道用什么图** → 看 [`docs/chart_selection.md`](chart_selection.md)
- **想按 tag 找** → 打开 `gallery/index.html` 用搜索框
- **想看效果** → 直接看 `gallery/<name>.png`
- **想看实现** → 看 `templates/python/<name>.py` 或 `templates/matlab/<name>.m`
