"""antenna_pattern_3d: 三维方向图（球面渲染）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='3D antenna pattern'):
    apply_theme(fig_size=(6.5, 5))
    phi   = np.linspace(0, 2*np.pi, 100)
    theta = np.linspace(0, np.pi,   60)
    PHI, THETA = np.meshgrid(phi, theta)
    R = np.abs(np.cos(THETA))**2 * np.abs(np.sin(2*PHI))
    X = R*np.sin(THETA)*np.cos(PHI)
    Y = R*np.sin(THETA)*np.sin(PHI)
    Z = R*np.cos(THETA)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='plasma', linewidth=0)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
