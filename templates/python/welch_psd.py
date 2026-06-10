"""welch_psd: Welch 法功率谱密度（噪声信号更稳）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from theme import apply_theme
from palette import cycle
from demo_data import gen_signal

def make_figure(sig=None, fs=None, title='Welch PSD'):
    apply_theme(fig_size=(7, 4))
    if sig is None:
        _, sig, fs = gen_signal()
    f, Pxx = welch(sig, fs=fs, nperseg=256)
    fig, ax = plt.subplots()
    ax.semilogy(f, Pxx, color=cycle(0))
    ax.set_xlabel('frequency (Hz)'); ax.set_ylabel('PSD (V²/Hz)')
    ax.set_title(title); ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
