"""swing_curve: 多机功角摇摆曲线（暂态稳定）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(t=None, delta=None, t_clear=0.25, title='Rotor angle swing curves'):
    apply_theme()
    if t is None:
        t = np.linspace(0, 3, 600)
        f0, zeta = (1.2, 1.6, 0.9), 0.35
        delta = []
        for i, fi in enumerate(f0):
            d0 = 35 + 12*i
            amp = 38 * np.exp(-zeta*np.clip(t - t_clear, 0, None))
            d = d0 + amp*np.sin(2*np.pi*fi*np.clip(t - t_clear, 0, None))*(t > t_clear)
            delta.append(d)
    fig, ax = plt.subplots()
    for i, d in enumerate(delta):
        ax.plot(t, d, color=cycle(i), label=f'Gen {i+1}')
    ax.axvline(t_clear, color='0.4', linestyle='--', linewidth=1)
    ax.annotate('fault cleared', xy=(t_clear, ax.get_ylim()[1]*0.96),
                xytext=(t_clear + 0.15, ax.get_ylim()[1]*0.96), fontsize=8,
                arrowprops=dict(arrowstyle='->', lw=0.8))
    ax.set_xlabel('time (s)'); ax.set_ylabel('rotor angle (deg)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
