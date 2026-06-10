"""coherence_plot: 两信号的相干函数."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import coherence
from theme import apply_theme
from palette import cycle

def make_figure(title='Magnitude-squared coherence'):
    apply_theme()
    fs = 1000; rng = np.random.default_rng(2)
    n = 4096; common = np.sin(2*np.pi*70*np.arange(n)/fs)
    x = common + 0.7*rng.standard_normal(n)
    y = 0.8*common + 0.7*rng.standard_normal(n)
    f, Cxy = coherence(x, y, fs=fs, nperseg=512)
    fig, ax = plt.subplots()
    ax.plot(f, Cxy, color=cycle(0))
    ax.axvline(70, color='red', linestyle='--', linewidth=0.7, label='common at 70 Hz')
    ax.set_xlabel('frequency (Hz)'); ax.set_ylabel('coherence γ²'); ax.set_title(title)
    ax.set_xlim(0, 250); ax.legend()
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
