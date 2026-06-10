"""harmonic_spectrum: 谐波频谱（条状显示 2~25 次）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Harmonic spectrum'):
    apply_theme()
    rng = np.random.default_rng(0)
    orders = np.arange(1, 26)
    amps = np.zeros(25); amps[0] = 1.0
    amps[[2, 4, 6, 10]] = [0.3, 0.18, 0.08, 0.05]
    amps += rng.uniform(0, 0.02, 25)
    fig, ax = plt.subplots()
    ax.bar(orders, amps*100, color=cycle(0), width=0.6)
    ax.set_xlabel('harmonic order'); ax.set_ylabel('amplitude (% of fundamental)')
    ax.set_title(title); ax.set_xticks(orders[::2])
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
