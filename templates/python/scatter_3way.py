"""scatter_3way: 散点用颜色+大小+形状同时编码三个维度."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='3-encoded scatter'):
    apply_theme()
    rng = np.random.default_rng(1)
    n = 60
    x = rng.uniform(0, 10, n); y = rng.uniform(0, 10, n)
    sizes = rng.uniform(40, 400, n)
    groups = rng.integers(0, 3, n)
    markers = ['o', 's', '^']
    fig, ax = plt.subplots()
    for g in range(3):
        m = groups == g
        ax.scatter(x[m], y[m], s=sizes[m], marker=markers[g],
                   color=cycle(g), alpha=0.6, edgecolors='k', linewidth=0.4,
                   label=f'class {g}')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
