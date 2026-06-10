"""sensitivity_function: S, T, KS 灵敏度函数族."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Sensitivity functions'):
    apply_theme()
    w = np.logspace(-2, 2, 500); s = 1j*w
    K = 5*(s + 2)/(s + 10)
    P = 1/(s*(s + 1))
    L = K*P
    S = 1/(1 + L); T = L/(1 + L); KS = K*S
    fig, ax = plt.subplots()
    ax.semilogx(w, 20*np.log10(np.abs(S)),  color=cycle(0), label='|S|')
    ax.semilogx(w, 20*np.log10(np.abs(T)),  color=cycle(1), label='|T|')
    ax.semilogx(w, 20*np.log10(np.abs(KS)), color=cycle(2), label='|KS|')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.set_xlabel('ω (rad/s)'); ax.set_ylabel('magnitude (dB)'); ax.set_title(title)
    ax.legend(); ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
