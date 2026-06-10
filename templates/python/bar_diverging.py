"""bar_diverging: 发散柱状（正负对比，tornado chart）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(labels=None, values=None, title='Diverging bar'):
    apply_theme()
    if labels is None:
        labels = [f'factor {i+1}' for i in range(10)]
        values = np.random.default_rng(2).uniform(-5, 5, 10)
    order = np.argsort(values)
    labels = [labels[i] for i in order]; values = values[order]
    colors = [cycle(1) if v < 0 else cycle(0) for v in values]
    fig, ax = plt.subplots()
    ax.barh(labels, values, color=colors)
    ax.axvline(0, color='k', linewidth=0.6)
    ax.set_xlabel('effect'); ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
