"""window_compare: 不同窗函数的频谱泄漏对比."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Window function comparison'):
    apply_theme(fig_size=(8, 5))
    N = 512
    wins = [('rect', np.ones(N)),
            ('hann', np.hanning(N)),
            ('hamming', np.hamming(N)),
            ('blackman', np.blackman(N)),
            ('flat-top', np.kaiser(N, 14))]
    fig, (a1, a2) = plt.subplots(1, 2)
    for i, (name, w) in enumerate(wins):
        a1.plot(w, color=cycle(i), label=name)
        W = np.abs(np.fft.rfft(w, 4096))
        W /= W.max()
        a2.plot(np.linspace(0, 0.5, len(W)), 20*np.log10(W + 1e-12),
                color=cycle(i), label=name)
    a1.set_xlabel('sample'); a1.set_ylabel('amplitude'); a1.set_title('Time')
    a1.legend(fontsize=7); a1.grid(True, linestyle=':', alpha=0.5)
    a2.set_xlabel('normalized freq'); a2.set_ylabel('dB'); a2.set_title('Magnitude')
    a2.set_ylim(-100, 5); a2.set_xlim(0, 0.05)
    a2.legend(fontsize=7); a2.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
