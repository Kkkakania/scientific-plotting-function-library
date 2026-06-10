"""lyapunov_surface: Lyapunov 函数 V(x) 三维曲面."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Lyapunov surface V(x)'):
    apply_theme(fig_size=(6.5, 5))
    X, Y = np.meshgrid(np.linspace(-2, 2, 50), np.linspace(-2, 2, 50))
    V = X**2 + 0.5*X*Y + Y**2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, V, cmap='plasma', alpha=0.85, linewidth=0)
    ax.contour(X, Y, V, zdir='z', offset=0, cmap='plasma', alpha=0.4)
    fig.colorbar(surf, ax=ax, shrink=0.6, label='V')
    ax.set_xlabel('x₁'); ax.set_ylabel('x₂'); ax.set_zlabel('V')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
