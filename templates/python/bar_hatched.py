"""bar_hatched: 带填充纹理的分组柱状图（黑白印刷友好）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

HATCHES = ['//', 'xx', '..', '\\\\']


def make_figure(data=None, group_labels=None, series_labels=None,
                title='Hatched grouped bars'):
    apply_theme()
    if data is None:
        rng = np.random.default_rng(11)
        data = rng.uniform(2, 9, (4, 5))          # 4 个系列 × 5 组
        group_labels = ['S%d' % (i + 1) for i in range(data.shape[1])]
        series_labels = ['method %s' % s for s in 'ABCD']
    data = np.asarray(data, dtype=float)
    n_series, n_groups = data.shape
    x = np.arange(n_groups)
    width = 0.8 / n_series
    fig, ax = plt.subplots()
    for i in range(n_series):
        ax.bar(x + (i - (n_series - 1) / 2) * width, data[i], width,
               color=cycle(i), edgecolor='black', linewidth=0.8,
               hatch=HATCHES[i % len(HATCHES)],
               label=series_labels[i] if series_labels else None)
    ax.set_xticks(x)
    if group_labels is not None:
        ax.set_xticklabels(group_labels)
    ax.set_xlabel('sample'); ax.set_ylabel('RMSE (m)')
    ax.set_title(title)
    ax.set_ylim(0, data.max() * 1.28)            # 顶部留白给图例
    ax.legend(frameon=False, ncol=4, loc='upper center', fontsize=8,
              columnspacing=1.2, handlelength=1.4)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
