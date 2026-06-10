"""multiclass_roc: 多类 ROC（one-vs-rest）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Multi-class ROC (OvR)'):
    apply_theme()
    rng = np.random.default_rng(4)
    n_per = 200
    n_class = 4
    scores = np.zeros((n_class*n_per, n_class))
    labels = np.repeat(np.arange(n_class), n_per)
    for k in range(n_class):
        for j in range(n_class):
            mu = 1.5 if j == k else 0
            scores[labels == k, j] = rng.normal(mu, 1, n_per)
    fig, ax = plt.subplots()
    for k in range(n_class):
        y = (labels == k).astype(int)
        sc = scores[:, k]
        order = np.argsort(-sc); y = y[order]
        tpr = np.cumsum(y) / y.sum()
        fpr = np.cumsum(1 - y) / (1 - y).sum()
        auc = np.trapezoid(tpr, fpr)
        ax.plot(fpr, tpr, color=cycle(k), label=f'class {k} (AUC={auc:.3f})')
    ax.plot([0, 1], [0, 1], '--', color='gray', linewidth=0.7)
    ax.set_xlabel('FPR'); ax.set_ylabel('TPR'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
