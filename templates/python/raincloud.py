"""raincloud: 雨云图（半小提琴 + 箱线 + 雨滴）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from theme import apply_theme
from palette import cycle

def make_figure(title='Raincloud plot'):
    apply_theme(fig_size=(7, 5))
    rng = np.random.default_rng(1)
    groups = [rng.normal(loc, 0.8, 200) for loc in [0, 1.5, 2.5]]
    labels = ['A', 'B', 'C']
    fig, ax = plt.subplots()
    for i, arr in enumerate(groups):
        kde = gaussian_kde(arr)
        ys = np.linspace(arr.min(), arr.max(), 200)
        density = kde(ys); density = density / density.max() * 0.35
        # 半小提琴（向右）
        ax.fill_betweenx(ys, i, i + density, color=cycle(i), alpha=0.6)
        # 雨滴
        jitter = rng.uniform(-0.15, -0.02, len(arr))
        ax.scatter(i + jitter, arr, s=8, color=cycle(i), alpha=0.5, edgecolors='none')
        # 箱线
        q1, med, q3 = np.percentile(arr, [25, 50, 75])
        ax.plot([i-0.2, i-0.2], [q1, q3], color='k', linewidth=4)
        ax.scatter(i-0.2, med, s=20, color='white', zorder=5)
    ax.set_xticks(range(len(groups))); ax.set_xticklabels(labels)
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
