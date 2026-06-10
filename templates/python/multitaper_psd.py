"""multitaper_psd: 多窗法 PSD（用多个正交窗平均）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import dpss
from theme import apply_theme
from palette import cycle

def make_figure(title='Multitaper PSD'):
    apply_theme()
    fs = 1000; N = 2048
    t = np.arange(N) / fs
    sig = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t) + 0.3*np.random.default_rng(0).standard_normal(N)
    tapers = dpss(N, NW=3, Kmax=5)
    psds = []
    for tap in tapers:
        S = np.abs(np.fft.rfft(sig * tap))**2
        psds.append(S)
    psd = np.mean(psds, axis=0)
    psd_single = np.abs(np.fft.rfft(sig))**2
    f = np.fft.rfftfreq(N, 1/fs)
    fig, ax = plt.subplots()
    ax.semilogy(f, psd_single, color='lightgray', linewidth=0.8, label='single taper')
    ax.semilogy(f, psd,        color=cycle(0),    linewidth=1.5, label='multitaper (k=5)')
    ax.set_xlim(0, 200); ax.set_xlabel('frequency (Hz)'); ax.set_ylabel('PSD')
    ax.set_title(title); ax.legend()
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
