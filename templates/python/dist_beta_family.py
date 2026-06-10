"""dist_beta_family: Beta 分布族（不同 α, β）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta as bdist
from theme import apply_theme
from palette import cycle

def make_figure(title='Beta family'):
    apply_theme()
    x = np.linspace(0.001, 0.999, 400)
    fig, ax = plt.subplots()
    for i, (a, b) in enumerate([(0.5,0.5), (1,1), (2,5), (5,2), (8,8)]):
        ax.plot(x, bdist.pdf(x, a, b), color=cycle(i), label=f'α={a}, β={b}')
    ax.set_xlabel('x'); ax.set_ylabel('PDF'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
