"""grid_frequency_response: 电网频率响应（不同惯量水平对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Frequency response after generation loss'):
    apply_theme()
    t = np.linspace(0, 30, 1200)
    fig, ax = plt.subplots()
    for i, (H, label) in enumerate([(6, 'H = 6 s (high inertia)'),
                                    (4, 'H = 4 s'),
                                    (2, 'H = 2 s (low inertia)')]):
        wn = 0.45*np.sqrt(4/H); zeta = 0.5
        wd = wn*np.sqrt(1 - zeta**2)
        df = -0.65*(4/H)**0.35*np.exp(-zeta*wn*t)*np.sin(wd*t)/(wd*4)
        f = 50 + df - 0.05*(1 - np.exp(-t/8))
        ax.plot(t, f, color=cycle(i), label=label)
        ax.plot(t[np.argmin(f)], f.min(), 'v', color=cycle(i), ms=5)
    ax.axhline(49.8, color='0.4', linestyle='--', linewidth=0.9)
    ax.text(20.5, 49.803, 'UFLS threshold', fontsize=8)
    ax.set_xlabel('time (s)'); ax.set_ylabel('frequency (Hz)'); ax.set_title(title)
    ax.legend(loc='lower right'); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
