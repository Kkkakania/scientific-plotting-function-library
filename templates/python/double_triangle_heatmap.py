"""double_triangle_heatmap: 上下三角分别展示两个矩阵."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential, diverging

def make_figure(A=None, B=None, title='Double-triangle heatmap'):
    apply_theme()
    if A is None:
        rng = np.random.default_rng(1)
        A = rng.uniform(0, 1, (10, 10))
        B = rng.uniform(-1, 1, (10, 10))
    n = A.shape[0]
    up = np.where(np.triu(np.ones_like(A), k=1) > 0, A, np.nan)
    lo = np.where(np.tril(np.ones_like(B), k=-1) > 0, B, np.nan)
    fig, ax = plt.subplots()
    im1 = ax.imshow(up, cmap=sequential(hue='blue'), aspect='auto')
    im2 = ax.imshow(lo, cmap=diverging(),            aspect='auto')
    for i in range(n):
        ax.text(i, i, '', ha='center', va='center')
    fig.colorbar(im1, ax=ax, label='upper', shrink=0.6, location='right')
    fig.colorbar(im2, ax=ax, label='lower', shrink=0.6, location='left')
    ax.set_title(title); ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
