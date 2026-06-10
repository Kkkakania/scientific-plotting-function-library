"""fir_design: FIR 滤波器系数 + 幅频响应."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
from theme import apply_theme
from palette import cycle

def make_figure(title='FIR low-pass design'):
    apply_theme(fig_size=(8, 5))
    fs = 1000; fc = 100; N = 51
    b = firwin(N, fc, fs=fs, window='hamming')
    w, h = freqz(b, fs=fs)
    fig, (a1, a2) = plt.subplots(2, 1)
    a1.stem(b, linefmt='-', markerfmt='o', basefmt=' ')
    a1.set_xlabel('tap'); a1.set_ylabel('coefficient'); a1.set_title('Impulse response')
    a1.grid(True, linestyle=':', alpha=0.5)
    a2.plot(w, 20*np.log10(np.abs(h) + 1e-12), color=cycle(0))
    a2.axvline(fc, color='red', linestyle='--', linewidth=0.8, label=f'fc = {fc} Hz')
    a2.set_xlabel('frequency (Hz)'); a2.set_ylabel('magnitude (dB)')
    a2.set_title('Frequency response'); a2.legend()
    a2.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
