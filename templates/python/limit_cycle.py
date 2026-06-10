"""limit_cycle: Van der Pol 极限环."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from theme import apply_theme
from palette import cycle

def make_figure(title='Van der Pol limit cycle'):
    apply_theme(fig_size=(6, 5))
    def vdp(s, t, mu=1.5):
        x, y = s; return [y, mu*(1 - x**2)*y - x]
    t = np.linspace(0, 30, 3000)
    fig, ax = plt.subplots()
    for i, ic in enumerate([(0.1, 0), (2.5, 2.5), (-2.5, -1)]):
        sol = odeint(vdp, ic, t)
        ax.plot(sol[:, 0], sol[:, 1], color=cycle(i), linewidth=0.8, alpha=0.8)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.set_aspect('equal'); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
