"""economic_dispatch: 机组经济调度（成本曲线 + 等微增率）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Economic dispatch (equal incremental cost)'):
    apply_theme()
    P = np.linspace(50, 400, 300)
    units = [(0.004, 5.5, 120), (0.006, 4.8, 90), (0.009, 4.0, 60)]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.6))
    for i, (a, b, c) in enumerate(units):
        ax1.plot(P, a*P**2 + b*P + c, color=cycle(i), label=f'Unit {i+1}')
        ax2.plot(P, 2*a*P + b, color=cycle(i), label=f'Unit {i+1}')
    lam = 7.2
    ax2.axhline(lam, color='0.3', linestyle='--', linewidth=1)
    ax2.text(60, lam + 0.12, r'system λ', fontsize=8)
    for i, (a, b, c) in enumerate(units):
        Popt = (lam - b)/(2*a)
        ax2.plot(Popt, lam, 'o', color=cycle(i), ms=5)
    ax1.set_xlabel('P (MW)'); ax1.set_ylabel('cost ($/h)'); ax1.set_title('cost curves')
    ax2.set_xlabel('P (MW)'); ax2.set_ylabel('incremental cost ($/MWh)')
    ax2.set_title('equal-λ dispatch')
    for ax in (ax1, ax2):
        ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(title, y=1.02, fontsize=10)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
