"""lag_plot_v2: 滞后散点图阵（lag = 1..4 四宫格，识别自相关衰减）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Lag plot matrix'):
    apply_theme(fig_size=(6, 5.5))
    rng = np.random.default_rng(12)
    n = 400
    y = np.zeros(n)
    for i in range(1, n):
        y[i] = 0.75 * y[i-1] + rng.standard_normal()
    fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
    for k, ax in enumerate(axes.ravel(), start=1):
        ax.scatter(y[:-k], y[k:], s=8, color=cycle(0), alpha=0.5,
                   edgecolors='none')
        rho = np.corrcoef(y[:-k], y[k:])[0, 1]
        ax.text(0.05, 0.92, f'lag={k}, r={rho:.2f}', transform=ax.transAxes,
                fontsize=8, color=cycle(1))
        ax.grid(True, linestyle=':', alpha=0.5)
    for ax in axes[1]:
        ax.set_xlabel('y(t)')
    for ax in axes[:, 0]:
        ax.set_ylabel('y(t+k)')
    fig.suptitle(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
