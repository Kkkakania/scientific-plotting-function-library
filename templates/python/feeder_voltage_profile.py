"""feeder_voltage_profile: 配电馈线电压分布（DG 接入前后）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Feeder voltage profile with/without DG'):
    apply_theme()
    node = np.arange(0, 16)
    base = 1.0 - 0.0042*node - 0.00012*node**2
    dg = base.copy(); dg[8:] += 0.0035*(node[8:] - 7)
    fig, ax = plt.subplots()
    ax.plot(node, base, 'o-', color=cycle(0), ms=4, label='without DG')
    ax.plot(node, dg, 's-', color=cycle(1), ms=4, label='with DG @ node 8')
    ax.axhline(0.95, color=cycle(3), linestyle='--', linewidth=1)
    ax.text(0.2, 0.9504, 'lower limit 0.95 p.u.', fontsize=8)
    ax.axvline(8, color='0.6', linestyle=':', linewidth=1)
    ax.set_xlabel('node number'); ax.set_ylabel('voltage (p.u.)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
