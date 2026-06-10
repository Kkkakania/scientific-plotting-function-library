"""isosurface: 等值面（球面简化版，不依赖 skimage）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(level=1.2, title='Isosurface'):
    apply_theme(fig_size=(6.5, 5))
    u = np.linspace(0, 2*np.pi, 60)
    v = np.linspace(0, np.pi, 30)
    U, V = np.meshgrid(u, v)
    r = np.sqrt(level) * (1 + 0.15*np.sin(3*U)*np.sin(2*V))
    X = r*np.sin(V)*np.cos(U); Y = r*np.sin(V)*np.sin(U); Z = r*np.cos(V)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, alpha=0.85)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(f'{title} V = {level}')
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
