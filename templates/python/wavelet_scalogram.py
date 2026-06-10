"""wavelet_scalogram: CWT-风格时频图（轻量 Morlet 模拟，仅作可视化用途）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Wavelet scalogram'):
    apply_theme(fig_size=(8, 4))
    fs = 500
    t = np.arange(0, 1, 1/fs)
    sig = np.sin(2*np.pi*20*t) * (t < 0.4) + np.sin(2*np.pi*80*t) * (t >= 0.4)
    freqs = np.logspace(np.log10(5), np.log10(120), 40)
    W = np.zeros((len(freqs), len(t)))
    for i, f in enumerate(freqs):
        N = int(min(6*fs/f, len(t)))
        n = np.arange(-N//2, N//2)
        wlt = np.exp(2j*np.pi*f*n/fs) * np.exp(-(n/fs)**2 * (f**2) * 2)
        W[i] = np.abs(np.convolve(sig, wlt, mode='same'))
    fig, ax = plt.subplots()
    pc = ax.pcolormesh(t, freqs, W, cmap='magma', shading='auto')
    ax.set_yscale('log')
    fig.colorbar(pc, ax=ax, label='|W|')
    ax.set_xlabel('t (s)'); ax.set_ylabel('frequency (Hz)'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
