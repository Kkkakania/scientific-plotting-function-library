"""nichols_chart: Nichols 图（相位 vs 增益）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Nichols chart'):
    apply_theme(fig_size=(6, 5.5))
    w = np.logspace(-1, 2, 500); s = 1j*w
    G = 10 / (s * (s/5 + 1) * (s/50 + 1))
    fig, ax = plt.subplots()
    ax.plot(np.angle(G)*180/np.pi, 20*np.log10(np.abs(G)), color=cycle(0))
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(-180, color='gray', linewidth=0.5)
    ax.set_xlabel('phase (°)'); ax.set_ylabel('|G| (dB)'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
