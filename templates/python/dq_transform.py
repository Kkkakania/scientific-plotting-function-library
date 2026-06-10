"""dq_transform: abc → dq0 旋转坐标变换前后波形."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='abc → dq0 transform'):
    apply_theme(fig_size=(8, 5))
    f = 50; t = np.linspace(0, 0.1, 1000); w = 2*np.pi*f
    a = np.sin(w*t); b = np.sin(w*t - 2*np.pi/3); c = np.sin(w*t + 2*np.pi/3)
    theta = w*t
    d = (2/3)*(a*np.cos(theta) + b*np.cos(theta - 2*np.pi/3) + c*np.cos(theta + 2*np.pi/3))
    q = -(2/3)*(a*np.sin(theta) + b*np.sin(theta - 2*np.pi/3) + c*np.sin(theta + 2*np.pi/3))
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(t*1000, a, color=cycle(0), label='a')
    ax1.plot(t*1000, b, color=cycle(1), label='b')
    ax1.plot(t*1000, c, color=cycle(2), label='c')
    ax1.set_ylabel('abc'); ax1.set_title(title); ax1.legend(loc='upper right')
    ax1.grid(True, linestyle=':', alpha=0.5)
    ax2.plot(t*1000, d, color=cycle(3), label='d')
    ax2.plot(t*1000, q, color=cycle(4), label='q')
    ax2.set_xlabel('t (ms)'); ax2.set_ylabel('dq'); ax2.legend(loc='upper right')
    ax2.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
