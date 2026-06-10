"""heatmap_categorical: 分类热力图（离散色块）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from theme import apply_theme
from palette import CATEGORICAL

def make_figure(title='Categorical heatmap'):
    apply_theme()
    rng = np.random.default_rng(5)
    M = rng.integers(0, 5, (8, 12))
    cmap = ListedColormap(CATEGORICAL[:5])
    norm = BoundaryNorm(np.arange(-0.5, 5.5, 1), cmap.N)
    fig, ax = plt.subplots()
    im = ax.imshow(M, cmap=cmap, norm=norm, aspect='auto')
    cb = fig.colorbar(im, ax=ax, ticks=range(5), shrink=0.7)
    cb.set_ticklabels([f'cat {i+1}' for i in range(5)])
    ax.set_xlabel('column'); ax.set_ylabel('row'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
