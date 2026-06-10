"""dot_plot_grouped: 分组点图（替代柱状，多组共比较）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(labels=None, V=None, series_names=None, title='Grouped dot plot'):
    apply_theme()
    if labels is None:
        labels = [f'item {i+1}' for i in range(8)]
        rng = np.random.default_rng(2)
        V = rng.uniform(20, 80, (3, 8))
        series_names = ['Q1', 'Q2', 'Q3']
    y = np.arange(len(labels))
    fig, ax = plt.subplots()
    for i, row in enumerate(V):
        ax.plot(row, y, 'o', color=cycle(i), markersize=8, label=series_names[i])
    ax.set_yticks(y); ax.set_yticklabels(labels)
    ax.set_xlabel('value'); ax.set_title(title)
    ax.legend(); ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
