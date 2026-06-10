"""eye_diagram: 数字通信眼图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Eye diagram'):
    apply_theme()
    rng = np.random.default_rng(1)
    sps = 32; n_sym = 200
    bits = rng.integers(0, 2, n_sym)*2 - 1
    sig = np.repeat(bits, sps).astype(float)
    # 简单升余弦平滑
    k = np.hanning(sps); k = k/k.sum()
    sig = np.convolve(sig, k, mode='same')
    sig += 0.1*rng.standard_normal(len(sig))
    fig, ax = plt.subplots()
    for i in range(50, n_sym-1, 1):
        seg = sig[i*sps : (i+2)*sps]
        ax.plot(np.arange(len(seg)), seg, color=cycle(0), alpha=0.3, linewidth=0.6)
    ax.set_xlabel('sample'); ax.set_ylabel('amplitude')
    ax.set_title(title); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
