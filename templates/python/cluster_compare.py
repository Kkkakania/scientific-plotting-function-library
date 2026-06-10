"""cluster_compare: 同一数据多种聚类算法可视化对比."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster
from theme import apply_theme
from palette import cycle

def make_figure(title='Clustering comparison'):
    apply_theme(fig_size=(9, 3.5))
    rng = np.random.default_rng(8)
    n = 80
    X = np.vstack([rng.normal((0, 0), 0.6, (n, 2)),
                   rng.normal((3, 3), 0.6, (n, 2)),
                   rng.normal((-3, 3), 0.6, (n, 2))])
    fig, axes = plt.subplots(1, 3)
    # KMeans-ish: distance to 3 random centers, assigned by min
    centers = rng.uniform(-3, 3, (3, 2))
    for _ in range(10):
        d = np.linalg.norm(X[:, None] - centers[None], axis=2)
        lab = d.argmin(1)
        centers = np.array([X[lab == k].mean(0) for k in range(3)])
    # hierarchical
    Z = linkage(X, method='ward'); lab_h = fcluster(Z, 3, criterion='maxclust') - 1
    # spectral-ish: just plot truth
    truth = np.repeat(np.arange(3), n)
    for ax, lab, name in zip(axes, [truth, lab, lab_h],
                              ['Truth', 'K-Means', 'Hierarchical']):
        for k in range(3):
            m = lab == k
            ax.scatter(X[m, 0], X[m, 1], s=15, color=cycle(k), alpha=0.7)
        ax.set_title(name); ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
