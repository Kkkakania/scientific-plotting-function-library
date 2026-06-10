"""bar_stacked: 堆积柱状（展示组成）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_groups

def make_figure(labels=None, V=None, series_names=None, title='Stacked bar'):
    apply_theme()
    if labels is None:
        labels, V = gen_groups(n_cat=5, n_series=4)
        series_names = [f'comp {i+1}' for i in range(4)]
    fig, ax = plt.subplots()
    bottom = np.zeros(len(labels))
    for i, row in enumerate(V):
        ax.bar(labels, row, bottom=bottom, color=cycle(i), label=series_names[i])
        bottom += row
    ax.set_ylabel('value'); ax.set_title(title)
    ax.legend(); ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
