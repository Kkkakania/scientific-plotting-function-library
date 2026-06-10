"""vswr_curve: VSWR 与回波损耗随频率变化."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='VSWR vs frequency'):
    apply_theme()
    f = np.linspace(1.5, 3.0, 400)
    f0 = 2.4
    gamma = 0.05 + 0.8*np.exp(-((f - f0)/0.05)**2)
    vswr = (1 + gamma) / (1 - gamma + 1e-9)
    rl = -20*np.log10(gamma + 1e-9)
    fig, ax1 = plt.subplots()
    ax1.plot(f, vswr, color=cycle(0))
    ax1.set_ylabel('VSWR', color=cycle(0))
    ax1.tick_params(axis='y', labelcolor=cycle(0))
    ax1.axhline(2, color='gray', linestyle='--', linewidth=0.7)
    ax2 = ax1.twinx()
    ax2.plot(f, rl, '--', color=cycle(1))
    ax2.set_ylabel('return loss (dB)', color=cycle(1))
    ax2.tick_params(axis='y', labelcolor=cycle(1))
    ax2.spines['right'].set_visible(True); ax2.invert_yaxis()
    ax1.set_xlabel('frequency (GHz)'); ax1.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
