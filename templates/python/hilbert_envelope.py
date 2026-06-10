"""hilbert_envelope: 解析信号的瞬时频率."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
from theme import apply_theme
from palette import cycle

def make_figure(title='Instantaneous frequency'):
    apply_theme(fig_size=(8, 4))
    fs = 1000; t = np.arange(0, 2, 1/fs)
    sig = chirp(t, f0=20, f1=150, t1=2, method='linear')
    analytic = hilbert(sig)
    inst_phase = np.unwrap(np.angle(analytic))
    inst_freq = np.diff(inst_phase) / (2*np.pi) * fs
    fig, ax = plt.subplots()
    ax.plot(t[1:], inst_freq, color=cycle(0), linewidth=1)
    ax.set_xlabel('t (s)'); ax.set_ylabel('instantaneous frequency (Hz)')
    ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
