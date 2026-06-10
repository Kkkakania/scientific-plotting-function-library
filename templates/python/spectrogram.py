"""spectrogram: 短时傅里叶变换时频图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp, spectrogram as _spec
from theme import apply_theme

def make_figure(sig=None, fs=2000, title='Spectrogram'):
    apply_theme(fig_size=(8, 4))
    if sig is None:
        t = np.arange(0, 2, 1/fs)
        sig = chirp(t, f0=20, f1=400, t1=2, method='linear')
    f, tt, Sxx = _spec(sig, fs=fs, nperseg=256, noverlap=200)
    fig, ax = plt.subplots()
    pcm = ax.pcolormesh(tt, f, 10*np.log10(Sxx + 1e-12), cmap='magma', shading='auto')
    fig.colorbar(pcm, ax=ax, label='dB')
    ax.set_xlabel('t (s)'); ax.set_ylabel('frequency (Hz)'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
