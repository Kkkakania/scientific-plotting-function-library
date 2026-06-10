"""bode_diagram: 幅频+相频两子图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(zetas=(0.1, 0.3, 0.707, 1.5), fn=100, title='Bode diagram'):
    apply_theme(fig_size=(8, 5.5))
    wn = 2*np.pi*fn
    w = np.logspace(0, 4, 500) * 2*np.pi
    fig, (ax_m, ax_p) = plt.subplots(2, 1, sharex=True)
    for i, z in enumerate(zetas):
        s = 1j*w
        H = wn**2 / (s**2 + 2*z*wn*s + wn**2)
        ax_m.semilogx(w/(2*np.pi), 20*np.log10(np.abs(H)), color=cycle(i), label=f'ζ={z}')
        ax_p.semilogx(w/(2*np.pi), np.unwrap(np.angle(H))*180/np.pi, color=cycle(i))
    ax_m.axhline(-3, color='gray', linestyle='--', linewidth=0.7)
    ax_m.set_ylabel('magnitude (dB)'); ax_m.set_title(title)
    ax_m.legend(); ax_m.grid(True, which='both', linestyle=':', alpha=0.5)
    ax_p.set_xlabel('frequency (Hz)'); ax_p.set_ylabel('phase (deg)')
    ax_p.set_yticks([0, -45, -90, -135, -180])
    ax_p.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
