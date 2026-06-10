"""voltage_sag: 电压暂降事件（半周期前后包络）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Voltage sag event'):
    apply_theme(fig_size=(8, 4))
    f = 50; fs = 5000
    t = np.linspace(0, 0.5, int(0.5*fs))
    env = np.ones_like(t)
    env[(t >= 0.18) & (t < 0.35)] = 0.5
    sig = env * np.sin(2*np.pi*f*t)
    fig, ax = plt.subplots()
    ax.plot(t*1000, sig, color=cycle(0), linewidth=0.8)
    ax.plot(t*1000, env, color=cycle(1), linewidth=1.5, label='RMS envelope')
    ax.plot(t*1000, -env, color=cycle(1), linewidth=1.5)
    ax.axhline(0, color='gray', linewidth=0.4)
    ax.set_xlabel('t (ms)'); ax.set_ylabel('voltage (pu)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
