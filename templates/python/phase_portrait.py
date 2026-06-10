"""phase_portrait: 非线性系统相图（含矢量场）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Phase portrait'):
    apply_theme(fig_size=(6, 5))
    Y, X = np.mgrid[-3:3:30j, -3:3:30j]
    U = Y
    V = -np.sin(X) - 0.2*Y
    fig, ax = plt.subplots()
    ax.streamplot(X, Y, U, V, color=np.hypot(U, V), cmap='viridis', density=1.4, linewidth=0.8)
    ax.set_xlabel('x'); ax.set_ylabel('dx/dt')
    ax.set_title(title); ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
