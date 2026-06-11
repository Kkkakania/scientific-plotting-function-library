"""bar_progress_bead: 滑珠进度柱状图（灰底100%柱+进度柱+顶端滑珠）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(values=None, labels=None, total=100.0,
                title='Progress bar with bead markers'):
    apply_theme()
    if values is None:
        rng = np.random.default_rng(7)
        values = np.round(np.sort(rng.uniform(20, 95, 12))[::-1], 1)
        labels = ['M%d' % (i + 1) for i in range(len(values))]
    values = np.asarray(values, dtype=float)
    x = np.arange(len(values))
    c = cycle(0)
    fig, ax = plt.subplots()
    # 背景 100% 轨道柱
    ax.bar(x, np.full_like(values, total), width=0.55,
           color='0.90', edgecolor='none', zorder=1)
    # 前景进度柱
    ax.bar(x, values, width=0.55, color=c, edgecolor='none', zorder=2)
    # 顶端滑珠：白面 + 主题色描边
    ax.scatter(x, values, s=90, facecolor='white', edgecolor=c,
               linewidth=1.6, zorder=3)
    # 数值标注
    for xi, v in zip(x, values):
        ax.text(xi, v + total * 0.045, '%.0f' % v, ha='center', va='bottom',
                fontsize=8, color='0.25')
    ax.set_xticks(x)
    if labels is not None:
        ax.set_xticklabels(labels)
    ax.set_xlabel('task'); ax.set_ylabel('completion (%)')
    ax.set_title(title)
    ax.set_ylim(0, total * 1.12)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
