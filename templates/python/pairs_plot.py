"""pairs_plot: 散点矩阵（PairPlot）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Pairs plot'):
    apply_theme(fig_size=(7, 7))
    rng = np.random.default_rng(3)
    n = 4
    data = rng.standard_normal((150, n))
    data[:, 1] = 0.7*data[:, 0] + 0.3*data[:, 1]
    data[:, 3] = -0.5*data[:, 2] + 0.5*data[:, 3]
    fig, axes = plt.subplots(n, n)
    for i in range(n):
        for j in range(n):
            ax = axes[i, j]
            if i == j:
                ax.hist(data[:, i], bins=20, color=cycle(0), edgecolor='w')
            else:
                ax.scatter(data[:, j], data[:, i], s=6, color=cycle(0), alpha=0.5, edgecolors='none')
            ax.tick_params(labelsize=6)
            if i < n - 1: ax.set_xticklabels([])
            if j > 0:     ax.set_yticklabels([])
            if i == n - 1: ax.set_xlabel(f'x{j+1}', fontsize=8)
            if j == 0:     ax.set_ylabel(f'x{i+1}', fontsize=8)
    fig.suptitle(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
