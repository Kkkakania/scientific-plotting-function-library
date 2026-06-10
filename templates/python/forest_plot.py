"""forest_plot: 森林图（meta 分析常用，效应量+置信区间）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(labels=None, effects=None, ci_lo=None, ci_hi=None, title='Forest plot'):
    apply_theme()
    if labels is None:
        labels = [f'study {i+1}' for i in range(8)]
        rng = np.random.default_rng(6)
        effects = rng.normal(0.5, 0.4, 8)
        widths  = rng.uniform(0.2, 0.6, 8)
        ci_lo = effects - widths; ci_hi = effects + widths
    y = np.arange(len(labels))[::-1]
    fig, ax = plt.subplots()
    ax.hlines(y, ci_lo, ci_hi, color='gray', linewidth=1.2)
    ax.plot(effects, y, 's', color=cycle(0), markersize=8)
    ax.axvline(0, color='k', linewidth=0.6)
    ax.set_yticks(y); ax.set_yticklabels(labels)
    ax.set_xlabel('effect size'); ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
