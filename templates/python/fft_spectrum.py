"""fft_spectrum: FFT 单边幅值谱."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_signal

def make_figure(t=None, sig=None, fs=None, title='FFT spectrum'):
    apply_theme(fig_size=(8, 4.5))
    if t is None:
        t, sig, fs = gen_signal()
    N = len(sig)
    Y = np.fft.rfft(sig); f = np.fft.rfftfreq(N, 1/fs)
    amp = 2*np.abs(Y)/N; amp[0] /= 2
    fig, (a1, a2) = plt.subplots(2, 1)
    a1.plot(t[:300], sig[:300], color=cycle(0))
    a1.set_xlabel('t (s)'); a1.set_ylabel('amp'); a1.set_title('Time')
    a1.grid(True, linestyle=':', alpha=0.5)
    a2.plot(f, amp, color=cycle(1))
    a2.set_xlabel('frequency (Hz)'); a2.set_ylabel('|Y|'); a2.set_title('Spectrum')
    a2.set_xlim(0, fs/4); a2.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
