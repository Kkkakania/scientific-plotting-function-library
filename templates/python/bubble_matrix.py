"""bubble_matrix: 矩阵 + 气泡大小（代替热力图，离散值更清晰）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential
from demo_data import gen_matrix

def make_figure(M=None, title='Bubble matrix'):
    apply_theme()
    if M is None:
        M = gen_matrix(rows=8, cols=8)
    fig, ax = plt.subplots()
    Y, X = np.indices(M.shape)
    sizes = (M / M.max()) * 600
    sc = ax.scatter(X.ravel(), Y.ravel(), s=sizes.ravel(), c=M.ravel(),
                    cmap=sequential(hue='blue'), alpha=0.85, edgecolors='w', linewidth=0.5)
    fig.colorbar(sc, ax=ax, label='value')
    ax.invert_yaxis()
    ax.set_xticks(range(M.shape[1])); ax.set_yticks(range(M.shape[0]))
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
