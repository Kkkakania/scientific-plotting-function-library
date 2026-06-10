"""dist_chi_family: 卡方分布族."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from theme import apply_theme
from palette import cycle

def make_figure(title='Chi-square family'):
    apply_theme()
    x = np.linspace(0.01, 25, 400)
    fig, ax = plt.subplots()
    for i, df in enumerate([2, 4, 6, 10, 15]):
        ax.plot(x, chi2.pdf(x, df), color=cycle(i), label=f'df={df}')
    ax.set_xlabel('x'); ax.set_ylabel('PDF'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
