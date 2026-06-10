"""periodogram: 周期图 + 平滑周期图对比."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram, welch
from theme import apply_theme
from palette import cycle

def make_figure(title='Periodogram vs Welch'):
    apply_theme()
    fs = 1000; rng = np.random.default_rng(1)
    sig = np.sin(2*np.pi*60*np.arange(4096)/fs) + 0.6*rng.standard_normal(4096)
    f1, p1 = periodogram(sig, fs=fs)
    f2, p2 = welch(sig, fs=fs, nperseg=512)
    fig, ax = plt.subplots()
    ax.semilogy(f1, p1, color='lightgray', linewidth=0.7, label='periodogram')
    ax.semilogy(f2, p2, color=cycle(0),    linewidth=1.5, label='Welch')
    ax.set_xlabel('frequency (Hz)'); ax.set_ylabel('PSD'); ax.set_title(title)
    ax.legend(); ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
