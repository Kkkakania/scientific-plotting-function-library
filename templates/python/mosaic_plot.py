"""mosaic_plot: 马赛克图（列联表可视化）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Mosaic plot'):
    apply_theme(fig_size=(6.5, 5))
    M = np.array([[40, 20, 10], [25, 50, 25], [15, 30, 45]], dtype=float)
    rowS = M.sum(1); total = M.sum()
    fig, ax = plt.subplots()
    y0 = 0
    for i in range(3):
        h = rowS[i] / total
        x0 = 0
        for j in range(3):
            w = M[i, j] / rowS[i]
            ax.add_patch(plt.Rectangle((x0, y0), w, h, color=cycle(j), alpha=0.8, edgecolor='w'))
            ax.text(x0 + w/2, y0 + h/2, f'{int(M[i,j])}', ha='center', va='center', color='white')
            x0 += w
        y0 += h
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
