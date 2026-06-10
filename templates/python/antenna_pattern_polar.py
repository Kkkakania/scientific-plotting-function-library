"""antenna_pattern_polar: 天线方向图（极坐标 dB 刻度）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Antenna pattern'):
    apply_theme(fig_size=(6, 6))
    theta = np.linspace(0, 2*np.pi, 720)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    for i, N in enumerate([2, 4, 8]):
        psi = np.pi * np.cos(theta)
        gain = np.abs(np.sin(N*psi/2) / (N*np.sin(psi/2) + 1e-12))
        dB = 20*np.log10(gain + 1e-6)
        dB = np.clip(dB, -40, 0)
        ax.plot(theta, dB + 40, color=cycle(i), label=f'N = {N}')
    ax.set_rmax(40); ax.set_rticks([10, 20, 30, 40])
    ax.set_yticklabels(['-30', '-20', '-10', '0 dB'])
    ax.set_title(title); ax.legend(loc='lower right', bbox_to_anchor=(1.2, 0))
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
