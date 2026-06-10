"""scatter_matrix: 散点图矩阵（对角线直方图，按类别着色）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Scatter-plot matrix'):
    apply_theme()
    rng = np.random.default_rng(2)
    k = 3   # 变量数
    names = ['V1', 'V2', 'V3']
    A = rng.normal([0, 0, 0], [1, .8, 1.2], (80, k)) @         np.array([[1, .6, .2], [0, 1, .5], [0, 0, 1]])
    B = rng.normal([2.5, 2, 1], [1, .9, .8], (80, k))
    data = [A, B]
    fig, axes = plt.subplots(k, k, figsize=(6.4, 6))
    for i in range(k):
        for j in range(k):
            ax = axes[i, j]
            for g, d in enumerate(data):
                if i == j:
                    ax.hist(d[:, j], bins=15, color=cycle(g), alpha=0.55)
                else:
                    ax.scatter(d[:, j], d[:, i], s=8, color=cycle(g), alpha=0.6)
            if i < k-1: ax.set_xticklabels([])
            if j > 0: ax.set_yticklabels([])
            if i == k-1: ax.set_xlabel(names[j])
            if j == 0: ax.set_ylabel(names[i])
            ax.tick_params(labelsize=7)
    fig.suptitle(title, fontsize=11)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
