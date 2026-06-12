"""roc_multi_compare: 多模型 ROC 对比（4 模型 + AUC 图例 + 随机猜测对角线）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def _roc(y, score):
    order = np.argsort(-score)
    ys = y[order]
    tpr = np.concatenate([[0], np.cumsum(ys) / ys.sum()])
    fpr = np.concatenate([[0], np.cumsum(1 - ys) / (len(ys) - ys.sum())])
    auc = np.trapezoid(tpr, fpr)
    return fpr, tpr, auc

def make_figure(title='ROC comparison'):
    apply_theme()
    rng = np.random.default_rng(11)
    n = 400
    y = (np.arange(n) < n // 2).astype(float)
    models = [('Model A', 2.0), ('Model B', 1.4), ('Model C', 0.9), ('Model D', 0.45)]
    fig, ax = plt.subplots(figsize=(5, 4.6))
    for i, (name, sep) in enumerate(models):
        score = rng.normal(0, 1, n) + sep * y
        fpr, tpr, auc = _roc(y, score)
        ax.plot(fpr, tpr, color=cycle(i), label=f'{name} (AUC = {auc:.3f})')
    ax.plot([0, 1], [0, 1], '--', color='gray', linewidth=0.8, label='chance')
    ax.set_xlim(-0.02, 1.02); ax.set_ylim(-0.02, 1.02)
    ax.set_xlabel('false positive rate'); ax.set_ylabel('true positive rate')
    ax.set_title(title)
    ax.legend(loc='lower right')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
