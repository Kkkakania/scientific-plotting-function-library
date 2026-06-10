"""histogram_overlay: 多组直方图叠加."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(arrays=None, labels=None, bins=30, title='Overlayed histograms'):
    apply_theme()
    if arrays is None:
        rng = np.random.default_rng(0)
        arrays = [rng.normal(-1, 1, 500), rng.normal(1, 1.2, 500), rng.normal(0, 0.6, 500)]
        labels = ['A', 'B', 'C']
    fig, ax = plt.subplots()
    for i, arr in enumerate(arrays):
        ax.hist(arr, bins=bins, color=cycle(i), alpha=0.5,
                edgecolor='w', label=labels[i])
    ax.set_xlabel('value'); ax.set_ylabel('count'); ax.set_title(title)
    ax.legend(); ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
