"""event_raster: 事件栅格图（多通道事件 raster，神经放电/告警日志通用）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Event raster'):
    apply_theme(fig_size=(7, 4))
    rng = np.random.default_rng(16)
    n_ch, T = 8, 60.0
    rates = rng.uniform(0.3, 2.0, n_ch)          # 每通道事件率（次/s）
    events, colors = [], []
    for ch in range(n_ch):
        gaps = rng.exponential(1 / rates[ch], int(rates[ch] * T * 2) + 10)
        tt = np.cumsum(gaps)
        events.append(tt[tt < T])
        colors.append(cycle(ch))
    fig, ax = plt.subplots()
    ax.eventplot(events, colors=colors, lineoffsets=np.arange(n_ch),
                 linelengths=0.7, linewidths=1.0)
    ax.set_yticks(np.arange(n_ch))
    ax.set_yticklabels([f'ch {c+1}' for c in range(n_ch)])
    ax.set_xlabel('time (s)'); ax.set_ylabel('channel')
    ax.set_title(title)
    ax.set_xlim(0, T)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
