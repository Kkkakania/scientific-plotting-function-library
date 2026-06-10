"""broken_axis: 折断坐标轴（异常值跨度极大时用）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, y=None, gap=(20, 90), title='Broken axis'):
    apply_theme(fig_size=(6, 4))
    if x is None:
        x = np.arange(10)
        y = np.concatenate([np.linspace(1, 15, 8), [95, 100]])
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios':[1, 3]})
    ax1.bar(x, y, color=cycle(0))
    ax2.bar(x, y, color=cycle(0))
    ax1.set_ylim(gap[1], y.max()*1.05); ax2.set_ylim(0, gap[0])
    ax1.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.tick_params(labeltop=False, bottom=False)
    d = 0.015
    kw = dict(transform=ax1.transAxes, color='k', clip_on=False, linewidth=1)
    ax1.plot((-d, +d), (-d, +d), **kw); ax1.plot((1-d, 1+d), (-d, +d), **kw)
    kw['transform'] = ax2.transAxes
    ax2.plot((-d, +d), (1-d, 1+d), **kw); ax2.plot((1-d, 1+d), (1-d, 1+d), **kw)
    ax2.set_xlabel('category'); ax1.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
