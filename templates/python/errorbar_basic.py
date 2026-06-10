"""errorbar_basic: 标准误差棒."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, y=None, yerr=None, title='Errorbar'):
    apply_theme()
    if x is None:
        rng = np.random.default_rng(0)
        x = np.arange(1, 11); y = 2 + np.log(x) + rng.normal(0, 0.1, 10)
        yerr = rng.uniform(0.1, 0.3, 10)
    fig, ax = plt.subplots()
    ax.errorbar(x, y, yerr=yerr, fmt='o-', capsize=4, color=cycle(0),
                ecolor='gray', markerfacecolor=cycle(0))
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
