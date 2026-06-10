"""dual_yaxis: 双 Y 轴对比（两个量纲不同的量）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(t=None, y1=None, y2=None, l1='Y1', l2='Y2', title='Dual Y-axis'):
    apply_theme()
    if t is None:
        t = np.arange(24)
        y1 = 20 + 8*np.sin((t-6)*np.pi/12)
        y2 = 60 - 20*np.sin((t-6)*np.pi/12)
    fig, ax1 = plt.subplots()
    ax1.plot(t, y1, '-o', color=cycle(0))
    ax1.set_ylabel(l1, color=cycle(0))
    ax1.tick_params(axis='y', labelcolor=cycle(0))
    ax2 = ax1.twinx()
    ax2.plot(t, y2, '-s', color=cycle(1))
    ax2.set_ylabel(l2, color=cycle(1))
    ax2.tick_params(axis='y', labelcolor=cycle(1))
    ax2.spines['right'].set_visible(True)
    ax1.set_xlabel('t'); ax1.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
