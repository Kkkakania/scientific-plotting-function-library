"""pie_donut: 环形图（饼图变体，中心留白放合计标注）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(values=None, labels=None, title='Energy mix share'):
    apply_theme(fig_size=(5, 4.2))
    if values is None:
        rng = np.random.default_rng(0)
        labels = ['Coal', 'Gas', 'Hydro', 'Wind', 'Solar', 'Nuclear']
        values = np.array([34., 22., 14., 12., 8., 10.]) + rng.uniform(-1, 1, 6)
    values = np.asarray(values, dtype=float)
    colors = [cycle(i) for i in range(len(values))]
    fig, ax = plt.subplots()
    wedges, _, autotexts = ax.pie(
        values, labels=labels, colors=colors, startangle=90,
        counterclock=False, autopct='%1.1f%%', pctdistance=0.78,
        wedgeprops={'width': 0.42, 'edgecolor': 'white', 'linewidth': 1.2},
        textprops={'fontsize': 8})
    for t in autotexts:
        t.set_color('white'); t.set_fontsize(7)
    ax.text(0, 0, f'total\n{values.sum():.0f}', ha='center', va='center', fontsize=9)
    ax.set_title(title)
    ax.set_aspect('equal')
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
