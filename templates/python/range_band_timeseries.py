"""range_band_timeseries: 多年同期范围带（历史 min-max 带 + 均值 + 今年线）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='This year vs historical range'):
    apply_theme(fig_size=(7, 4))
    rng = np.random.default_rng(22)
    weeks = np.arange(1, 53)
    season = 18 + 9 * np.sin((weeks - 12) * 2 * np.pi / 52)
    hist = season + rng.normal(0, 2.0, (9, 52))       # 9 个历史年份
    hist += rng.normal(0, 1.2, (9, 1))                # 年际整体偏移
    now_w = 23                                        # 今年进行到第 23 周
    this_year = season[:now_w] + 2.5 + rng.normal(0, 1.0, now_w)
    fig, ax = plt.subplots()
    ax.fill_between(weeks, hist.min(axis=0), hist.max(axis=0),
                    color=cycle(0), alpha=0.18, label='historical min-max')
    ax.plot(weeks, hist.mean(axis=0), color=cycle(0), linewidth=1.4,
            linestyle='--', label='historical mean')
    ax.plot(weeks[:now_w], this_year, color=cycle(1), linewidth=2,
            label='current year')
    ax.plot(now_w, this_year[-1], 'o', color=cycle(1), markersize=5)
    ax.annotate('latest', (now_w, this_year[-1]),
                textcoords='offset points', xytext=(6, 4), fontsize=8)
    ax.set_xlabel('week of year'); ax.set_ylabel('temperature (°C)')
    ax.set_title(title)
    ax.legend(frameon=False, loc='upper left', fontsize=8)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
