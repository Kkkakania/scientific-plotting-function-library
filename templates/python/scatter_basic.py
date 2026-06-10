"""scatter_basic: 单组散点."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_scatter

def make_figure(x=None, y=None, title='Scatter'):
    apply_theme()
    if x is None:
        x, y, _ = gen_scatter(n=150)
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=30, c=cycle(0), alpha=0.7, edgecolors='w', linewidth=0.4)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
