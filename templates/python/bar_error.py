"""bar_error: 柱状 + 误差棒."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Bar with error'):
    apply_theme()
    labels = list('ABCDE'); rng = np.random.default_rng(2)
    means = rng.uniform(30, 80, 5); err = rng.uniform(3, 10, 5)
    fig, ax = plt.subplots()
    ax.bar(labels, means, yerr=err, color=cycle(0),
           error_kw=dict(ecolor='black', capsize=4, capthick=1))
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
