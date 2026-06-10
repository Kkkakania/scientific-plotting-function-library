"""graph_directed: 带权重有向图（环形布局，线宽=权重）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
from theme import apply_theme
from palette import cycle

def make_figure(n=8, title='Weighted directed graph'):
    apply_theme()
    rng = np.random.default_rng(5)
    ang = np.linspace(0, 2*np.pi, n, endpoint=False) + np.pi/2
    pos = np.c_[np.cos(ang), np.sin(ang)]*3
    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4); ax.axis('off'); ax.set_aspect('equal')
    edges = [(i, j) for i in range(n) for j in range(n)
             if i != j and rng.random() < 0.22]
    for i, j in edges:
        w = rng.uniform(0.5, 3.0)
        ax.add_patch(FancyArrowPatch(pos[i], pos[j], arrowstyle='-|>',
                     connectionstyle='arc3,rad=0.12', mutation_scale=11,
                     lw=0.5 + w*0.7, color='#607080', alpha=0.65,
                     shrinkA=14, shrinkB=14, zorder=1))
    deg = np.zeros(n)
    for i, j in edges: deg[i] += 1; deg[j] += 1
    for k in range(n):
        ax.add_patch(Circle(pos[k], 0.28 + deg[k]*0.03, color=cycle(k), zorder=3))
        ax.text(*pos[k], f'{k+1}', ha='center', va='center',
                color='white', fontsize=9, zorder=4)
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
