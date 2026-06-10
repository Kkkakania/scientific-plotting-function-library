"""streamlines_colored: 流线按速度模值着色（CFD 报告常用）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Colored streamlines'):
    apply_theme(fig_size=(7, 5))
    Y, X = np.mgrid[-2:2:200j, -3:3:300j]
    U = 1 + 0.6*np.cos(X) - 0.3*Y
    V = -0.4*Y + 0.3*np.sin(X)
    speed = np.hypot(U, V)
    fig, ax = plt.subplots()
    strm = ax.streamplot(X, Y, U, V, color=speed, cmap='viridis',
                         linewidth=1.2, density=1.6)
    fig.colorbar(strm.lines, ax=ax, label='|U|')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title); ax.set_aspect('equal')
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
