"""dist_t_family: t 分布族（自由度变化）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as tdist
from theme import apply_theme
from palette import cycle

def make_figure(title="Student's t family"):
    apply_theme()
    x = np.linspace(-5, 5, 400)
    fig, ax = plt.subplots()
    for i, df in enumerate([1, 2, 5, 30]):
        ax.plot(x, tdist.pdf(x, df), color=cycle(i), label=f'df={df}')
    ax.plot(x, np.exp(-x**2/2)/np.sqrt(2*np.pi), '--', color='k', linewidth=0.8, label='N(0,1)')
    ax.set_xlabel('x'); ax.set_ylabel('PDF'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
