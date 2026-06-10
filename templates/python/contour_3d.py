"""contour_3d: 三维等高线（层叠 isoline）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from demo_data import gen_3d_surface

def make_figure(title='3D contour'):
    apply_theme(fig_size=(6.5, 5))
    X, Y, Z = gen_3d_surface(n=80)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.contour3D(X, Y, Z, 40, cmap='viridis')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title); ax.view_init(30, 60)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
