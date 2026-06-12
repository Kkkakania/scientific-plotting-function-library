"""seasonal_subseries_v2: 季节子序列分面图（12 个月分面小图 + 月均值线）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Seasonal subseries (faceted by month)'):
    apply_theme(fig_size=(9, 3.2))
    rng = np.random.default_rng(21)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    n_years = 6
    season = 10 + 4 * np.sin((np.arange(12) - 2) * np.pi / 6)
    M = season + 0.5 * np.arange(n_years)[:, None] \
        + rng.normal(0, 0.6, (n_years, 12))            # 年 x 月
    fig, axes = plt.subplots(1, 12, sharey=True)
    for m, ax in enumerate(axes):
        ax.plot(np.arange(n_years), M[:, m], '-o', color=cycle(0),
                markersize=2.5, linewidth=1)
        ax.axhline(M[:, m].mean(), color=cycle(1), linewidth=1.4)
        ax.set_xticks([])
        ax.set_xlabel(months[m], fontsize=7)
        ax.grid(True, axis='y', linestyle=':', alpha=0.5)
        for sp in ('top', 'right'):
            ax.spines[sp].set_visible(False)
    axes[0].set_ylabel('value')
    fig.suptitle(title)
    fig.supxlabel('year index within each month panel', fontsize=8)
    fig.tight_layout(w_pad=0.2)
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
