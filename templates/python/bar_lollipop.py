"""bar_lollipop: 棒棒糖图（替代柱状，更轻盈）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(labels=None, values=None, title='Lollipop'):
    apply_theme()
    if labels is None:
        labels = [f'item {i+1}' for i in range(10)]
        values = np.random.default_rng(3).uniform(20, 90, 10)
    order = np.argsort(values)
    labels = [labels[i] for i in order]; values = values[order]
    y = np.arange(len(labels))
    fig, ax = plt.subplots()
    ax.hlines(y, 0, values, color=cycle(0), linewidth=1.5)
    ax.plot(values, y, 'o', color=cycle(0), markersize=8)
    ax.set_yticks(y); ax.set_yticklabels(labels)
    ax.set_xlabel('value'); ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
