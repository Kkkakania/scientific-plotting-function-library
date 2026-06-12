"""beam_steering: 波束扫描方向图叠加（不同扫描角 + 栅瓣警戒）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(n=8, d=0.6, steer_deg=(0, 30, 60), floor_db=-35,
                title='Beam steering, N=8 ULA (d=0.6$\\lambda$)'):
    apply_theme()
    theta = np.linspace(-90, 90, 1801)
    st = np.sin(np.radians(theta))
    fig, ax = plt.subplots()
    for i, s0 in enumerate(steer_deg):
        psi = 2 * np.pi * d * (st - np.sin(np.radians(s0)))
        num = np.sin(n * psi / 2)
        den = n * np.sin(psi / 2)
        af = np.abs(np.where(np.abs(den) < 1e-9, 1.0,
                             num / np.where(np.abs(den) < 1e-9, 1, den)))
        db = np.clip(20 * np.log10(af + 1e-9), floor_db, 0)
        ax.plot(theta, db, color=cycle(i), label=f'steer {s0}$^\\circ$')
        ax.axvline(s0, color=cycle(i), linestyle=':', alpha=0.6, linewidth=1)
    # grating lobe of the 60-deg beam: sin(tg) = sin(60) - 1/d
    tg = np.degrees(np.arcsin(np.sin(np.radians(60)) - 1 / d))
    ax.annotate('grating lobe', xy=(tg, -1.5), xytext=(tg + 8, -8),
                fontsize=8, color=cycle(2),
                arrowprops=dict(arrowstyle='->', color=cycle(2), lw=1))
    ax.axhline(-13.2, color='grey', linestyle='--', linewidth=0.8, alpha=0.7)
    ax.text(-88, -12.6, 'first sidelobe level', fontsize=7, color='grey')
    ax.set_xlim(-90, 90); ax.set_ylim(floor_db, 2)
    ax.set_xlabel('angle (deg)'); ax.set_ylabel('array factor (dB)')
    ax.set_title(title)
    ax.legend(frameon=False, loc='lower left')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
