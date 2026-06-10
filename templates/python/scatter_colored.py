"""scatter_colored: 连续色映射第三维."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(x=None, y=None, c=None, title='Color-coded scatter'):
    apply_theme()
    if x is None:
        rng = np.random.default_rng(3)
        x = rng.normal(0, 1, 200); y = rng.normal(0, 1, 200); c = x**2 + y**2
    fig, ax = plt.subplots()
    sc = ax.scatter(x, y, c=c, cmap='viridis', s=30, alpha=0.85, edgecolors='w', linewidth=0.3)
    fig.colorbar(sc, ax=ax, label='value')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
