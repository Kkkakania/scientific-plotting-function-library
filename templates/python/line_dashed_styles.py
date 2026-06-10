"""line_dashed_styles: 不同线型对比展示."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Line styles'):
    apply_theme()
    x = np.linspace(0, 10, 100)
    styles = [('-', 'solid'), ('--', 'dashed'), ('-.', 'dashdot'), (':', 'dotted')]
    fig, ax = plt.subplots()
    for i, (ls, name) in enumerate(styles):
        ax.plot(x, np.sin(x) + i*0.6, linestyle=ls, color=cycle(i), label=name)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
