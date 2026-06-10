"""histogram_log: 对数分箱直方图（跨度大时用）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Log-bin histogram'):
    apply_theme()
    data = np.random.default_rng(9).pareto(1.5, 5000) + 1
    bins = np.logspace(0, np.log10(data.max()), 40)
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, color=cycle(0), edgecolor='w')
    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_xlabel('value (log)'); ax.set_ylabel('count (log)'); ax.set_title(title)
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
