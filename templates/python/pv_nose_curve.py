"""pv_nose_curve: P-V 鼻形曲线（电压稳定极限）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='P-V nose curves'):
    apply_theme()
    fig, ax = plt.subplots()
    E, X = 1.0, 0.5
    for i, pf_tan in enumerate([-0.2, 0.0, 0.2]):
        P = np.linspace(0, 1.05/ (X*(1+pf_tan**2))**0.5, 400)
        Q = pf_tan * P
        disc = E**4/4 - X**2*P**2 - X*Q*E**2
        m = disc >= 0
        Vh = np.sqrt(E**2/2 - X*Q[m] + np.sqrt(disc[m]))
        Vl = np.sqrt(np.clip(E**2/2 - X*Q[m] - np.sqrt(disc[m]), 0, None))
        ax.plot(P[m], Vh, color=cycle(i), label=f'tanφ = {pf_tan:+.1f}')
        ax.plot(P[m], Vl, color=cycle(i), linestyle='--', linewidth=1)
        ax.plot(P[m][-1], Vh[-1], 'o', color=cycle(i), ms=4)
    ax.set_xlabel('P (p.u.)'); ax.set_ylabel('V (p.u.)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
