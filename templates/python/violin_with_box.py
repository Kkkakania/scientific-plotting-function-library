"""violin_with_box: 小提琴外形 + 内嵌箱线."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Violin + box'):
    apply_theme()
    rng = np.random.default_rng(6)
    arrays = [rng.normal(loc, 1, 200) for loc in [0, 1, 1.5, 0.5]]
    labels = list('ABCD')
    fig, ax = plt.subplots()
    parts = ax.violinplot(arrays, showextrema=False)
    for i, b in enumerate(parts['bodies']):
        b.set_facecolor(cycle(i)); b.set_alpha(0.5); b.set_edgecolor(cycle(i))
    bp = ax.boxplot(arrays, positions=range(1, len(arrays)+1), widths=0.15,
                    patch_artist=True, showfliers=False)
    for patch in bp['boxes']:
        patch.set_facecolor('white')
    ax.set_xticks(range(1, len(labels)+1)); ax.set_xticklabels(labels)
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
