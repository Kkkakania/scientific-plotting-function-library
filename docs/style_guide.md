# 模板风格指南

新加模板时按这个清单对照，确保整库风格一致。

## Python 模板模板

```python
"""<name>: 一行说明用途."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle              # 视需要 import
from demo_data import gen_xxx          # 视需要 import


def make_figure(x=None, y=None, title='Some title'):
    apply_theme()
    if x is None:
        x, y = gen_xxx(...)            # 合成数据
    fig, ax = plt.subplots()
    ax.plot(x, y, color=cycle(0))
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
```

## MATLAB 模板模板

```matlab
function fig = <name>()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    rng(0);                            % 让 demo 数据确定性
    % 数据
    x = linspace(0, 10, 100);
    y = sin(x);
    % 画图
    fig = figure;
    plot(x, y, 'Color', palette('cat', 1), 'LineWidth', 1.5);
    xlabel('x'); ylabel('y'); title('Some title');
    grid on;
end
```

## 规则

1. **每个模板独立可运行**：直接 `python <name>.py` 或 `<name>()` 不报错
2. **第一行调主题**：`apply_theme()` 必须在最前，保证风格一致
3. **不传数据时用 demo**：方便看效果
4. **`grid on` 用点状轻量风格**：`linestyle=':'`, `alpha=0.5`
5. **去掉默认刺眼颜色**：用 `palette` / `cycle` 系列，避免直接写 `'b'`、`'r'`
6. **figure 大小默认 6×4 in**：除非有特别理由
7. **图标题 + 三轴标签都不能省**
8. **图例外加 `frameon=False` / `'Box','off'`**
9. **MATLAB 端用 `rng(<seed>)`** 让 demo 输出可重现
10. **模板名 = 文件名（小写下划线）**，不要驼峰

## 文档

每个模板必须在 manifest.json 里注册一行：

```
name|category|tag1,tag2|一句话描述
```

可用的 category 见 [`docs/api_reference.md`](api_reference.md) 的列表。

## 反模式

- ❌ 在模板里 `plt.show()`（会阻塞批量渲染）
- ❌ 直接 `plt.savefig(...)` 在 make_figure 内部（让调用方决定）
- ❌ 在 `make_figure` 里读文件（数据进参数）
- ❌ 给坐标轴写硬编码中文（图本身能用，但库目标读者覆盖全球）
- ❌ 使用 `for` 循环画 100+ 元素（用 matplotlib 矢量化 API）
- ❌ 在 MATLAB 里 `clear all` / `close all`（污染调用方环境）

## 提交前自检

```bash
# 1. 加进 _manifest_source.txt
echo 'my_chart|specialty|tag1,tag2|一句话' >> _manifest_source.txt

# 2. 重生成 manifest 和 catalog
python -c "..."   # 见 _manifest_source.txt 顶部说明

# 3. 跑一遍
python templates/python/my_chart.py

# 4. 跑 test
python -m pytest tests/

# 5. 加进画廊
python render_all.py my_chart
```
