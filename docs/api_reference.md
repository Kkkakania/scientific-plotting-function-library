# API 参考

## 模板函数签名约定

### Python

每个模板暴露一个 `make_figure()` 函数：

```python
def make_figure(*, title='Some title', **data_kwargs) -> matplotlib.figure.Figure:
    ...
```

- **所有参数都是关键字参数**（kwonly）
- **数据参数（x、y、M、…）传 None 时使用合成数据**（来自 `_utils/python/demo_data.py`）
- **返回 `matplotlib.figure.Figure` 对象**，由调用方决定保存或显示

通用形参约定：

| 形参名 | 类型 | 含义 |
|---|---|---|
| `x`, `y`, `z` | 1D array | 坐标轴数据 |
| `M` | 2D array | 矩阵数据 |
| `X`, `Y`, `Z` | 2D array | meshgrid 三件套 |
| `labels` | list[str] | 类别标签 |
| `values` | array | 单系列数值 |
| `V` | 2D array | (n_series, n_categories) |
| `title` | str | 图标题 |

### MATLAB

```matlab
function fig = <template_name>(varargin)
    ...
end
```

- 不传参 = 用 demo 数据
- 调用方拿到 `fig` 后用 `save_figure(fig, ...)` 导出

## 共享工具

### `_utils/python/theme.py`

| 函数 | 说明 |
|---|---|
| `apply_theme(font_size=9, fig_size=(6,4))` | 应用统一主题 |
| `chinese_friendly()` | 切换到中文友好字体 |

### `_utils/python/palette.py`

| 函数 | 说明 |
|---|---|
| `cycle(i)` | 按索引取 Wong 8 色（自动循环） |
| `sequential(hue='blue', n=256)` | 顺序色谱 |
| `diverging(n=256)` | 蓝-白-红 |

### `_utils/python/export.py`

| 函数 | 说明 |
|---|---|
| `save_figure(fig, basename, out_dir='.', formats=('png',))` | 多格式导出 |

### `_utils/python/demo_data.py`

| 函数 | 返回 |
|---|---|
| `gen_line(n=100, n_series=1, noise=0.05, seed=0)` | `(x, Y)` |
| `gen_scatter(n=200, n_groups=1, separation=2.0)` | `(X, Y, G)` |
| `gen_groups(n_cat=5, n_series=2)` | `(labels, values_matrix)` |
| `gen_matrix(rows=8, cols=10, kind='random')` | `M` |
| `gen_timeseries(n=365, n_series=1)` | `(t, Y)` |
| `gen_signal(fs=1000, T=1.0, components=...)` | `(t, sig, fs)` |
| `gen_3d_surface(n=60, kind='peaks')` | `(X, Y, Z)` |
| `gen_categorical_pairs(n=8)` | `(cats, before, after)` |
| `gen_distribution(n=500, kind='normal')` | 1D array |

### `_utils/python/data_loader.py`

| 函数 | 说明 |
|---|---|
| `load_xy(path, x_col, y_col)` | CSV/Excel/MAT → `(x, y)` |
| `load_matrix(path)` | CSV/Excel/MAT → 2D array |
| `load_groups(path, label_col, value_col)` | → `(labels, values)` |
| `load_timeseries(path, time_col, value_cols=None)` | → `(t, Y)` |
| `load_comtrade(cfg_path)` | COMTRADE `.cfg/.dat` → 录波字典 |
| `load_tdms(path, group=None, channel=None)` | TDMS → `(t, y)`，需要可选依赖 `npTDMS` |

### `palettes/python/sci_palettes.py`

| 函数 | 说明 |
|---|---|
| `list_palettes(kind=None)` | 列出名字（按类别） |
| `get_palette(name, n=256)` | 取调色板 (list[hex] 或 cmap) |
| `preview_all(savepath=None)` | 生成所有色板预览 |

MATLAB 端对应函数：

| MATLAB | Python 等价 |
|---|---|
| `apply_theme(font_size)` | `apply_theme()` |
| `palette(kind, n)` | `cycle()` / `sequential()` |
| `sci_palettes(name, n)` | `get_palette()` |
| `sci_palettes_list()` | `list_palettes()` |
| `save_figure(fig, name, dir, fmts)` | `save_figure()` |
| `demo_data(kind, ...)` | `gen_*()` 系列 |
| `load_data(path, kind, ...)` | `load_xy / load_matrix / ...` |

## render_all 入口

### Python

```bash
python render_all.py                      # 全部
python render_all.py line_basic bar_basic # 指定
python render_all.py --tag heatmap        # 按 tag 过滤
```

### MATLAB

```matlab
render_all                       % 全部
render_all('line_basic')         % 指定
render_all('--tag', 'heatmap')   % 按 tag
```

## manifest.json 结构

```json
{
  "version": "1.7",
  "count": 252,
  "templates": [
    {"name": "line_basic", "category": "basic",
     "tags": ["line", "trend"], "description": "单条折线"},
    ...
  ]
}
```

可以拿来做自动化任务（如批量按 tag 重渲染、CI 检查、生成画廊）。
