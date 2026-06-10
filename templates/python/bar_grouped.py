"""bar_grouped: 分组柱状（多系列并排）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_groups

def make_figure(labels=None, V=None, series_names=None, title='Grouped bar'):
    apply_theme()
    if labels is None:
        labels, V = gen_groups(n_cat=5, n_series=3)
        series_names = ['2023', '2024', '2025']
    x = np.arange(len(labels))
    w = 0.8 / V.shape[0]
    fig, ax = plt.subplots()
    for i, row in enumerate(V):
        ax.bar(x + (i - V.shape[0]/2 + 0.5)*w, row, w,
               color=cycle(i), label=series_names[i] if series_names else None)
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylabel('value'); ax.set_title(title)
    ax.legend(); ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
