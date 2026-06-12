"""anomaly_timeline: 异常事件时间线（序列 + 异常区间底色 + 事件标记）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Anomaly timeline'):
    apply_theme(fig_size=(8, 4))
    rng = np.random.default_rng(13)
    n = 300
    t = np.arange(n)
    y = 10 + 2 * np.sin(2 * np.pi * t / 50) + rng.normal(0, 0.4, n)
    spans = [(80, 95), (160, 172), (238, 252)]   # 异常区间
    y[80:95] += 3.0                              # 水平漂移
    y[160:172] += rng.normal(0, 2.0, 12)         # 方差爆炸
    y[238:252] -= np.linspace(0, 4, 14)          # 斜坡跌落
    mask = np.zeros(n, bool)
    for a, b in spans:
        mask[a:b] = True
    fig, ax = plt.subplots()
    for i, (a, b) in enumerate(spans):
        ax.axvspan(a, b, color=cycle(1), alpha=0.15,
                   label='anomaly window' if i == 0 else None)
        ax.text((a + b) / 2, ax.get_ylim()[1], f'E{i+1}', ha='center',
                va='bottom', fontsize=8, color=cycle(1))
    ax.plot(t, y, color=cycle(0), linewidth=1.1, label='signal')
    ax.plot(t[mask], y[mask], '.', color=cycle(1), markersize=4,
            label='flagged points')
    ax.set_xlabel('time (sample)'); ax.set_ylabel('sensor reading')
    ax.set_title(title)
    ax.legend(frameon=False, loc='lower left', fontsize=7)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
