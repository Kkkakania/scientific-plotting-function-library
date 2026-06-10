"""wireframe_3d: 线框 + 底面投影等高线."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from demo_data import gen_3d_surface

def make_figure(X=None, Y=None, Z=None, title='Wireframe + projection'):
    apply_theme(fig_size=(6.5, 5))
    if X is None:
        X, Y, Z = gen_3d_surface(n=40)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(X, Y, Z, color='#0072B2', linewidth=0.5)
    ax.contour(X, Y, Z, zdir='z', offset=Z.min()-1, cmap='RdBu_r')
    ax.set_zlim(Z.min()-1, Z.max())
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
