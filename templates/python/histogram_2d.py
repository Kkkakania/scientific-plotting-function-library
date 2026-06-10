"""histogram_2d: 二维直方图（替代密度散点）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(x=None, y=None, bins=40, title='2D histogram'):
    apply_theme()
    if x is None:
        rng = np.random.default_rng(1)
        x = rng.normal(0, 1, 5000); y = 0.6*x + rng.normal(0, 0.8, 5000)
    fig, ax = plt.subplots()
    h = ax.hist2d(x, y, bins=bins, cmap=sequential(hue='blue'))
    fig.colorbar(h[3], ax=ax, label='count')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
