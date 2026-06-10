"""group_delay: 滤波器群延迟."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, group_delay as _gd
from theme import apply_theme
from palette import cycle

def make_figure(title='Group delay'):
    apply_theme()
    fig, ax = plt.subplots()
    for i, order in enumerate([2, 4, 6, 8]):
        b, a = butter(order, 0.3)
        w, gd = _gd((b, a), w=512)
        ax.plot(w/np.pi, gd, color=cycle(i), label=f'order {order}')
    ax.set_xlabel('normalized frequency (×π rad/sample)')
    ax.set_ylabel('group delay (samples)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
