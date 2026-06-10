"""line_basic: 单条折线."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_line

def make_figure(x=None, y=None, label='y', title='Line plot'):
    apply_theme()
    if x is None:
        x, y = gen_line(n=100)
    fig, ax = plt.subplots()
    ax.plot(x, y, color=cycle(0), label=label)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
