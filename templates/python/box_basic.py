"""box_basic: 箱线图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(arrays=None, labels=None, title='Box plot'):
    apply_theme()
    if arrays is None:
        rng = np.random.default_rng(3)
        arrays = [rng.normal(loc, 1, 100) for loc in [0, 1, 2, 1.5, 0.5]]
        labels = list('ABCDE')
    fig, ax = plt.subplots()
    bp = ax.boxplot(arrays, tick_labels=labels, patch_artist=True)
    for i, patch in enumerate(bp['boxes']):
        patch.set_facecolor(cycle(i)); patch.set_alpha(0.6)
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
