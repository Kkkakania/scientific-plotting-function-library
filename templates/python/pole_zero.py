"""pole_zero: 极点零点分布图 + 单位圆."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(zeros=None, poles=None, title='Pole-zero plot'):
    apply_theme(fig_size=(5.5, 5.5))
    if zeros is None:
        zeros = [0.6+0.4j, 0.6-0.4j]
        poles = [-0.5+0.3j, -0.5-0.3j, 0.2]
    theta = np.linspace(0, 2*np.pi, 200)
    fig, ax = plt.subplots()
    ax.plot(np.cos(theta), np.sin(theta), 'k', linewidth=0.8)
    ax.axhline(0, color='gray', linewidth=0.5); ax.axvline(0, color='gray', linewidth=0.5)
    for z in zeros:
        ax.plot(z.real, z.imag, 'o', markersize=10, markerfacecolor='none',
                markeredgecolor='#1f77b4', markeredgewidth=1.6)
    for p in poles:
        ax.plot(p.real, p.imag, 'x', markersize=12, markeredgewidth=1.8, color='#d62728')
    ax.set_aspect('equal'); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('Re'); ax.set_ylabel('Im'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
