"""dist_normal_family: 多参正态分布族 PDF."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Normal distribution family'):
    apply_theme()
    x = np.linspace(-6, 6, 400)
    fig, ax = plt.subplots()
    for i, (mu, sigma) in enumerate([(0, 0.5), (0, 1), (0, 2), (-1, 1), (2, 0.8)]):
        pdf = np.exp(-(x-mu)**2/(2*sigma**2)) / (sigma*np.sqrt(2*np.pi))
        ax.plot(x, pdf, color=cycle(i), label=f'µ={mu}, σ={sigma}')
    ax.set_xlabel('x'); ax.set_ylabel('PDF'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
