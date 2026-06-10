"""surface_3d: 三维曲面."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from demo_data import gen_3d_surface

def make_figure(X=None, Y=None, Z=None, title='3D surface'):
    apply_theme(fig_size=(6.5, 5))
    if X is None:
        X, Y, Z = gen_3d_surface(n=60, kind='sinc')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0)
    fig.colorbar(surf, ax=ax, shrink=0.6, label='z')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
