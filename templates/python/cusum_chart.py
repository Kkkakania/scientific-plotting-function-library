"""cusum_chart: CUSUM 累积和控制图（双侧 C+/C-，决策限 ±h，越限标红）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(k=0.5, h=5.0, title='CUSUM control chart'):
    apply_theme()
    rng = np.random.default_rng(6)
    n = 60
    x = rng.normal(0, 1, n)
    x[35:] += 1.0                              # 注入小幅均值漂移
    cp = np.zeros(n); cm = np.zeros(n)
    for i in range(1, n):
        cp[i] = max(0, cp[i-1] + x[i] - k)
        cm[i] = min(0, cm[i-1] + x[i] + k)
    t = np.arange(n)
    fig, ax = plt.subplots()
    ax.plot(t, cp, '-o', color=cycle(0), markersize=3.5, label='C+ (upper)')
    ax.plot(t, cm, '-s', color=cycle(5), markersize=3.5, label='C- (lower)')
    ax.axhline(h, color=cycle(7), linestyle='--', linewidth=1, label='decision limit ±h')
    ax.axhline(-h, color=cycle(7), linestyle='--', linewidth=1)
    ax.axhline(0, color='#666666', linewidth=0.8)
    up_out, lo_out = cp > h, cm < -h
    ax.plot(t[up_out], cp[up_out], 'o', color=cycle(1), markersize=6,
            label='signal')
    ax.plot(t[lo_out], cm[lo_out], 's', color=cycle(1), markersize=6)
    ax.set_xlabel('sample number')
    ax.set_ylabel('cumulative sum (standardized)')
    ax.set_title(title)
    ax.legend(frameon=False, loc='upper left', fontsize=7)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
