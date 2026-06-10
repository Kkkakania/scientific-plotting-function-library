"""roc_curve: ROC 曲线 + AUC."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='ROC curves'):
    apply_theme()
    rng = np.random.default_rng(11)
    fig, ax = plt.subplots()
    for i, sep in enumerate([0.3, 1.0, 2.0]):
        pos = rng.normal(sep, 1, 300); neg = rng.normal(0, 1, 300)
        scores = np.concatenate([pos, neg])
        labels = np.concatenate([np.ones(300), np.zeros(300)])
        order = np.argsort(-scores); labels = labels[order]
        tpr = np.cumsum(labels) / labels.sum()
        fpr = np.cumsum(1 - labels) / (1 - labels).sum()
        auc = np.trapezoid(tpr, fpr)
        ax.plot(fpr, tpr, color=cycle(i), label=f'sep={sep} (AUC={auc:.3f})')
    ax.plot([0, 1], [0, 1], '--', color='gray', linewidth=0.8)
    ax.set_xlabel('FPR'); ax.set_ylabel('TPR'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
