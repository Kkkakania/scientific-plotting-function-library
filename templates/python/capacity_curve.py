"""capacity_curve: Shannon 信道容量随 SNR 变化."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Shannon capacity'):
    apply_theme()
    snr_db = np.linspace(-10, 30, 200)
    snr = 10**(snr_db/10)
    fig, ax = plt.subplots()
    for i, B in enumerate([1, 5, 20]):
        C = B * np.log2(1 + snr)
        ax.plot(snr_db, C, color=cycle(i), label=f'B = {B} MHz')
    ax.set_xlabel('SNR (dB)'); ax.set_ylabel('capacity (Mbit/s)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
