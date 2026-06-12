"""arc_diagram: 弧线图（节点一字排开，上方半圆弧连边，弧高=距离）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(n=12, n_edges=16, title='Arc diagram'):
    apply_theme()
    rng = np.random.default_rng(3)
    x = np.arange(1, n + 1, dtype=float)
    edges = set()
    while len(edges) < n_edges:
        i, j = sorted(rng.choice(n, 2, replace=False))
        if j > i:
            edges.add((i, j))
    fig, ax = plt.subplots(figsize=(6.4, 4))
    th = np.linspace(0, np.pi, 60)
    for (i, j) in sorted(edges):
        w = rng.uniform(0.5, 2.5)
        c = (x[i] + x[j]) / 2
        r = (x[j] - x[i]) / 2          # arc height = half the node distance
        ax.plot(c + r * np.cos(th), r * np.sin(th), color='#607080',
                lw=0.6 + 0.6 * w, alpha=0.55, zorder=1)
    ax.plot([x[0] - 0.4, x[-1] + 0.4], [0, 0], color='#B0B6BC',
            lw=1, zorder=0)
    ax.scatter(x, np.zeros(n), s=120, c=[cycle(k) for k in range(n)],
               zorder=3, edgecolors='white', linewidths=0.8)
    for k in range(n):
        ax.text(x[k], -0.55, chr(65 + k), ha='center', va='top', fontsize=9)
    ax.set_xlim(0, n + 1); ax.set_ylim(-1.2, n / 2 + 0.6)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
