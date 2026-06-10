"""load_curve_daily: 24h 负荷曲线 + 峰谷标注."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Daily load profile'):
    apply_theme(fig_size=(8, 4))
    h = np.arange(24)
    load = 50 + 20*np.sin((h - 6)*np.pi/12) + 15*np.exp(-((h-19)**2)/8)
    fig, ax = plt.subplots()
    ax.plot(h, load, '-o', color=cycle(0), markersize=5)
    ax.fill_between(h, 0, load, color=cycle(0), alpha=0.2)
    peak = h[np.argmax(load)]; trough = h[np.argmin(load)]
    ax.scatter([peak, trough], [load[peak], load[trough]],
               s=80, c=['red', 'green'], zorder=5)
    ax.annotate(f'peak {load[peak]:.0f}', (peak, load[peak]),
                xytext=(5, -15), textcoords='offset points')
    ax.annotate(f'valley {load[trough]:.0f}', (trough, load[trough]),
                xytext=(5, 10), textcoords='offset points')
    ax.set_xlabel('hour'); ax.set_ylabel('load (MW)'); ax.set_title(title)
    ax.set_xticks(range(0, 24, 3))
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
