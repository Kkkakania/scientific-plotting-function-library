"""circular_heatmap: 极坐标热力图（环形布局）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(title='Circular heatmap'):
    apply_theme(fig_size=(6, 6))
    n_theta, n_r = 24, 6
    M = np.random.default_rng(16).uniform(0, 1, (n_r, n_theta))
    theta = np.linspace(0, 2*np.pi, n_theta+1)
    r = np.linspace(0.3, 1.0, n_r+1)
    T, R = np.meshgrid(theta, r)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    pc = ax.pcolormesh(T, R, M, cmap=sequential(hue='orange'), shading='auto')
    ax.set_yticklabels([]); ax.set_title(title)
    fig.colorbar(pc, ax=ax, shrink=0.7, label='value', pad=0.1)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
