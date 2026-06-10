"""ber_curve: 不同调制方式的 BER vs SNR（理论曲线）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
from theme import apply_theme
from palette import cycle

def make_figure(title='BER vs Eb/N0'):
    apply_theme()
    ebn0_db = np.linspace(0, 14, 30)
    ebn0 = 10**(ebn0_db/10)
    bpsk = 0.5*erfc(np.sqrt(ebn0))
    qpsk = bpsk
    qam16 = (3/8)*erfc(np.sqrt((2/5)*ebn0))
    qam64 = (7/24)*erfc(np.sqrt((1/7)*ebn0))
    fig, ax = plt.subplots()
    ax.semilogy(ebn0_db, bpsk,  color=cycle(0), label='BPSK')
    ax.semilogy(ebn0_db, qpsk,  '--', color=cycle(1), label='QPSK')
    ax.semilogy(ebn0_db, qam16, color=cycle(2), label='16-QAM')
    ax.semilogy(ebn0_db, qam64, color=cycle(3), label='64-QAM')
    ax.set_xlabel('Eb/N₀ (dB)'); ax.set_ylabel('BER'); ax.set_title(title)
    ax.set_ylim(1e-6, 1); ax.legend()
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
