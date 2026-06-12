"""candlestick_ohlc: K 线图（合成随机游走 OHLC + 成交量副图，涨绿跌红）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='OHLC candlestick'):
    apply_theme(fig_size=(8, 4.5))
    rng = np.random.default_rng(7)
    n = 60
    drift = rng.normal(0.05, 1.2, n)
    close = 100 + np.cumsum(drift)
    open_ = np.concatenate(([100.0], close[:-1])) + rng.normal(0, 0.3, n)
    high = np.maximum(open_, close) + rng.uniform(0.2, 1.8, n)
    low = np.minimum(open_, close) - rng.uniform(0.2, 1.8, n)
    vol = rng.uniform(0.4, 1.0, n) * (1 + np.abs(drift))
    x = np.arange(n)
    up = close >= open_
    fig, (ax, axv) = plt.subplots(2, 1, sharex=True,
                                  gridspec_kw={'height_ratios': [3, 1]})
    ax.vlines(x, low, high, color='#666666', linewidth=0.7)
    for mask, c in [(up, cycle(2)), (~up, cycle(1))]:
        ax.bar(x[mask], (close - open_)[mask], bottom=open_[mask],
               width=0.6, color=c)
        axv.bar(x[mask], vol[mask], width=0.6, color=c, alpha=0.6)
    ax.set_ylabel('price'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    axv.set_xlabel('trading day'); axv.set_ylabel('volume')
    axv.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
