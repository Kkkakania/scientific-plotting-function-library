"""envelope_detect: Hilbert 变换求解析信号包络."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert
from theme import apply_theme
from palette import cycle

def make_figure(title='Hilbert envelope'):
    apply_theme(fig_size=(8, 4))
    fs = 5000; t = np.arange(0, 0.5, 1/fs)
    env = 1 + 0.5*np.cos(2*np.pi*5*t)
    sig = env * np.sin(2*np.pi*80*t)
    analytic = hilbert(sig)
    fig, ax = plt.subplots()
    ax.plot(t*1000, sig, color='lightgray', linewidth=0.7, label='signal')
    ax.plot(t*1000, np.abs(analytic), color=cycle(0), linewidth=1.5, label='|envelope|')
    ax.set_xlabel('t (ms)'); ax.set_ylabel('amplitude'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
