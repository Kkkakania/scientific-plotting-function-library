"""scatter_density: 高密度散点用 KDE 着色."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from theme import apply_theme

def make_figure(x=None, y=None, title='Density scatter'):
    apply_theme()
    if x is None:
        rng = np.random.default_rng(4)
        x = rng.normal(0, 1, 2000); y = x*0.6 + rng.normal(0, 0.8, 2000)
    xy = np.vstack([x, y])
    z = gaussian_kde(xy)(xy)
    idx = z.argsort()
    fig, ax = plt.subplots()
    sc = ax.scatter(x[idx], y[idx], c=z[idx], cmap='magma', s=8, edgecolors='none')
    fig.colorbar(sc, ax=ax, label='density')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
