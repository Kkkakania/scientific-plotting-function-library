"""polar_basic: 极坐标曲线."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Polar curve'):
    apply_theme(fig_size=(5.5, 5.5))
    theta = np.linspace(0, 2*np.pi, 500)
    r = 1 + 0.6*np.sin(5*theta)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color=cycle(0))
    ax.fill(theta, r, color=cycle(0), alpha=0.2)
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
