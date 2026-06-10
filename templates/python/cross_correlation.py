"""cross_correlation: 互相关函数（识别滞后关系）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Cross-correlation'):
    apply_theme()
    rng = np.random.default_rng(24)
    n = 500
    x = rng.standard_normal(n)
    y = np.roll(x, 15) + 0.4*rng.standard_normal(n)
    x -= x.mean(); y -= y.mean()
    xc = np.correlate(y, x, mode='full') / (np.std(x)*np.std(y)*n)
    lags = np.arange(-n+1, n)
    fig, ax = plt.subplots()
    mask = (lags >= -50) & (lags <= 50)
    ax.stem(lags[mask], xc[mask], linefmt='-', markerfmt='o', basefmt=' ')
    ax.axvline(0, color='k', linewidth=0.5)
    ax.set_xlabel('lag'); ax.set_ylabel('xcorr'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
