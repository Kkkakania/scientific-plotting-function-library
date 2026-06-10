"""battery_discharge: 电池放电曲线（多倍率）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Battery discharge curves'):
    apply_theme()
    soc = np.linspace(100, 0, 200)
    fig, ax = plt.subplots()
    for i, C in enumerate([0.2, 0.5, 1.0, 2.0]):
        plateau = 3.7 - 0.05*C
        V = plateau - (100 - soc)/100 * 0.5 - 0.15*C*np.exp(-soc/15)
        V = np.where(soc < 5, V - (5-soc)*0.1, V)
        ax.plot(100 - soc, V, color=cycle(i), label=f'{C}C')
    ax.set_xlabel('capacity discharged (%)'); ax.set_ylabel('cell voltage (V)')
    ax.set_title(title); ax.legend(title='rate')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
