"""single_line_diagram: 电气主接线单线图（电源-变压器-母线-馈线）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from theme import apply_theme

def _breaker(ax, x, y, closed=True):
    c = '#2E5077' if closed else '#C44E52'
    ax.add_patch(plt.Rectangle((x-0.14, y-0.14), 0.28, 0.28, fill=closed,
                 facecolor=c if closed else 'white', edgecolor=c, lw=1.2, zorder=3))

def make_figure(title='Single-line diagram (110/10 kV substation)'):
    apply_theme()
    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 9); ax.axis('off'); ax.set_aspect('equal')
    lc = '#303030'
    # 电源进线 ×2
    for i, x in enumerate([3.5, 8.5]):
        ax.annotate('', xy=(x, 7.6), xytext=(x, 8.7),
                    arrowprops=dict(arrowstyle='-|>', lw=1.4, color=lc))
        ax.text(x + 0.2, 8.45, f'110 kV source {i+1}', fontsize=8)
        _breaker(ax, x, 7.3)
        ax.plot([x, x], [7.16, 6.6], color=lc, lw=1.4)
        # 变压器（双圆圈）
        ax.add_patch(Circle((x, 6.25), 0.38, fill=False, ec=lc, lw=1.4))
        ax.add_patch(Circle((x, 5.75), 0.38, fill=False, ec=lc, lw=1.4))
        ax.text(x + 0.5, 6.0, f'T{i+1}\n31.5 MVA', fontsize=7.5, va='center')
        ax.plot([x, x], [5.37, 4.9], color=lc, lw=1.4)
        _breaker(ax, x, 4.62)
        ax.plot([x, x], [4.48, 4.0], color=lc, lw=1.4)
    # 10kV 分段母线
    ax.plot([1.5, 5.8], [4.0, 4.0], color=lc, lw=3)
    ax.plot([6.2, 10.5], [4.0, 4.0], color=lc, lw=3)
    ax.text(1.5, 4.2, 'Bus I (10 kV)', fontsize=8)
    ax.text(9.0, 4.2, 'Bus II (10 kV)', fontsize=8)
    _breaker(ax, 6.0, 4.0, closed=False)   # 分段断路器常开
    ax.text(5.6, 3.55, 'bus tie\n(N.O.)', fontsize=7, ha='center')
    # 馈线
    for x in [2.2, 3.4, 4.6, 7.4, 8.6, 9.8]:
        ax.plot([x, x], [4.0, 3.2], color=lc, lw=1.2)
        _breaker(ax, x, 2.95)
        ax.annotate('', xy=(x, 1.9), xytext=(x, 2.8),
                    arrowprops=dict(arrowstyle='-|>', lw=1.1, color=lc))
    ax.text(6.0, 1.45, 'outgoing feeders (10 kV)', fontsize=8, ha='center')
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
