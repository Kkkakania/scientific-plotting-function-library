"""calendar_heatmap: 日历热力图（每周一列、一年 53 列）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(values=None, title='Calendar heatmap'):
    apply_theme(fig_size=(9, 2.5))
    if values is None:
        rng = np.random.default_rng(2)
        values = rng.uniform(0, 1, 365)
        values[(np.arange(365) % 7 >= 5)] *= 0.4   # 周末"低活"
    M = np.full((7, 53), np.nan)
    for i, v in enumerate(values):
        wk, wd = divmod(i, 7)
        if wk < 53: M[wd, wk] = v
    fig, ax = plt.subplots()
    im = ax.imshow(M, cmap=sequential(hue='green'), aspect='auto')
    fig.colorbar(im, ax=ax, label='value', shrink=0.8)
    ax.set_yticks(range(7)); ax.set_yticklabels(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
    ax.set_xlabel('week'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
