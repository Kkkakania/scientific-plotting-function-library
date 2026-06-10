"""spectrum_mask: 发射频谱模板 + 实测谱."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Spectrum mask'):
    apply_theme(fig_size=(8, 4))
    f = np.linspace(-30, 30, 600)
    measured = -30 + 25*np.exp(-(f/5)**2) - 0.15*np.abs(f)
    measured += np.random.default_rng(0).normal(0, 1.5, len(f))
    mask = np.where(np.abs(f) < 9.5, 0,
            np.where(np.abs(f) < 12, -25, -45))
    fig, ax = plt.subplots()
    ax.plot(f, measured, color=cycle(0), linewidth=0.8, label='measured')
    ax.plot(f, mask, color='red', linewidth=1.5, label='mask limit')
    ax.fill_between(f, mask, 10, color='red', alpha=0.08)
    ax.set_xlabel('frequency offset (MHz)'); ax.set_ylabel('PSD (dBm/Hz)')
    ax.set_title(title); ax.legend()
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
