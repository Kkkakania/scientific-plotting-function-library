"""line_with_markers: 带显著标记的折线（少量数据点时优先）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Line with markers'):
    apply_theme()
    x = np.arange(1, 13)
    fig, ax = plt.subplots()
    markers = ['o', 's', '^', 'D']
    for i, m in enumerate(markers):
        y = np.cumsum(np.random.default_rng(i).normal(0, 1, 12))
        ax.plot(x, y, marker=m, color=cycle(i), markersize=7,
                markerfacecolor='white', markeredgewidth=1.4, label=f'series {i+1}')
    ax.set_xlabel('month'); ax.set_ylabel('value'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
