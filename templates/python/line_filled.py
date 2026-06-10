"""line_filled: 曲线+下方填充（强调累计/区域）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, y=None, title='Filled line'):
    apply_theme()
    if x is None:
        x = np.linspace(0, 10, 200)
        y = np.exp(-x/4) * np.sin(2*x) + 1
    fig, ax = plt.subplots()
    ax.fill_between(x, 0, y, color=cycle(0), alpha=0.3)
    ax.plot(x, y, color=cycle(0))
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
