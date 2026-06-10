"""scatter_3d: 三维散点 + 颜色编码第四维."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(x=None, y=None, z=None, c=None, title='3D scatter'):
    apply_theme(fig_size=(6.5, 5))
    if x is None:
        rng = np.random.default_rng(0)
        n = 300
        x = rng.normal(0, 1, n); y = rng.normal(0, 1, n); z = rng.normal(0, 1, n)
        c = x**2 + y**2 + z**2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(x, y, z, c=c, cmap='plasma', s=25, alpha=0.85,
                    edgecolor='w', linewidth=0.3)
    fig.colorbar(sc, ax=ax, shrink=0.6, label='value')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
