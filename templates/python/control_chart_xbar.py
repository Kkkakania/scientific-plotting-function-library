"""control_chart_xbar: X̄-R 控制图（均值图 + 极差图，UCL/LCL 越限点标红）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='X-bar / R control chart'):
    apply_theme(fig_size=(7, 5))
    rng = np.random.default_rng(4)
    n_grp, n_sub = 25, 5                       # 25 个子组，每组 5 个样本
    X = rng.normal(10, 1, (n_grp, n_sub))
    X[19:] += 1.6                              # 注入均值漂移
    xbar = X.mean(axis=1)
    R = X.max(axis=1) - X.min(axis=1)
    A2, D3, D4 = 0.577, 0.0, 2.114             # n=5 的控制图系数
    xbb, rbar = xbar.mean(), R.mean()
    lim_x = (xbb - A2 * rbar, xbb + A2 * rbar)
    lim_r = (D3 * rbar, D4 * rbar)
    g = np.arange(1, n_grp + 1)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    for ax, v, lim, center, name in [
            (ax1, xbar, lim_x, xbb, 'subgroup mean'),
            (ax2, R, lim_r, rbar, 'subgroup range')]:
        ax.plot(g, v, '-o', color=cycle(0), markersize=4)
        ax.axhline(center, color=cycle(2), linewidth=1.2, label='center line')
        for L in lim:
            ax.axhline(L, color=cycle(7), linestyle='--', linewidth=1)
        out = (v > lim[1]) | (v < lim[0])
        ax.plot(g[out], v[out], 'o', color=cycle(1), markersize=6,
                label='out of control')
        ax.set_ylabel(name)
        ax.grid(True, linestyle=':', alpha=0.5)
    ax1.set_title(title)
    ax1.legend(frameon=False, loc='upper left', fontsize=7)
    ax2.set_xlabel('subgroup number')
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
