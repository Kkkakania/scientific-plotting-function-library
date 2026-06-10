"""nyquist_diagram: 开环频率特性 Nyquist 轨迹."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(K=10, title='Nyquist diagram'):
    apply_theme(fig_size=(5.5, 5.5))
    w = np.logspace(-2, 2, 5000); s = 1j*w
    G = K / (s * (s + 1) * (s + 5))
    fig, ax = plt.subplots()
    ax.plot( G.real,  G.imag, color=cycle(0), label='ω > 0')
    ax.plot( G.real, -G.imag, color=cycle(0), linestyle='--', label='ω < 0')
    ax.plot(-1, 0, 'rx', markersize=10, markeredgewidth=2, label='(-1, 0)')
    ax.axhline(0, color='gray', linewidth=0.5); ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlim(-3, 1); ax.set_ylim(-2, 2); ax.set_aspect('equal')
    ax.set_xlabel('Re'); ax.set_ylabel('Im')
    ax.set_title(f'{title}: K={K}/[s(s+1)(s+5)]'); ax.legend()
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
