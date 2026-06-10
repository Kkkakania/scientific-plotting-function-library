"""polar_scatter: 极坐标散点（角度+半径数据）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Polar scatter'):
    apply_theme(fig_size=(5.5, 5.5))
    rng = np.random.default_rng(21)
    n = 200
    theta = rng.uniform(0, 2*np.pi, n)
    r = rng.uniform(0, 1, n) + 0.3*np.sin(3*theta)
    c = r
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    sc = ax.scatter(theta, r, c=c, cmap='viridis', s=25, alpha=0.7, edgecolors='w', linewidth=0.4)
    fig.colorbar(sc, ax=ax, label='radius', pad=0.1)
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
