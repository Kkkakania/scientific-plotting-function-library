"""area_stacked: 堆叠面积（多组成）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, Y=None, labels=None, title='Stacked area'):
    apply_theme(fig_size=(8, 4))
    if x is None:
        rng = np.random.default_rng(0)
        x = np.linspace(0, 10, 60)
        Y = np.abs(rng.normal(2, 0.5, (4, 60)) + np.arange(4)[:, None]*0.2)
        labels = [f'comp {i+1}' for i in range(4)]
    fig, ax = plt.subplots()
    ax.stackplot(x, Y, colors=[cycle(i) for i in range(len(Y))],
                 alpha=0.8, labels=labels)
    ax.set_xlabel('x'); ax.set_ylabel('value'); ax.set_title(title)
    ax.legend(loc='upper left'); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
