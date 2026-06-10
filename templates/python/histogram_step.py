"""histogram_step: 阶梯直方图（多组对比时比叠加更清晰）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(arrays=None, labels=None, bins=40, title='Step histogram'):
    apply_theme()
    if arrays is None:
        rng = np.random.default_rng(2)
        arrays = [rng.normal(0, 1, 1000), rng.normal(1.5, 1, 1000), rng.normal(-1, 0.8, 1000)]
        labels = ['A', 'B', 'C']
    fig, ax = plt.subplots()
    for i, arr in enumerate(arrays):
        ax.hist(arr, bins=bins, histtype='step', linewidth=1.5,
                color=cycle(i), label=labels[i])
    ax.set_xlabel('value'); ax.set_ylabel('count'); ax.set_title(title)
    ax.legend(); ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
