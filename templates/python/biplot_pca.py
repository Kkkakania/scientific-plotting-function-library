"""biplot_pca: PCA 双标图（样本点 + 载荷向量）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='PCA biplot'):
    apply_theme(fig_size=(7, 6))
    rng = np.random.default_rng(4)
    n_feat = 6
    centers = rng.uniform(-2, 2, (3, n_feat))
    X = np.vstack([rng.normal(c, 0.7, (40, n_feat)) for c in centers])
    labels = np.repeat(np.arange(3), 40)
    Xc = X - X.mean(0)
    U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
    PC = U[:, :2] * S[:2]
    loadings = Vt[:2].T * S[:2] / np.sqrt(len(X))
    fig, ax = plt.subplots()
    for k in range(3):
        m = labels == k
        ax.scatter(PC[m, 0], PC[m, 1], s=30, color=cycle(k), alpha=0.7,
                   edgecolors='w', linewidth=0.4, label=f'class {k}')
    scale = PC.std() / loadings.std() * 1.2
    for i, lo in enumerate(loadings):
        ax.annotate('', xy=(lo[0]*scale, lo[1]*scale), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color='red', lw=1.2))
        ax.text(lo[0]*scale*1.1, lo[1]*scale*1.1, f'f{i+1}', color='red')
    ax.set_xlabel('PC1'); ax.set_ylabel('PC2'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
