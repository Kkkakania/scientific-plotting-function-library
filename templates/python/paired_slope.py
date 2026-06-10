"""paired_slope: 配对斜率图（before/after 个体变化趋势）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(before=None, after=None, title='Paired slope'):
    apply_theme()
    if before is None:
        rng = np.random.default_rng(7)
        before = rng.uniform(20, 80, 25); after = before + rng.normal(5, 8, 25)
    fig, ax = plt.subplots()
    for b, a in zip(before, after):
        col = cycle(0) if a > b else cycle(1)
        ax.plot([0, 1], [b, a], '-o', color=col, alpha=0.5, markersize=4)
    ax.set_xticks([0, 1]); ax.set_xticklabels(['before', 'after'])
    ax.set_xlim(-0.3, 1.3)
    ax.set_ylabel('measurement'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
