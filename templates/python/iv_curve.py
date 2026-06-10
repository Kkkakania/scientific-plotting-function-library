"""iv_curve: 光伏组件 I-V 与 P-V 特性（多辐照度）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='PV I-V & P-V curves'):
    apply_theme(fig_size=(7, 5))
    V = np.linspace(0, 22, 300)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    for i, G in enumerate([1000, 800, 600, 400]):
        Isc = 8.2 * (G/1000)
        Voc = 22 - 0.4 * (1 - G/1000)
        I = Isc * (1 - np.exp((V - Voc)/2))
        I = np.clip(I, 0, Isc)
        P = V * I
        ax1.plot(V, I, color=cycle(i), label=f'G={G} W/m²')
        ax2.plot(V, P, '--', color=cycle(i), alpha=0.6)
    ax1.set_xlabel('V'); ax1.set_ylabel('I (A)'); ax2.set_ylabel('P (W)')
    ax1.set_title(title); ax1.legend(loc='lower left')
    ax2.spines['right'].set_visible(True)
    ax1.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
