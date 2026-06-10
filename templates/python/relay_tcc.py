"""relay_tcc: 反时限过流保护时间-电流特性（log-log TCC）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Inverse-time overcurrent coordination'):
    apply_theme()
    M = np.linspace(1.1, 30, 400)
    fig, ax = plt.subplots()
    # IEC 60255 标准反时限族: t = TDS * k / (M^a - 1)
    for i, (name, k, a, tds) in enumerate([
            ('standard inverse', 0.14, 0.02, 0.3),
            ('very inverse', 13.5, 1.0, 0.4),
            ('extremely inverse', 80.0, 2.0, 0.5)]):
        ax.loglog(M, tds*k/(M**a - 1), color=cycle(i), label=name)
    ax.set_xlabel('current multiple M = I/I_pickup'); ax.set_ylabel('operating time (s)')
    ax.set_title(title); ax.legend()
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
