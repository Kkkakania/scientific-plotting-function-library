"""parallel_coordinates: 平行坐标（高维数据探索）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(data=None, names=None, classes=None, title='Parallel coordinates'):
    apply_theme(fig_size=(8, 4.5))
    if data is None:
        rng = np.random.default_rng(1)
        data = rng.uniform(0, 1, (60, 6))
        classes = (data[:, 0] > 0.5).astype(int)
        names = [f'd{i+1}' for i in range(6)]
    n_feat = data.shape[1]
    x = np.arange(n_feat)
    fig, ax = plt.subplots()
    for row, cls in zip(data, classes):
        ax.plot(x, row, color=cycle(int(cls)), alpha=0.4, linewidth=1)
    ax.set_xticks(x); ax.set_xticklabels(names)
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
