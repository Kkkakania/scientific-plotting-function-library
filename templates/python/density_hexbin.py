"""density_hexbin: 六边形分箱密度图（适合海量散点）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(x=None, y=None, gridsize=30, title='Hexbin'):
    apply_theme()
    if x is None:
        rng = np.random.default_rng(1)
        x = rng.normal(0, 1, 10000); y = 0.7*x + rng.normal(0, 0.6, 10000)
    fig, ax = plt.subplots()
    hb = ax.hexbin(x, y, gridsize=gridsize, cmap=sequential(hue='blue'), mincnt=1)
    fig.colorbar(hb, ax=ax, label='count')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
