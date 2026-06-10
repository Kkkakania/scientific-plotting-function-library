"""line_log: 半对数/双对数图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(scale='loglog', title='Log-scale line'):
    apply_theme()
    x = np.logspace(-1, 3, 200)
    y1 = x**2
    y2 = x**1.5
    y3 = x**0.5
    fig, ax = plt.subplots()
    for i, (y, lab) in enumerate(zip([y1, y2, y3], ['x²', 'x^1.5', '√x'])):
        ax.plot(x, y, color=cycle(i), label=lab)
    if scale == 'loglog':
        ax.set_xscale('log'); ax.set_yscale('log')
    elif scale == 'semilogx':
        ax.set_xscale('log')
    elif scale == 'semilogy':
        ax.set_yscale('log')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.legend(); ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
