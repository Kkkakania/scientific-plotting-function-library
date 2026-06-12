"""waterfall_timeseries: 时序瀑布桥（期初 -> 各月增减 -> 期末，含连接线）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Year-to-date waterfall bridge'):
    apply_theme(fig_size=(8, 4))
    rng = np.random.default_rng(24)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    start = 120.0
    delta = rng.normal(2, 8, 12).round(1)
    end = start + delta.sum()
    labels = ['Start'] + months + ['End']
    x = np.arange(len(labels))
    bottoms = start + np.concatenate(([0], np.cumsum(delta)))
    fig, ax = plt.subplots()
    ax.bar(0, start, color=cycle(7), width=0.65)
    up = delta >= 0
    ax.bar(x[1:-1][up], delta[up], bottom=bottoms[:-1][up],
           color=cycle(2), width=0.65, label='increase')
    ax.bar(x[1:-1][~up], delta[~up], bottom=bottoms[:-1][~up],
           color=cycle(1), width=0.65, label='decrease')
    ax.bar(len(labels) - 1, end, color=cycle(7), width=0.65, label='total')
    # 阶梯连接线
    lv = np.concatenate(([start], bottoms[1:], [end]))
    ax.hlines(lv[:-1], x[:-1] - 0.325, x[1:] + 0.325,
              color='#888888', linewidth=0.7, linestyle=':')
    for xi, v in [(0, start), (len(labels) - 1, end)]:
        ax.text(xi, v + 1.5, f'{v:.0f}', ha='center', fontsize=7)
    ax.set_xticks(x); ax.set_xticklabels(labels, rotation=45, fontsize=7)
    ax.set_xlabel('period'); ax.set_ylabel('balance')
    ax.set_title(title)
    ax.legend(frameon=False, fontsize=8)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
