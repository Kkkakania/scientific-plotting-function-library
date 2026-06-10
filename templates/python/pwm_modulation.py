"""pwm_modulation: 正弦 PWM 调制波形（载波+调制+输出）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Sinusoidal PWM'):
    apply_theme(fig_size=(9, 4))
    t = np.linspace(0, 0.02, 5000)
    mod = 0.8 * np.sin(2*np.pi*50*t)
    carrier = 2/np.pi * np.arcsin(np.sin(2*np.pi*1000*t))
    out = np.where(mod > carrier, 1, -1)
    fig, ax = plt.subplots()
    ax.plot(t*1000, carrier, color='lightgray', linewidth=0.7, label='carrier')
    ax.plot(t*1000, mod, color=cycle(0), label='modulation')
    ax.plot(t*1000, out*0.6, color=cycle(1), linewidth=0.8, alpha=0.7, label='output')
    ax.set_xlabel('t (ms)'); ax.set_ylabel('value'); ax.set_title(title)
    ax.legend(loc='upper right'); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
