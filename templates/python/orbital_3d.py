"""orbital_3d: 球谐函数 Re(Y_lm) 极坐标渲染（教学用）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(l=3, m=2, title='Spherical harmonic'):
    apply_theme(fig_size=(6.5, 5))
    theta = np.linspace(0, np.pi, 80)
    phi = np.linspace(0, 2*np.pi, 80)
    THETA, PHI = np.meshgrid(theta, phi)
    try:
        from scipy.special import sph_harm_y
        Y = sph_harm_y(l, m, THETA, PHI)
    except (ImportError, TypeError):
        from scipy.special import sph_harm
        Y = sph_harm(m, l, PHI, THETA)
    R = np.abs(Y)
    X = R*np.sin(THETA)*np.cos(PHI)
    Y_ = R*np.sin(THETA)*np.sin(PHI)
    Z = R*np.cos(THETA)
    real_Y = np.real(Y)
    span = np.ptp(real_Y) + 1e-9
    colors = plt.cm.RdBu_r((real_Y - real_Y.min())/span)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y_, Z, facecolors=colors, linewidth=0)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(f'{title} l={l}, m={m}')
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
