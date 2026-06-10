"""compass_plot: 罗盘图（多个方向矢量）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Compass'):
    apply_theme(fig_size=(5.5, 5.5))
    rng = np.random.default_rng(22)
    n = 8
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    r = rng.uniform(0.4, 1.0, n)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    for i in range(n):
        ax.annotate('', xy=(theta[i], r[i]), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=cycle(i), lw=2))
    ax.set_rmax(1.0); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
