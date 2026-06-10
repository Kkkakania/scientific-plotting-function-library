"""inrush_current: 变压器/电机励磁涌流的衰减波形."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Inrush current'):
    apply_theme(fig_size=(8, 4))
    f = 50; fs = 5000
    t = np.linspace(0, 0.4, int(0.4*fs))
    envelope = 8*np.exp(-t/0.05) + 1
    i = envelope * np.sin(2*np.pi*f*t - np.pi/2)
    i = np.where(i > 0, i, 0.1*i)
    fig, ax = plt.subplots()
    ax.plot(t*1000, i, color=cycle(0), linewidth=0.8)
    ax.plot(t*1000, envelope, '--', color=cycle(1), linewidth=1.2, label='envelope')
    ax.set_xlabel('t (ms)'); ax.set_ylabel('current (pu)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
