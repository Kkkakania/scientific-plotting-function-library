"""horizon_chart: 地平线图（单变量分层折叠填色，4 序列小多图）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(n_bands=2, title='Horizon chart'):
    apply_theme(fig_size=(8, 3.6))
    rng = np.random.default_rng(5)
    n, n_series = 400, 4
    x = np.arange(n)
    Y = np.cumsum(rng.normal(0, 1, (n_series, n)), axis=1)
    Y -= Y.mean(axis=1, keepdims=True)
    fig, axes = plt.subplots(n_series, 1, sharex=True)
    for s, ax in enumerate(axes):
        y = Y[s]
        h = np.abs(y).max() / n_bands            # 每层带宽
        for k in range(n_bands):
            pos = np.clip(np.clip(y, 0, None) - k * h, 0, h)
            neg = np.clip(np.clip(-y, 0, None) - k * h, 0, h)
            a = 0.35 + 0.5 * k / max(n_bands - 1, 1)
            ax.fill_between(x, 0, pos, color=cycle(0), alpha=a, linewidth=0)
            ax.fill_between(x, 0, neg, color=cycle(1), alpha=a, linewidth=0)
        ax.set_ylim(0, h); ax.set_yticks([])
        ax.set_ylabel(f'S{s+1}', rotation=0, ha='right', va='center')
    axes[0].set_title(title)
    axes[-1].set_xlabel('time (sample)')
    fig.tight_layout(h_pad=0.3)
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
