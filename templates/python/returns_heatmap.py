"""returns_heatmap: 月度收益率热力日历（年 x 月矩阵，发散色 + 数值标注）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import diverging

def make_figure(title='Monthly returns heatmap'):
    apply_theme(fig_size=(7, 4))
    rng = np.random.default_rng(14)
    years = np.arange(2018, 2026)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    R = rng.normal(0.8, 3.5, (len(years), 12))       # 月收益率 (%)
    vmax = np.abs(R).max()
    fig, ax = plt.subplots()
    im = ax.imshow(R, cmap=diverging(), vmin=-vmax, vmax=vmax, aspect='auto')
    ax.set_xticks(range(12)); ax.set_xticklabels(months, fontsize=8)
    ax.set_yticks(range(len(years))); ax.set_yticklabels(years)
    for (i, j), v in np.ndenumerate(R):
        ax.text(j, i, f'{v:.0f}', ha='center', va='center', fontsize=6.5,
                color='white' if abs(v) > 0.6 * vmax else '#333333')
    ax.set_xlabel('month'); ax.set_ylabel('year'); ax.set_title(title)
    cb = fig.colorbar(im, ax=ax, shrink=0.9)
    cb.set_label('return (%)')
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
