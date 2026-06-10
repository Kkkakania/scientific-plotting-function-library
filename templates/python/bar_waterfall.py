"""bar_waterfall: 瀑布图（贡献分解）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(labels=None, values=None, title='Waterfall'):
    apply_theme()
    if labels is None:
        labels = ['start', 'A', 'B', 'C', 'D', 'end']
        values = [50, 15, -8, 22, -10, 0]
    values = np.array(values, dtype=float)
    values[-1] = sum(values[:-1])
    cum = np.cumsum([0] + list(values[:-1]))
    fig, ax = plt.subplots()
    for i, (lab, v, c) in enumerate(zip(labels, values, cum)):
        if i == 0 or i == len(labels)-1:
            color = cycle(7)
            ax.bar(lab, v, color=color)
        else:
            color = cycle(0) if v > 0 else cycle(1)
            ax.bar(lab, v, bottom=c, color=color)
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
