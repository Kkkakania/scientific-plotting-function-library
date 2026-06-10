"""box_jittered: 箱线图 + jitter 散点（数据点不多时强烈推荐）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(arrays=None, labels=None, title='Box + jitter'):
    apply_theme()
    rng = np.random.default_rng(4)
    if arrays is None:
        arrays = [rng.normal(loc, 1, 30) for loc in [0, 1, 2, 1.5]]
        labels = list('ABCD')
    fig, ax = plt.subplots()
    bp = ax.boxplot(arrays, tick_labels=labels, patch_artist=True, widths=0.5,
                    showfliers=False)
    for i, patch in enumerate(bp['boxes']):
        patch.set_facecolor(cycle(i)); patch.set_alpha(0.3)
    for i, arr in enumerate(arrays):
        x = np.full_like(arr, i+1) + rng.uniform(-0.12, 0.12, len(arr))
        ax.plot(x, arr, 'o', color=cycle(i), markersize=4, alpha=0.8)
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
