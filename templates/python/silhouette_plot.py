"""silhouette_plot: 聚类轮廓系数图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from theme import apply_theme
from palette import cycle

def make_figure(title='Silhouette plot'):
    apply_theme(fig_size=(6, 5))
    rng = np.random.default_rng(2)
    centers = np.array([[0, 0], [4, 4], [-3, 4]])
    n_per = 50
    X = np.vstack([rng.normal(c, 0.9, (n_per, 2)) for c in centers])
    labels = np.repeat(np.arange(3), n_per)
    # 轮廓
    D = cdist(X, X)
    sils = np.zeros(len(X))
    for i in range(len(X)):
        same = labels == labels[i]; same[i] = False
        a = D[i, same].mean()
        b = min(D[i, labels == k].mean() for k in range(3) if k != labels[i])
        sils[i] = (b - a) / max(a, b)
    fig, ax = plt.subplots()
    y = 0
    for k in range(3):
        s_k = np.sort(sils[labels == k])
        y_pos = np.arange(y, y + len(s_k))
        ax.barh(y_pos, s_k, color=cycle(k), edgecolor='none')
        y += len(s_k) + 5
    ax.axvline(sils.mean(), color='red', linestyle='--', linewidth=0.8,
               label=f'avg = {sils.mean():.2f}')
    ax.set_xlabel('silhouette coefficient'); ax.set_yticks([])
    ax.set_title(title); ax.legend()
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
