"""scatter_sized: 气泡图，第三维用大小编码."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, y=None, size=None, title='Bubble chart'):
    apply_theme()
    if x is None:
        rng = np.random.default_rng(2)
        x = rng.uniform(0, 10, 50); y = rng.uniform(0, 10, 50); size = rng.uniform(20, 400, 50)
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=size, c=cycle(2), alpha=0.5, edgecolors='k', linewidth=0.4)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
