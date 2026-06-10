"""confidence_band: 多组均值±标准差对比."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, means=None, stds=None, labels=None, title='Group means ± std'):
    apply_theme()
    rng = np.random.default_rng(2)
    if x is None:
        x = np.linspace(0, 10, 100)
        means = [np.sin(x), np.cos(x), 0.5*np.sin(2*x)]
        stds  = [0.15+0*x, 0.2+0*x, 0.1+0*x]
        labels = ['A', 'B', 'C']
    fig, ax = plt.subplots()
    for i, (m, s) in enumerate(zip(means, stds)):
        ax.fill_between(x, m-s, m+s, color=cycle(i), alpha=0.2)
        ax.plot(x, m, color=cycle(i), label=labels[i])
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
