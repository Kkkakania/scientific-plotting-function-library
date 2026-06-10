"""autocorrelation: 自相关函数 ACF."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(y=None, max_lag=40, title='Autocorrelation'):
    apply_theme()
    if y is None:
        rng = np.random.default_rng(1)
        n = 500; y = np.zeros(n)
        for i in range(1, n):
            y[i] = 0.7*y[i-1] + rng.standard_normal()
    y = y - y.mean()
    n = len(y)
    acf = [np.dot(y[:n-k], y[k:]) / np.dot(y, y) for k in range(max_lag+1)]
    ci = 1.96 / np.sqrt(n)
    fig, ax = plt.subplots()
    ax.stem(range(max_lag+1), acf, linefmt='-', markerfmt='o', basefmt=' ')
    ax.axhline( ci, color='gray', linestyle='--', linewidth=0.7)
    ax.axhline(-ci, color='gray', linestyle='--', linewidth=0.7)
    ax.set_xlabel('lag'); ax.set_ylabel('ACF'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
