"""signal_flow_graph: 信号流图（Mason 公式经典结构）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
from theme import apply_theme

def make_figure(title='Signal-flow graph'):
    apply_theme()
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.set_xlim(0, 12); ax.set_ylim(0, 5); ax.axis('off'); ax.set_aspect('equal')
    nodes = {'R': (1, 2.5), 'E': (3.2, 2.5), 'X1': (5.4, 2.5),
             'X2': (7.6, 2.5), 'Y': (9.8, 2.5)}
    for name, (x, y) in nodes.items():
        ax.add_patch(Circle((x, y), 0.16, color='#2E5077', zorder=3))
        ax.text(x, y - 0.55, name, ha='center', fontsize=9)
    def edge(a, b, gain, rad=0.0, color='#404040'):
        xa, ya = nodes[a]; xb, yb = nodes[b]
        ax.add_patch(FancyArrowPatch((xa, ya), (xb, yb), arrowstyle='-|>',
                     connectionstyle=f'arc3,rad={rad}', mutation_scale=13,
                     lw=1.3, color=color, shrinkA=10, shrinkB=10, zorder=2))
        mx, my = (xa + xb)/2, (ya + yb)/2
        off = 0.35 + abs(rad)*2.2
        ax.text(mx, my + (off if rad >= 0 else -off), gain,
                ha='center', fontsize=9, color=color)
    edge('R', 'E', '1')
    edge('E', 'X1', r'$G_1$')
    edge('X1', 'X2', r'$G_2$')
    edge('X2', 'Y', r'$G_3$')
    edge('X2', 'X1', r'$-H_1$', rad=0.5, color='#A8741A')
    edge('Y', 'E', r'$-H_2$', rad=0.55, color='#C44E52')
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
