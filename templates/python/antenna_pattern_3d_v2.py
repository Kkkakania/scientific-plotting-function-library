"""antenna_pattern_3d_v2: 平面阵阵列因子三维方向图（dB 球面，主瓣/旁瓣可见）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme


def _af(n, psi):
    num = np.sin(n * psi / 2)
    den = n * np.sin(psi / 2)
    out = np.where(np.abs(den) < 1e-9, 1.0, num / np.where(np.abs(den) < 1e-9, 1, den))
    return np.abs(out)


def make_figure(nx=8, ny=8, d=0.5, floor_db=-40,
                title='Planar array 3D pattern (8x8, d=0.5$\\lambda$)'):
    apply_theme(fig_size=(6.5, 5.2))
    theta = np.linspace(0, np.pi / 2, 121)
    phi = np.linspace(0, 2 * np.pi, 241)
    TH, PH = np.meshgrid(theta, phi)
    psix = 2 * np.pi * d * np.sin(TH) * np.cos(PH)
    psiy = 2 * np.pi * d * np.sin(TH) * np.sin(PH)
    af = _af(nx, psix) * _af(ny, psiy)
    db = 20 * np.log10(af + 1e-9)
    db = np.clip(db, floor_db, 0)
    r = db - floor_db
    X = r * np.sin(TH) * np.cos(PH)
    Y = r * np.sin(TH) * np.sin(PH)
    Z = r * np.cos(TH)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    cmap = plt.get_cmap('viridis')
    ax.plot_surface(X, Y, Z, facecolors=cmap((db - floor_db) / (-floor_db)),
                    rstride=1, cstride=1, linewidth=0, shade=False, antialiased=False)
    m = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(floor_db, 0))
    fig.colorbar(m, ax=ax, shrink=0.55, pad=0.08, label='normalized gain (dB)')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_box_aspect((1, 1, 0.65))
    ax.set_title(title)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
