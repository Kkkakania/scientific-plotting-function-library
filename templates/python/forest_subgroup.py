"""forest_subgroup: 分组森林图（每组多个研究）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Subgroup forest plot'):
    apply_theme(fig_size=(7, 5))
    rng = np.random.default_rng(6)
    groups = ['Trial set A', 'Trial set B', 'Trial set C']
    studies_per = 4
    fig, ax = plt.subplots()
    y = 0; ticks = []; labels = []
    for g, group in enumerate(groups):
        ax.text(-2.3, y+0.5, group, fontweight='bold')
        for s in range(studies_per):
            y -= 1
            eff = rng.normal(0.3, 0.4); err = rng.uniform(0.2, 0.5)
            ax.hlines(y, eff-err, eff+err, color='gray', linewidth=1.2)
            ax.plot(eff, y, 's', color=cycle(g), markersize=8)
            ticks.append(y); labels.append(f'  study {s+1}')
        # pooled
        y -= 1
        ax.plot(0.3, y, 'D', color=cycle(g), markersize=10)
        ticks.append(y); labels.append('  pooled')
        y -= 0.5
    ax.axvline(0, color='k', linewidth=0.6)
    ax.set_yticks(ticks); ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel('effect size'); ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
