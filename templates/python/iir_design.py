"""iir_design: 不同 IIR 类型幅频响应对比."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, cheby2, ellip, freqz
from theme import apply_theme
from palette import cycle

def make_figure(title='IIR filter comparison'):
    apply_theme()
    fs = 1000; fc = 100; order = 6
    designs = [
        ('Butterworth',  butter(order, fc, fs=fs)),
        ('Cheby I',      cheby1(order, 1, fc, fs=fs)),
        ('Cheby II',     cheby2(order, 40, fc, fs=fs)),
        ('Elliptic',     ellip(order, 1, 40, fc, fs=fs)),
    ]
    fig, ax = plt.subplots()
    for i, (name, (b, a)) in enumerate(designs):
        w, h = freqz(b, a, fs=fs)
        ax.plot(w, 20*np.log10(np.abs(h) + 1e-12), color=cycle(i), label=name)
    ax.axvline(fc, color='gray', linestyle='--', linewidth=0.7)
    ax.set_xlabel('frequency (Hz)'); ax.set_ylabel('magnitude (dB)')
    ax.set_ylim(-80, 5); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
