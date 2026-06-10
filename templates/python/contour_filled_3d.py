"""contour_filled_3d: 3D 填充等高线 + 曲面."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from demo_data import gen_3d_surface

def make_figure(title='3D filled contour'):
    apply_theme(fig_size=(6.5, 5))
    X, Y, Z = gen_3d_surface(n=60, kind='sinc')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.contourf(X, Y, Z, zdir='z', offset=Z.min()-0.5, levels=15, cmap='viridis')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5, linewidth=0)
    ax.set_zlim(Z.min()-0.5, Z.max())
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
