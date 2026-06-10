"""line_multi: 多条折线对比."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_line

def make_figure(x=None, Y=None, labels=None, title='Multi-line'):
    apply_theme()
    if x is None:
        x, Y = gen_line(n=100, n_series=4)
        labels = [f'series {i+1}' for i in range(4)]
    fig, ax = plt.subplots()
    for i, y in enumerate(Y):
        ax.plot(x, y, color=cycle(i), label=labels[i] if labels else None)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
