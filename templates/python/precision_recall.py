"""precision_recall: PR 曲线 + AP."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Precision-Recall curve'):
    apply_theme()
    rng = np.random.default_rng(1)
    fig, ax = plt.subplots()
    for i, sep in enumerate([0.3, 1.0, 2.0]):
        pos = rng.normal(sep, 1, 300); neg = rng.normal(0, 1, 700)
        scores = np.concatenate([pos, neg])
        y = np.concatenate([np.ones(300), np.zeros(700)])
        order = np.argsort(-scores); y = y[order]
        tp = np.cumsum(y); fp = np.cumsum(1 - y)
        precision = tp / (tp + fp); recall = tp / y.sum()
        ap = np.sum(np.diff(np.concatenate([[0], recall])) * precision)
        ax.plot(recall, precision, color=cycle(i), label=f'sep={sep} (AP={ap:.3f})')
    ax.set_xlabel('recall'); ax.set_ylabel('precision'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
