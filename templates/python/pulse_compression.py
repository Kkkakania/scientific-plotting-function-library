"""pulse_compression: LFM 脉冲压缩（匹配滤波 + 加窗旁瓣对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(T=10e-6, B=10e6, oversample=8, title='LFM pulse compression'):
    apply_theme(fig_size=(6, 5))
    K = B / T                                   # chirp rate
    fs = oversample * B
    n = int(round(fs * T))
    t = np.linspace(-T / 2, T / 2, n, endpoint=False)
    st = np.exp(1j * np.pi * K * t**2)          # LFM chirp
    ht = np.conj(st[::-1])                      # matched filter

    def compress(sig, win):
        out = np.convolve(sig * win, ht)
        mag = np.abs(out)
        return 20 * np.log10(mag / mag.max() + 1e-12)

    rect_db = compress(st, np.ones(n))
    hamm_db = compress(st, np.hamming(n))
    tau = (np.arange(2 * n - 1) - (n - 1)) / fs * 1e6   # lag, us

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(t * 1e6, st.real, color=cycle(0), lw=0.8, label='Re s(t)')
    ax1.plot(t * 1e6, K * t / 1e6 / (B / 2e6), color=cycle(1), lw=1.2,
             label='inst. freq (norm.)')
    ax1.set_xlabel('time (μs)'); ax1.set_ylabel('amplitude')
    ax1.set_title(f'LFM chirp, TBP = {B * T:.0f}')
    ax1.legend(frameon=False, loc='upper left', fontsize=8)
    ax1.grid(True, linestyle=':', alpha=0.5)

    ax2.plot(tau, rect_db, color=cycle(0), lw=1.0, label='rectangular')
    ax2.plot(tau, hamm_db, color=cycle(1), lw=1.0, label='hamming')
    ax2.set_xlim(-1.5, 1.5); ax2.set_ylim(-80, 3)
    ax2.set_xlabel('delay (μs)'); ax2.set_ylabel('output (dB)')
    ax2.set_title('matched-filter output')
    ax2.legend(frameon=False); ax2.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(title)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
