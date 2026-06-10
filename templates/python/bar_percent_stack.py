"""bar_percent_stack: 100% 堆叠柱状（占比对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='100% stacked bar'):
    apply_theme()
    labels = [f'group {i+1}' for i in range(5)]
    V = np.random.default_rng(3).uniform(10, 50, (4, 5))
    V_pct = V / V.sum(axis=0) * 100
    fig, ax = plt.subplots()
    bottom = np.zeros(5)
    for i, row in enumerate(V_pct):
        ax.bar(labels, row, bottom=bottom, color=cycle(i), label=f'comp {i+1}')
        bottom += row
    ax.set_ylabel('percentage (%)'); ax.set_title(title)
    ax.set_ylim(0, 100); ax.legend()
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
