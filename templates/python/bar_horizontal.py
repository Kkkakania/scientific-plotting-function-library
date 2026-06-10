"""bar_horizontal: 横向条形（标签长时优先用这个）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(labels=None, values=None, title='Horizontal bar'):
    apply_theme()
    if labels is None:
        labels = [f'option {i+1}' for i in range(8)]
        values = sorted(np.random.default_rng(1).uniform(10, 90, 8))
    fig, ax = plt.subplots()
    ax.barh(labels, values, color=cycle(1))
    ax.set_xlabel('value'); ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
