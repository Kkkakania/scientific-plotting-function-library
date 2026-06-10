"""stress_test: 全部调色板的色盲/灰度对照压力测试图.

对每个 palette 同时显示四视角：
- 正常视觉
- 红色盲 (protanopia)
- 绿色盲 (deuteranopia)
- 灰度（按 Rec. 709 亮度）

让你一眼看出哪些 palette 在 CVD 或黑白印刷下会塌掉。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from sci_palettes import (PALETTES_CAT, PALETTES_SEQ, PALETTES_DIV,
                           PALETTES_CYC, get_palette)
from color_lab import simulate_cvd, relative_luminance, hex_to_rgb


def _to_rgb(c):
    return hex_to_rgb(c) if isinstance(c, str) else c


def _grayscale(rgb):
    L = relative_luminance(rgb)
    return np.stack([L, L, L], axis=-1) if np.asarray(rgb).ndim > 1 else (L, L, L)


def _row_categorical(name, ax_row):
    """单行：一个分类 palette × 4 视角."""
    colors = PALETTES_CAT[name]
    titles = ['normal', 'protanopia', 'deuteranopia', 'grayscale']
    transforms = [
        lambda c: _to_rgb(c),
        lambda c: simulate_cvd(_to_rgb(c), 'protanopia'),
        lambda c: simulate_cvd(_to_rgb(c), 'deuteranopia'),
        lambda c: _grayscale(_to_rgb(c)),
    ]
    for ax, title, fn in zip(ax_row, titles, transforms):
        for i, c in enumerate(colors):
            ax.add_patch(plt.Rectangle((i/len(colors), 0), 1/len(colors), 1,
                                       color=fn(c)))
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        ax.set_xticks([]); ax.set_yticks([])
    ax_row[0].set_ylabel(name, rotation=0, ha='right', va='center',
                          fontsize=8, family='monospace')


def _row_continuous(name, ax_row, kind='seq'):
    """单行：一个连续 palette × 4 视角."""
    cmap = get_palette(name)
    n = 256
    if kind == 'div':
        vals = np.linspace(-1, 1, n)
        norm = lambda v: (v + 1) / 2
    else:
        vals = np.linspace(0, 1, n)
        norm = lambda v: v
    base_rgb = cmap(norm(vals))[:, :3]

    transforms = [
        ('normal',       base_rgb),
        ('protanopia',   np.array([simulate_cvd(c, 'protanopia') for c in base_rgb])),
        ('deuteranopia', np.array([simulate_cvd(c, 'deuteranopia') for c in base_rgb])),
        ('grayscale',    np.array([_grayscale(c) for c in base_rgb])),
    ]
    for ax, (_, arr) in zip(ax_row, transforms):
        ax.imshow(arr.reshape(1, -1, 3), aspect='auto')
        ax.set_xticks([]); ax.set_yticks([])
    ax_row[0].set_ylabel(name, rotation=0, ha='right', va='center',
                          fontsize=8, family='monospace')


def build():
    cat_names = list(PALETTES_CAT)
    seq_names = list(PALETTES_SEQ)
    div_names = list(PALETTES_DIV)
    cyc_names = list(PALETTES_CYC)

    n_rows = len(cat_names) + len(seq_names) + len(div_names) + len(cyc_names)
    fig, axes = plt.subplots(n_rows, 4, figsize=(11, 0.45 * n_rows + 0.6))

    # 顶部列标题
    col_titles = ['Normal', 'Protanopia (red-blind)',
                  'Deuteranopia (green-blind)', 'Grayscale (B&W print)']
    for ax, t in zip(axes[0], col_titles):
        ax.set_title(t, fontsize=10, fontweight='bold', pad=8)

    row = 0
    for name in cat_names:
        _row_categorical(name, axes[row]); row += 1
    for name in seq_names:
        _row_continuous(name, axes[row], 'seq'); row += 1
    for name in div_names:
        _row_continuous(name, axes[row], 'div'); row += 1
    for name in cyc_names:
        _row_continuous(name, axes[row], 'cyc'); row += 1

    plt.subplots_adjust(left=0.14, right=0.99, top=0.97, bottom=0.01,
                        hspace=0.3, wspace=0.04)
    out = 'palette_stress_test.png'
    fig.savefig(out, dpi=180, bbox_inches='tight')
    print(f'wrote {out}: {n_rows} rows × 4 views')
    return out


if __name__ == '__main__':
    build()
