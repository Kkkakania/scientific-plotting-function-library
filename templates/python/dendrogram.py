"""dendrogram: 层次聚类树状图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram as _dendro
from theme import apply_theme

def make_figure(title='Hierarchical dendrogram'):
    apply_theme(fig_size=(7, 4))
    rng = np.random.default_rng(14)
    X = rng.normal(0, 1, (15, 6))
    Z = linkage(X, method='ward')
    fig, ax = plt.subplots()
    _dendro(Z, ax=ax, leaf_font_size=8, color_threshold=0.5*max(Z[:, 2]))
    ax.set_ylabel('distance'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
