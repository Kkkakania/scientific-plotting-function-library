"""quiver_3d: 三维矢量场."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='3D quiver field'):
    apply_theme(fig_size=(6.5, 5))
    x, y, z = np.meshgrid(np.linspace(-2, 2, 6), np.linspace(-2, 2, 6), np.linspace(-2, 2, 6))
    u, v, w = -y, x, 0.3*z
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(x, y, z, u, v, w, length=0.3, normalize=True, color='#0072B2', alpha=0.7)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
