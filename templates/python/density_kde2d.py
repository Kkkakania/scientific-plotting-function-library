"""density_kde2d: 二维核密度等高线（轮廓型分布展示）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from theme import apply_theme
from palette import sequential

def make_figure(x=None, y=None, title='2D KDE contour'):
    apply_theme()
    if x is None:
        rng = np.random.default_rng(0)
        x = rng.normal(0, 1, 1500); y = 0.5*x + rng.normal(0, 0.7, 1500)
    xs = np.linspace(x.min(), x.max(), 100)
    ys = np.linspace(y.min(), y.max(), 100)
    XX, YY = np.meshgrid(xs, ys)
    ZZ = gaussian_kde(np.vstack([x, y]))(np.vstack([XX.ravel(), YY.ravel()])).reshape(XX.shape)
    fig, ax = plt.subplots()
    cf = ax.contourf(XX, YY, ZZ, levels=12, cmap=sequential(hue='purple'))
    ax.scatter(x, y, s=2, c='k', alpha=0.2)
    fig.colorbar(cf, ax=ax, label='density')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
