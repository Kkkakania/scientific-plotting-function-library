"""uncertainty_fan: 扇形不确定性（多分位数嵌套）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, sims=None, title='Uncertainty fan'):
    apply_theme()
    if x is None:
        rng = np.random.default_rng(3)
        x = np.arange(50)
        sims = np.cumsum(rng.normal(0, 1, (500, 50)), axis=1)
    qs = [5, 25, 50, 75, 95]
    pcts = np.percentile(sims, qs, axis=0)
    fig, ax = plt.subplots()
    ax.fill_between(x, pcts[0], pcts[4], color=cycle(0), alpha=0.15, label='5-95%')
    ax.fill_between(x, pcts[1], pcts[3], color=cycle(0), alpha=0.30, label='25-75%')
    ax.plot(x, pcts[2], color=cycle(0), label='median')
    ax.set_xlabel('t'); ax.set_ylabel('value'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
