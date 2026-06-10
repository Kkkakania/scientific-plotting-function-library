"""palette_showcase: 把所有调色板应用到真实图表上（折线 + 热力图），
比纯色块预览更能看出实战效果."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from sci_palettes import (PALETTES_CAT, PALETTES_SEQ, PALETTES_DIV,
                           PALETTES_CYC, get_palette)


def make_categorical_demo(name, ax):
    """折线图演示分类配色."""
    colors = PALETTES_CAT[name]
    x = np.linspace(0, 10, 100)
    for i, c in enumerate(colors):
        ax.plot(x, np.sin(x + i*np.pi/4) + i*0.4, color=c, linewidth=1.3)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(name, fontsize=9, family='monospace')


def make_continuous_demo(name, ax, kind='seq'):
    """热力图演示顺序/发散/周期配色."""
    cmap = get_palette(name)
    if kind == 'div':
        data = np.linspace(-1, 1, 256).reshape(1, -1)
        ax.imshow(data, cmap=cmap, aspect='auto', vmin=-1, vmax=1)
    else:
        data = np.linspace(0, 1, 256).reshape(1, -1)
        ax.imshow(data, cmap=cmap, aspect='auto')
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(name, fontsize=9, family='monospace')


def build_showcase(savepath='palette_showcase.png'):
    cat_names = list(PALETTES_CAT)
    seq_names = list(PALETTES_SEQ)
    div_names = list(PALETTES_DIV)
    cyc_names = list(PALETTES_CYC)

    rows = (len(cat_names) + 4) // 5            # 动态行数
    fig = plt.figure(figsize=(13, rows*2.6 + 1))
    gs = fig.add_gridspec(rows, 5, hspace=0.35, wspace=0.15,
                          left=0.04, right=0.98, top=0.94, bottom=0.04)

    # 分类 —— 折线
    fig.text(0.5, 0.97, 'Categorical palettes applied to line plots',
             ha='center', fontsize=11, fontweight='bold')
    for i, name in enumerate(cat_names):
        r, c = divmod(i, 5)
        ax = fig.add_subplot(gs[r, c])
        make_categorical_demo(name, ax)

    plt.savefig(savepath.replace('.png', '_cat.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)

    # 顺序 + 发散 + 周期 —— 横条
    n = len(seq_names) + len(div_names) + len(cyc_names)
    fig = plt.figure(figsize=(13, n*0.5 + 1))
    gs = fig.add_gridspec(n, 1, hspace=0.6, left=0.18, right=0.96, top=0.97, bottom=0.02)

    i = 0
    for name in seq_names:
        ax = fig.add_subplot(gs[i]); make_continuous_demo(name, ax, 'seq'); i += 1
    for name in div_names:
        ax = fig.add_subplot(gs[i]); make_continuous_demo(name, ax, 'div'); i += 1
    for name in cyc_names:
        ax = fig.add_subplot(gs[i]); make_continuous_demo(name, ax, 'cyc'); i += 1

    plt.savefig(savepath.replace('.png', '_continuous.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)

    return savepath.replace('.png', '_cat.png'), savepath.replace('.png', '_continuous.png')


if __name__ == '__main__':
    paths = build_showcase('palette_showcase.png')
    for p in paths: print(p)
