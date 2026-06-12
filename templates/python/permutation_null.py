"""permutation_null: 置换检验零分布（null 直方图 + 观测统计量 + 双侧 p 值阴影）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, y=None, n_perm=5000, title='Permutation test null distribution'):
    apply_theme()
    rng = np.random.default_rng(6)
    if x is None:
        x = rng.normal(0.0, 1.0, 40)
        y = rng.normal(0.8, 1.0, 35)
    obs = y.mean() - x.mean()
    pooled = np.concatenate([x, y])
    nx = len(x)
    perm = rng.permuted(np.tile(pooled, (n_perm, 1)), axis=1)
    null = perm[:, nx:].mean(axis=1) - perm[:, :nx].mean(axis=1)
    p = (np.abs(null) >= abs(obs)).mean()
    fig, ax = plt.subplots()
    counts, edges, patches = ax.hist(null, bins=50, color=cycle(0), alpha=0.7,
                                     edgecolor='w', linewidth=0.3)
    for e, patch in zip(edges[:-1], patches):
        if abs(e + (edges[1] - edges[0]) / 2) >= abs(obs):
            patch.set_facecolor(cycle(1)); patch.set_alpha(0.9)
    ax.axvline(obs, color='k', linewidth=1.4,
               label=f'observed diff = {obs:.2f}')
    ax.axvline(-obs, color='k', linewidth=1.0, linestyle=':')
    ax.text(0.02, 0.95, f'two-sided p = {p:.4f}\n({n_perm} permutations)',
            transform=ax.transAxes, va='top', fontsize=8)
    ax.set_xlabel('mean difference under null')
    ax.set_ylabel('count')
    ax.set_title(title)
    ax.legend(loc='upper right')
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
