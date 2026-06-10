"""ecdf: 经验累积分布函数."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='ECDF'):
    apply_theme()
    rng = np.random.default_rng(7)
    fig, ax = plt.subplots()
    for i, loc in enumerate([-1, 0, 1.5]):
        data = rng.normal(loc, 1, 400)
        xs = np.sort(data); ys = np.arange(1, len(xs)+1) / len(xs)
        ax.step(xs, ys, color=cycle(i), label=f'µ = {loc}')
    ax.set_xlabel('value'); ax.set_ylabel('P(X ≤ x)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
