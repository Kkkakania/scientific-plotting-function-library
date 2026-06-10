"""confusion_per_class: 每类精度/召回率柱状图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Per-class metrics'):
    apply_theme()
    classes = [f'cls {i+1}' for i in range(8)]
    rng = np.random.default_rng(9)
    precision = 0.6 + 0.35*rng.uniform(0, 1, 8)
    recall    = 0.6 + 0.35*rng.uniform(0, 1, 8)
    f1 = 2*precision*recall / (precision + recall)
    x = np.arange(len(classes)); w = 0.27
    fig, ax = plt.subplots()
    ax.bar(x - w, precision, w, color=cycle(0), label='precision')
    ax.bar(x,     recall,    w, color=cycle(1), label='recall')
    ax.bar(x + w, f1,        w, color=cycle(2), label='F1')
    ax.set_xticks(x); ax.set_xticklabels(classes)
    ax.set_ylabel('score'); ax.set_ylim(0, 1)
    ax.set_title(title); ax.legend()
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
