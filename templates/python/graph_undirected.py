"""graph_undirected: 无向图（力导向式布局，社团着色）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from theme import apply_theme
from palette import cycle

def make_figure(title='Undirected network (communities)'):
    apply_theme()
    rng = np.random.default_rng(7)
    centers = np.array([[0, 0], [4.2, 1.2], [2.0, 4.0]])
    pos, com = [], []
    for c, ctr in enumerate(centers):
        k = 8
        pos.append(ctr + rng.normal(0, 0.85, (k, 2)))
        com += [c]*k
    pos = np.vstack(pos); com = np.array(com); n = len(pos)
    # 同社团密连 + 跨社团疏连
    segs, lws = [], []
    for i in range(n):
        for j in range(i+1, n):
            p = 0.42 if com[i] == com[j] else 0.03
            if rng.random() < p:
                segs.append([pos[i], pos[j]])
                lws.append(1.4 if com[i] == com[j] else 0.7)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.add_collection(LineCollection(segs, colors='#90A0AC',
                                     linewidths=lws, alpha=0.6, zorder=1))
    for c in range(3):
        m = com == c
        ax.scatter(pos[m, 0], pos[m, 1], s=120, color=cycle(c),
                   edgecolor='white', linewidth=1.2, zorder=3,
                   label=f'community {c+1}')
    ax.axis('off'); ax.set_aspect('equal')
    ax.legend(loc='lower right', fontsize=8)
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
