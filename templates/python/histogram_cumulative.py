"""histogram_cumulative: 累积直方图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Cumulative histogram'):
    apply_theme()
    data = np.random.default_rng(8).normal(0, 1, 1000)
    fig, ax = plt.subplots()
    ax.hist(data, bins=50, cumulative=True, density=True,
            histtype='step', color=cycle(0), linewidth=1.5)
    ax.set_xlabel('value'); ax.set_ylabel('cumulative P'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
