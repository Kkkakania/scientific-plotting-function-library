"""harmonic_heatmap: 谐波时变热力图（谐波次数 × 时间，幅值着色）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential


def make_figure(amp=None, title='Harmonic amplitude vs time of day'):
    apply_theme(fig_size=(7, 4))
    orders = np.arange(2, 26)
    hours = np.linspace(0, 24, 97)            # 15-min resolution
    if amp is None:
        rng = np.random.default_rng(2)
        # characteristic 6-pulse orders dominate; magnitude follows the
        # industrial load profile (high 8h-18h), plus measurement noise
        base = np.full(orders.size, 0.15)
        for k, a in zip([3, 5, 7, 11, 13, 17, 19, 23], [1.2, 4.0, 2.8, 1.6, 1.3, 0.7, 0.6, 0.4]):
            base[orders == k] = a
        load = 0.35 + 0.65*np.exp(-((hours - 13)/4.2)**2)
        amp = base[:, None]*load[None, :]
        amp += rng.uniform(0, 0.08, amp.shape)
    fig, ax = plt.subplots()
    pm = ax.pcolormesh(hours, orders, amp, cmap=sequential('blue'),
                       shading='auto')
    cb = fig.colorbar(pm, ax=ax, pad=0.02)
    cb.set_label('amplitude (% of fundamental)')
    ax.set_xlabel('time of day (h)'); ax.set_ylabel('harmonic order')
    ax.set_title(title)
    ax.set_xticks(np.arange(0, 25, 4))
    ax.set_yticks([3, 5, 7, 11, 13, 17, 19, 23])
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
