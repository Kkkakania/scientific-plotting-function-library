"""line_step: 阶梯折线（适合离散事件/计数）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, y=None, title='Step plot'):
    apply_theme()
    if x is None:
        x = np.arange(20)
        y = np.cumsum(np.random.default_rng(0).standard_normal(20))
    fig, ax = plt.subplots()
    ax.step(x, y, where='post', color=cycle(0))
    ax.plot(x, y, 'o', color=cycle(0), markersize=4)
    ax.set_xlabel('t'); ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
