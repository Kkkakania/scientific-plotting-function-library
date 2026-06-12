"""step_after_compare: 前后阶梯对比（切换前后水平段均值 + 置信带）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(switch=50, title='Before / after step comparison'):
    apply_theme()
    rng = np.random.default_rng(19)
    n = 100
    t = np.arange(n)
    y = np.where(t < switch, 5.0, 6.5) + rng.normal(0, 0.6, n)
    segs = [(t < switch, cycle(0), 'before'), (t >= switch, cycle(1), 'after')]
    fig, ax = plt.subplots()
    ax.plot(t, y, '.', color='#999999', markersize=4, alpha=0.7,
            label='observations')
    for mask, c, name in segs:
        m, s = y[mask].mean(), y[mask].std(ddof=1)
        ci = 1.96 * s / np.sqrt(mask.sum())
        tt = t[mask]
        ax.fill_between([tt[0], tt[-1]], m - ci, m + ci, color=c, alpha=0.2)
        ax.hlines(m, tt[0], tt[-1], color=c, linewidth=2.2,
                  label=f'{name} mean = {m:.2f}')
    ax.axvline(switch - 0.5, color='#666666', linestyle='--', linewidth=1)
    ax.text(switch - 0.5, ax.get_ylim()[1], ' intervention', fontsize=8,
            va='top', color='#666666')
    ax.set_xlabel('time (sample)'); ax.set_ylabel('process output')
    ax.set_title(title)
    ax.legend(frameon=False, loc='lower right', fontsize=8)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
