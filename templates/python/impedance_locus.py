"""impedance_locus: Z(ω) 在复平面上的轨迹（RLC 串联）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(R=10, L=0.1, C=1e-4, title='Impedance locus (series RLC)'):
    apply_theme(fig_size=(6, 5))
    w = np.logspace(0, 5, 400)
    Z = R + 1j*w*L + 1/(1j*w*C)
    f0 = 1/(2*np.pi*np.sqrt(L*C))
    fig, ax = plt.subplots()
    ax.plot(Z.real, Z.imag, color=cycle(0))
    ax.plot(R, 0, 'rx', markersize=10, markeredgewidth=2, label=f'resonance (f = {f0:.1f} Hz)')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.set_xlabel('Re{Z}'); ax.set_ylabel('Im{Z}'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
