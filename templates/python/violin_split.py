"""violin_split: 左右拆分小提琴（同类下两个条件对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from theme import apply_theme
from palette import cycle

def make_figure(left=None, right=None, labels=None, title='Split violin'):
    apply_theme()
    rng = np.random.default_rng(7)
    if left is None:
        left  = [rng.normal(0, 1, 200) for _ in range(4)]
        right = [rng.normal(0.5, 1, 200) for _ in range(4)]
        labels = list('ABCD')
    fig, ax = plt.subplots()
    for i, (l, r) in enumerate(zip(left, right)):
        for arr, side, col in [(l, -1, cycle(0)), (r, +1, cycle(1))]:
            kde = gaussian_kde(arr)
            ys = np.linspace(arr.min(), arr.max(), 100)
            xs = kde(ys) * 0.3 * side
            ax.fill_betweenx(ys, i + xs, i, color=col, alpha=0.6,
                             label=('left' if side == -1 else 'right') if i == 0 else None)
    ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels)
    ax.set_ylabel('value'); ax.set_title(title); ax.legend()
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
