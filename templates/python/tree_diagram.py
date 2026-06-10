"""tree_diagram: 简单决策树/分类树（递归绘制）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Tree diagram'):
    apply_theme(fig_size=(8, 5))
    fig, ax = plt.subplots()
    def node(x, y, txt, c):
        ax.add_patch(plt.Circle((x, y), 0.25, color=c, alpha=0.85))
        ax.text(x, y, txt, ha='center', va='center', color='white', fontsize=8)
    def edge(x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], color='gray', linewidth=1)
    edge(4, 4, 2, 3); edge(4, 4, 6, 3)
    edge(2, 3, 1, 2); edge(2, 3, 3, 2)
    edge(6, 3, 5, 2); edge(6, 3, 7, 2)
    node(4, 4, 'X1<0.5', cycle(0))
    node(2, 3, 'X2<2',   cycle(0))
    node(6, 3, 'X2<3',   cycle(0))
    node(1, 2, 'A',      cycle(1))
    node(3, 2, 'B',      cycle(2))
    node(5, 2, 'C',      cycle(3))
    node(7, 2, 'D',      cycle(4))
    ax.set_xlim(0, 8); ax.set_ylim(1.5, 4.5)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
