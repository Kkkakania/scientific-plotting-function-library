"""errorbar_filled: 阴影区间替代误差棒（数据点密时更清晰）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, mean=None, std=None, title='Mean with band'):
    apply_theme()
    if x is None:
        rng = np.random.default_rng(1)
        x = np.linspace(0, 10, 100)
        trials = np.sin(x) + 0.15*rng.standard_normal((30, 100))
        mean = trials.mean(0); std = trials.std(0)
    fig, ax = plt.subplots()
    ax.fill_between(x, mean-std, mean+std, color=cycle(0), alpha=0.25)
    ax.plot(x, mean, color=cycle(0))
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
