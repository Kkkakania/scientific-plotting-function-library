"""trisurf_3d: 非规则采样点的三角化曲面."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Triangulated surface'):
    apply_theme(fig_size=(6.5, 5))
    rng = np.random.default_rng(23)
    n = 200
    x = rng.uniform(-2, 2, n); y = rng.uniform(-2, 2, n)
    z = np.exp(-(x**2 + y**2)/2)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')
    fig.colorbar(surf, ax=ax, shrink=0.6, label='z')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
