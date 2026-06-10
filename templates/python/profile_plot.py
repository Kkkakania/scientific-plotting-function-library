"""profile_plot: 多组多指标剖面图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Profile plot'):
    apply_theme()
    metrics = ['speed', 'cost', 'noise', 'efficiency', 'durability']
    groups = ['A', 'B', 'C']
    rng = np.random.default_rng(2)
    M = rng.uniform(2, 9, (3, len(metrics)))
    fig, ax = plt.subplots()
    for i, g in enumerate(groups):
        ax.plot(metrics, M[i], '-o', color=cycle(i), label=g, markersize=7)
    ax.set_ylim(0, 10); ax.set_ylabel('score')
    ax.set_title(title); ax.legend()
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
