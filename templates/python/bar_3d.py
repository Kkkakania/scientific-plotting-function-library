"""bar_3d: 三维柱状（categories × series 矩阵）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(M=None, title='3D bar'):
    apply_theme(fig_size=(6.5, 5))
    if M is None:
        rng = np.random.default_rng(1)
        M = rng.uniform(1, 8, (5, 6))
    n_rows, n_cols = M.shape
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(n_rows):
        xs = np.arange(n_cols)
        ys = np.full(n_cols, i)
        zs = np.zeros(n_cols)
        ax.bar3d(xs, ys, zs, 0.7, 0.7, M[i], color=cycle(i), shade=True, alpha=0.9)
    ax.set_xlabel('column'); ax.set_ylabel('row'); ax.set_zlabel('value')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
