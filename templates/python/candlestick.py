"""candlestick: 蜡烛图（OHLC 简化版，金融/电气负荷波动可用）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Candlestick'):
    apply_theme(fig_size=(8, 4))
    rng = np.random.default_rng(20)
    n = 30
    close = 100 + np.cumsum(rng.normal(0, 1, n))
    open_ = close + rng.normal(0, 1, n)
    high = np.maximum(open_, close) + rng.uniform(0, 1.5, n)
    low  = np.minimum(open_, close) - rng.uniform(0, 1.5, n)
    fig, ax = plt.subplots()
    for i in range(n):
        c = '#26A69A' if close[i] >= open_[i] else '#EF5350'
        ax.plot([i, i], [low[i], high[i]], color='k', linewidth=0.7)
        ax.add_patch(plt.Rectangle((i-0.3, min(open_[i], close[i])),
                                    0.6, abs(close[i] - open_[i]),
                                    color=c, alpha=0.85))
    ax.set_xlim(-1, n); ax.set_xlabel('day'); ax.set_ylabel('price'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
