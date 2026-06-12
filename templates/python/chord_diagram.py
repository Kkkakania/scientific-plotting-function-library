"""chord_diagram: 和弦图（6 节点流量矩阵，弧带宽=流量，贝塞尔连接）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def _arc(t1, t2, r, m=40):
    a = np.linspace(t1, t2, m)
    return np.c_[r * np.cos(a), r * np.sin(a)]


def _chord(t1, t2, r, m=40):
    p0 = r * np.array([np.cos(t1), np.sin(t1)])
    p1 = r * np.array([np.cos(t2), np.sin(t2)])
    t = np.linspace(0, 1, m)[:, None]
    return (1 - t)**2 * p0 + t**2 * p1


def make_figure(F=None, title='Chord diagram of flows'):
    apply_theme()
    rng = np.random.default_rng(7)
    n = 6
    if F is None:
        F = rng.integers(0, 9, (n, n)).astype(float)
        F[F < 3] = 0
        np.fill_diagonal(F, 0)
    totals = F.sum(0) + F.sum(1)
    gap = 0.05
    span = (2 * np.pi - n * gap) * totals / totals.sum()
    starts = np.pi / 2 + np.concatenate(([0], np.cumsum(span[:-1] + gap)))
    seg_o = np.zeros((n, n, 2)); seg_i = np.zeros((n, n, 2))
    cur = starts.copy()
    for i in range(n):
        for j in range(n):
            if F[i, j] > 0:
                w = F[i, j] / totals[i] * span[i]
                seg_o[i, j] = (cur[i], cur[i] + w); cur[i] += w
        for j in range(n):
            if F[j, i] > 0:
                w = F[j, i] / totals[i] * span[i]
                seg_i[i, j] = (cur[i], cur[i] + w); cur[i] += w
    fig, ax = plt.subplots(figsize=(5.6, 5.4))
    ax.set_xlim(-1.55, 1.55); ax.set_ylim(-1.55, 1.55)
    ax.set_aspect('equal'); ax.axis('off')
    for i in range(n):                      # ribbons
        for j in range(n):
            if F[i, j] > 0:
                a1, a2 = seg_o[i, j]; b1, b2 = seg_i[j, i]
                poly = np.vstack([_arc(a1, a2, 0.96), _chord(a2, b1, 0.96),
                                  _arc(b1, b2, 0.96), _chord(b2, a1, 0.96)])
                ax.fill(poly[:, 0], poly[:, 1], color=cycle(i),
                        alpha=0.45, lw=0, zorder=1)
    for k in range(n):                      # node arc bands + labels
        band = np.vstack([_arc(starts[k], starts[k] + span[k], 1.0),
                          _arc(starts[k] + span[k], starts[k], 1.09)])
        ax.fill(band[:, 0], band[:, 1], color=cycle(k), lw=0, zorder=3)
        mid = starts[k] + span[k] / 2
        ax.text(1.26 * np.cos(mid), 1.26 * np.sin(mid), f'N{k+1}',
                ha='center', va='center', fontsize=9)
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
