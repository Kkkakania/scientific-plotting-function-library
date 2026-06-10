# 添加新模板的步骤

如果你自己用着用着想加一个新图型，或者把组里实测数据画图的流程沉淀成模板：

## 1. 想好图型

- 已经存在 ≠ 不能加：可以做"变种"（比如 `bar_diverging` 之外做 `bar_diverging_with_threshold`）
- 但同样的图换配色不算"新模板"，应该作为参数传入
- 优先填补 [`catalog.md`](catalog.md) 里没有的图型

## 2. 写代码

**Python**: `templates/python/<name>.py`
**MATLAB**: `templates/matlab/<name>.m`

按 [`docs/style_guide.md`](docs/style_guide.md) 的模板写。三条铁律：

1. 第一行调 `apply_theme()`
2. 不传数据时用合成数据
3. 返回 `fig` 对象，不要在函数里保存或显示

## 3. 注册到 manifest

在 `_manifest_source.txt` 末尾加一行：

```
<name>|<category>|tag1,tag2,tag3|一句话描述（不超过 30 字）
```

category 选已有的，或者起新的（同时改 `docs/api_reference.md` 里的列表）。

## 4. 重生成 manifest 和 catalog

```bash
python scripts/build_manifest.py
```

（如果还没建这个脚本，照 `manifest.json` 的现有结构手改也行。）

## 5. 测试

```bash
# Python 跑通
python templates/python/<name>.py

# 加进画廊
python render_all.py <name>
ls gallery/<name>.png        # 看效果

# 跑测试集
python -m pytest tests/test_render.py
```

## 6. 更新画廊

```bash
python scripts/build_gallery_index.py   # 重生成 gallery/index.html
```

## 命名约定

- 全小写下划线：`my_chart`、`scatter_density`
- 不要带语言/工具前缀：✅ `bode_plot`，❌ `mpl_bode_plot`
- 同主题用前缀分类：`bar_basic` / `bar_grouped` / `bar_stacked`

## 范围之外（不要加）

- 太具体的领域图（如某特定型号示波器的截图复刻）
- 装饰性的、信息密度低的图（如带渐变阴影的"PPT 风"图表）
- 依赖收费数据集才能跑的图（demo 数据必须合成）

## 我自己的代码我能直接合进来吗？

可以——只要：

- 数据是合成的、或来自公开数据集
- 没用别人有版权的代码片段
- 跟着风格指南改成 `make_figure()` 形式
