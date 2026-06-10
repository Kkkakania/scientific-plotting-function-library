"""cepstrum: 倒谱（用于谐波识别、回声检测）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Cepstrum'):
    apply_theme(fig_size=(8, 4))
    fs = 8000; t = np.arange(0, 0.1, 1/fs)
    f0 = 200
    sig = sum(0.6**k * np.sin(2*np.pi*(k+1)*f0*t) for k in range(8))
    sig += 0.05*np.random.default_rng(0).standard_normal(len(t))
    spec = np.fft.rfft(sig)
    log_mag = np.log(np.abs(spec) + 1e-12)
    cep = np.fft.irfft(log_mag).real
    quef = np.arange(len(cep)) / fs
    fig, ax = plt.subplots()
    ax.plot(quef*1000, cep, color=cycle(0))
    ax.set_xlim(0, 20)
    ax.axvline(1000/f0, color='red', linestyle='--', linewidth=0.8, label=f'1/f₀ = {1000/f0:.1f} ms')
    ax.set_xlabel('quefrency (ms)'); ax.set_ylabel('cepstrum')
    ax.set_title(title); ax.legend()
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
