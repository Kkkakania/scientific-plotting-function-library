"""ridgeline: 山脊图（多组分布纵向堆叠）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from theme import apply_theme
from palette import cycle

def make_figure(arrays=None, labels=None, title='Ridgeline'):
    apply_theme(fig_size=(7, 5))
    rng = np.random.default_rng(8)
    if arrays is None:
        arrays = [rng.normal(loc, 1, 400) for loc in np.linspace(0, 4, 6)]
        labels = [f'group {i+1}' for i in range(6)]
    fig, ax = plt.subplots()
    xs = np.linspace(-4, 8, 200)
    for i, arr in enumerate(arrays):
        kde = gaussian_kde(arr)(xs)
        kde = kde / kde.max() * 0.8
        ax.fill_between(xs, i, i + kde, color=cycle(i), alpha=0.7)
        ax.plot(xs, i + kde, color='white', linewidth=0.8)
    ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels)
    ax.set_xlabel('value'); ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
