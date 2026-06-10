"""lag_plot: y(t) vs y(t-k) 滞后散点（识别自相关结构）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(lag=1, title='Lag plot'):
    apply_theme()
    rng = np.random.default_rng(18)
    n = 500; y = np.zeros(n)
    for i in range(1, n):
        y[i] = 0.8*y[i-1] + rng.standard_normal()
    fig, ax = plt.subplots()
    ax.scatter(y[:-lag], y[lag:], s=15, c=cycle(0), alpha=0.6, edgecolors='none')
    ax.set_xlabel(f'y(t)'); ax.set_ylabel(f'y(t+{lag})')
    ax.set_title(f'{title} (lag = {lag})')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
