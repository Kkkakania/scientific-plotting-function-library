"""tsne_scatter: 降维后散点（用 PCA 模拟，标记类别）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='2D embedding scatter'):
    apply_theme()
    rng = np.random.default_rng(3)
    centers = rng.uniform(-4, 4, (4, 8))
    X = np.vstack([rng.normal(c, 0.6, (60, 8)) for c in centers])
    labels = np.repeat(np.arange(4), 60)
    Xc = X - X.mean(0)
    _, _, V = np.linalg.svd(Xc, full_matrices=False)
    proj = Xc @ V[:2].T
    fig, ax = plt.subplots()
    for k in range(4):
        m = labels == k
        ax.scatter(proj[m, 0], proj[m, 1], s=30, color=cycle(k),
                   alpha=0.7, edgecolors='w', linewidth=0.4, label=f'class {k}')
    ax.set_xlabel('dim 1'); ax.set_ylabel('dim 2'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
