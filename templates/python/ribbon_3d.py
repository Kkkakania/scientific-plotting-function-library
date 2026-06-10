"""ribbon_3d: 多条 3D 条带（多曲线时间演化）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from theme import apply_theme
from palette import cycle

def make_figure(title='3D ribbons'):
    apply_theme(fig_size=(6.5, 5))
    x = np.linspace(0, 10, 80)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    width = 0.3
    for i in range(5):
        z = np.sin(x + i*0.6) * np.exp(-x/8)
        verts = []
        for j in range(len(x)-1):
            verts.append([
                (x[j],   i - width, z[j]),
                (x[j+1], i - width, z[j+1]),
                (x[j+1], i + width, z[j+1]),
                (x[j],   i + width, z[j]),
            ])
        poly = Poly3DCollection(verts, facecolor=cycle(i), edgecolor='none', alpha=0.85)
        ax.add_collection3d(poly)
    ax.set_xlim(0, 10); ax.set_ylim(-1, 5); ax.set_zlim(-1, 1.2)
    ax.set_xlabel('x'); ax.set_ylabel('series'); ax.set_zlabel('z')
    ax.set_title(title); ax.view_init(30, -60)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
