"""frequency_drift: 电网频率漂移 + 死区."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Grid frequency drift'):
    apply_theme(fig_size=(8, 4))
    rng = np.random.default_rng(2)
    t = np.linspace(0, 60, 600)
    f = 50 + 0.03*np.sin(t/5) + rng.normal(0, 0.01, 600)
    f[300:340] += 0.18
    fig, ax = plt.subplots()
    ax.plot(t, f, color=cycle(0), linewidth=0.8)
    ax.axhspan(49.95, 50.05, color='green', alpha=0.15, label='dead band ±0.05 Hz')
    ax.axhline(50, color='gray', linewidth=0.5)
    ax.set_xlabel('t (s)'); ax.set_ylabel('frequency (Hz)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
