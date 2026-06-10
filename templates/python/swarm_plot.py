"""swarm_plot: 蜂群图（避免点重叠的散点）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Swarm plot'):
    apply_theme()
    rng = np.random.default_rng(0)
    groups = [rng.normal(loc, 0.7, 60) for loc in [0, 1.5, 1, 0.5]]
    fig, ax = plt.subplots()
    for i, arr in enumerate(groups):
        # 简易避重叠：按值排序后给 x 偏移
        sorted_y = np.sort(arr)
        x = np.full_like(sorted_y, i, dtype=float)
        offset = 0
        for j in range(1, len(sorted_y)):
            if sorted_y[j] - sorted_y[j-1] < 0.15:
                offset = -offset + 0.06 * np.sign(-offset or 1)
                x[j] = i + offset
            else:
                offset = 0
        ax.scatter(x, sorted_y, s=22, color=cycle(i), alpha=0.8, edgecolors='w', linewidth=0.3)
    ax.set_xticks(range(4)); ax.set_xticklabels(['A','B','C','D'])
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
