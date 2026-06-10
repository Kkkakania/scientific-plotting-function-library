"""scatter_grouped: 按类别着色的散点."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_scatter

def make_figure(x=None, y=None, groups=None, title='Grouped scatter'):
    apply_theme()
    if x is None:
        x, y, groups = gen_scatter(n=80, n_groups=3, separation=2.5)
    fig, ax = plt.subplots()
    for g in np.unique(groups):
        m = groups == g
        ax.scatter(x[m], y[m], s=30, color=cycle(int(g)), alpha=0.7,
                   edgecolors='w', linewidth=0.4, label=f'class {int(g)}')
    ax.set_xlabel('feature 1'); ax.set_ylabel('feature 2'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
