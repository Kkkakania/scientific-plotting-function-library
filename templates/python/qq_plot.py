"""qq_plot: 正态性 Q-Q 图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from theme import apply_theme
from palette import cycle

def make_figure(data=None, title='Q-Q plot vs Normal'):
    apply_theme()
    if data is None:
        data = np.random.default_rng(5).normal(0, 1, 300)
    fig, ax = plt.subplots()
    stats.probplot(data, dist='norm', plot=ax)
    ax.get_lines()[0].set_color(cycle(0)); ax.get_lines()[0].set_markersize(4)
    ax.get_lines()[1].set_color('k');     ax.get_lines()[1].set_linewidth(1)
    ax.set_title(title); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
