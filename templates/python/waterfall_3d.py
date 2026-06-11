"""waterfall_3d: 三维瀑布图（多条谱线沿 y 轴堆叠演化）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from theme import apply_theme
from palette import sequential


def _spectra(n_curves=12, n_pts=160, seed=3):
    """合成一族随参数演化的双峰谱线."""
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 10, n_pts)
    curves = []
    for i in range(n_curves):
        c1 = 3.0 + 0.20 * i              # 峰 1 缓慢右移
        c2 = 7.0 - 0.12 * i              # 峰 2 缓慢左移
        a1 = 1.0 - 0.05 * i
        a2 = 0.3 + 0.06 * i
        z = (a1 * np.exp(-(x - c1) ** 2 / 0.5)
             + a2 * np.exp(-(x - c2) ** 2 / 0.9)
             + rng.uniform(0, 0.02, n_pts))
        curves.append(z)
    return x, np.array(curves)


def make_figure(x=None, Z=None, title='Waterfall plot'):
    apply_theme(fig_size=(6.5, 5))
    if x is None:
        x, Z = _spectra()
    n_curves = Z.shape[0]
    cmap = sequential('blue')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    zmin = 0.0
    for i in range(n_curves - 1, -1, -1):   # 从后往前画保证遮挡正确
        z = Z[i]
        verts = [list(zip(np.r_[x[0], x, x[-1]],
                          np.r_[zmin, z, zmin]))]
        shade = 0.3 + 0.6 * i / max(n_curves - 1, 1)
        poly = PolyCollection(verts, facecolor=cmap(shade),
                              edgecolor='none', alpha=0.9)
        ax.add_collection3d(poly, zs=i, zdir='y')
        ax.plot(x, np.full_like(x, i), z, color='0.25', lw=0.7)
    ax.set_xlim(x[0], x[-1]); ax.set_ylim(0, n_curves - 1)
    ax.set_zlim(zmin, Z.max() * 1.05)
    ax.set_xlabel('frequency'); ax.set_ylabel('series index')
    ax.set_zlabel('amplitude'); ax.set_title(title)
    ax.view_init(35, -65)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
