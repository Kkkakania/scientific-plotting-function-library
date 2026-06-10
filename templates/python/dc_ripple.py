"""dc_ripple: 整流后直流纹波 + 滤波前后对比."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from theme import apply_theme
from palette import cycle

def make_figure(title='DC ripple before/after filter'):
    apply_theme(fig_size=(8, 4))
    fs = 5000; t = np.arange(0, 0.04, 1/fs)
    ac = np.abs(np.sin(2*np.pi*50*t)) * 311
    b, a = butter(4, 30/(fs/2), btype='low')
    dc = filtfilt(b, a, ac)
    fig, ax = plt.subplots()
    ax.plot(t*1000, ac, color='lightgray', linewidth=1, label='rectified')
    ax.plot(t*1000, dc, color=cycle(0), linewidth=1.5, label='after filter')
    ripple_pp = ac.max() - ac.min()
    ax.text(0.02, 0.95, f'ripple = {ripple_pp:.0f} V pp', transform=ax.transAxes,
            verticalalignment='top')
    ax.set_xlabel('t (ms)'); ax.set_ylabel('voltage (V)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
