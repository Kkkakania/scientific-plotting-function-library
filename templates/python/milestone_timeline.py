"""milestone_timeline: 里程碑时间轴（水平主轴，标注上下交替防重叠）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Milestone timeline'):
    apply_theme(fig_size=(8, 3.5))
    miles = [(1, 'Kick-off'), (3, 'Spec freeze'), (6, 'Alpha build'),
             (9, 'Field test'), (12, 'Beta release'), (15, 'Certification'),
             (18, 'Launch')]
    x = np.array([m[0] for m in miles])
    levels = np.tile([1.0, -1.0], len(miles))[:len(miles)] \
        * np.tile([1.0, 1.0, 0.6, 0.6], 2)[:len(miles)]
    fig, ax = plt.subplots()
    ax.axhline(0, color='#666666', linewidth=1.2)
    ax.vlines(x, 0, levels, color=cycle(0), linewidth=1)
    ax.plot(x, np.zeros_like(x), 'o', color=cycle(1), markersize=7,
            markerfacecolor='white', markeredgewidth=1.6)
    for (xi, name), lv in zip(miles, levels):
        ax.text(xi, lv + 0.09 * np.sign(lv), name, ha='center',
                va='bottom' if lv > 0 else 'top', fontsize=8)
        ax.text(xi, -0.14 * np.sign(lv), f'M{xi}', ha='center',
                va='top' if lv > 0 else 'bottom', fontsize=7, color='#888888')
    ax.set_ylim(-1.6, 1.6)
    ax.set_yticks([])
    for sp in ('left', 'top', 'right'):
        ax.spines[sp].set_visible(False)
    ax.set_xlabel('project month'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
