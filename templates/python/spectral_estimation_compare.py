"""spectral_estimation_compare: 谱估计对比——周期图(非参数) vs Burg AR(参数)."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram
from theme import apply_theme
from palette import cycle
from demo_data import gen_signal

def _burg_psd(x, order, fs, nfreq=512):
    """Burg 法估计 AR 系数并求功率谱."""
    x = np.asarray(x, float); N = len(x)
    f = b = x.copy()
    a = np.zeros(order + 1); a[0] = 1.0
    Dk = np.dot(x, x) * 2 - x[0] ** 2 - x[-1] ** 2
    P = np.dot(x, x) / N
    for k in range(order):
        fk, bk = f[k + 1:], b[k:-1]
        mu = -2.0 * np.dot(fk, bk) / Dk if Dk > 1e-12 else 0.0
        f, b = fk + mu * bk, bk + mu * fk
        a[:k + 2] = a[:k + 2] + mu * a[:k + 2][::-1]
        P *= (1 - mu ** 2)
        Dk = (1 - mu ** 2) * Dk - f[0] ** 2 - b[-1] ** 2
    w = np.linspace(0, np.pi, nfreq)
    z = np.exp(-1j * np.outer(w, np.arange(order + 1)))
    H = 1.0 / np.abs(z @ a) ** 2
    return w / np.pi * (fs / 2), P * H / fs

def make_figure(sig=None, fs=None, title='Spectral estimation: periodogram vs Burg AR'):
    apply_theme(fig_size=(7, 4))
    if sig is None:
        _, sig, fs = gen_signal(components=((50, 1.0), (130, 0.7)), noise=0.4)
    fp, Pp = periodogram(sig, fs=fs)
    fb, Pb = _burg_psd(sig, order=24, fs=fs)
    fig, ax = plt.subplots()
    ax.semilogy(fp, Pp + 1e-12, color=cycle(7), alpha=0.55, lw=1, label='periodogram')
    ax.semilogy(fb, Pb + 1e-12, color=cycle(1), lw=2, label='Burg AR(24)')
    ax.set_xlabel('frequency (Hz)'); ax.set_ylabel('PSD (V^2/Hz)')
    ax.set_xlim(0, fs / 2); ax.set_title(title)
    ax.legend(frameon=False); ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
