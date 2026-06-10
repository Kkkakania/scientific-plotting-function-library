"""line_collection_3d: 3D 曲线族（多个 z 切片堆叠）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Stacked 3D curves'):
    apply_theme(fig_size=(7, 5))
    x = np.linspace(0, 10, 200)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i, k in enumerate(np.linspace(0.5, 2.0, 8)):
        y = np.sin(k*x)*np.exp(-x/8)
        ax.plot(x, np.full_like(x, i), y, color=plt.cm.plasma(i/8))
    ax.set_xlabel('x'); ax.set_ylabel('series'); ax.set_zlabel('y')
    ax.set_title(title); ax.view_init(30, -60)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
