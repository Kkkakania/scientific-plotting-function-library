"""pv_iv_temperature: 光伏 I-V/P-V 曲线随温度变化."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(title='PV module I-V curves vs temperature'):
    apply_theme()
    cmap = sequential('orange')
    V = np.linspace(0, 48, 400)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.6))
    temps = [0, 25, 50, 75]
    for i, T in enumerate(temps):
        Voc = 44 - 0.16*(T - 25); Isc = 9.0*(1 + 0.0005*(T - 25))
        I = Isc*(1 - np.exp((V - Voc)/2.2))
        I = np.clip(I, 0, None)
        c = cmap(0.3 + 0.7*i/(len(temps)-1))
        ax1.plot(V, I, color=c, label=f'{T} °C')
        ax2.plot(V, V*I, color=c, label=f'{T} °C')
        ax2.plot(V[np.argmax(V*I)], (V*I).max(), 'o', color=c, ms=4)
    ax1.set_xlabel('voltage (V)'); ax1.set_ylabel('current (A)'); ax1.set_title('I-V')
    ax2.set_xlabel('voltage (V)'); ax2.set_ylabel('power (W)'); ax2.set_title('P-V with MPP')
    for ax in (ax1, ax2):
        ax.legend(fontsize=7); ax.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(title, y=1.02, fontsize=10)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
