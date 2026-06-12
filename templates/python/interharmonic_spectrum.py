"""interharmonic_spectrum: 间谐波频谱（整数次谐波与间谐波分色柱状）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(title='Harmonic and interharmonic spectrum'):
    apply_theme(fig_size=(7, 4))
    rng = np.random.default_rng(1)
    f1 = 50.0
    # integer harmonics: typical 6-pulse drive pattern (5,7,11,13...) + noise floor
    h_orders = np.arange(2, 20)
    h_amp = np.full(h_orders.size, 0.15)
    for k, a in zip([5, 7, 11, 13, 17], [4.5, 3.2, 1.8, 1.4, 0.8]):
        h_amp[h_orders == k] = a
    h_amp += rng.uniform(0, 0.1, h_orders.size)
    # interharmonics from a cycloconverter / doubly-fed drive: sidebands
    # at fi = |f_drive*k +/- f1*m| -- not integer multiples of 50 Hz
    ih_freq = np.array([128., 172., 282., 328., 432., 628.])
    ih_amp = np.array([0.9, 0.7, 0.55, 0.4, 0.3, 0.2]) + rng.uniform(0, 0.05, 6)
    fig, ax = plt.subplots()
    ax.bar(h_orders*f1, h_amp, width=9, color=cycle(0), label='integer harmonics')
    ax.bar(ih_freq, ih_amp, width=9, color=cycle(1), label='interharmonics')
    ax.set_xlabel('frequency (Hz)'); ax.set_ylabel('amplitude (% of fundamental)')
    ax.set_title(title)
    ax.set_xlim(50, 1000)
    ax.legend()
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
