"""phase_margin: Bode 图上标注增益裕度/相位裕度."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Gain/phase margin'):
    apply_theme(fig_size=(7, 5.5))
    w = np.logspace(-1, 3, 1000); s = 1j*w
    G = 10 / (s * (s/5 + 1) * (s/50 + 1))
    mag = 20*np.log10(np.abs(G)); phs = np.unwrap(np.angle(G))*180/np.pi
    # 找 0dB 穿越和 -180 穿越
    i_gc = np.argmin(np.abs(mag))
    i_pc = np.argmin(np.abs(phs + 180))
    PM = 180 + phs[i_gc]
    GM = -mag[i_pc]
    fig, (a1, a2) = plt.subplots(2, 1, sharex=True)
    a1.semilogx(w, mag, color=cycle(0))
    a1.axhline(0, color='gray', linewidth=0.7)
    a1.vlines(w[i_pc], -GM, 0, color='red', linewidth=2)
    a1.text(w[i_pc]*1.2, -GM/2, f'GM = {GM:.1f} dB', color='red')
    a1.set_ylabel('mag (dB)'); a1.grid(True, which='both', linestyle=':', alpha=0.5)
    a2.semilogx(w, phs, color=cycle(0))
    a2.axhline(-180, color='gray', linewidth=0.7)
    a2.vlines(w[i_gc], -180, phs[i_gc], color='red', linewidth=2)
    a2.text(w[i_gc]*1.2, (-180+phs[i_gc])/2, f'PM = {PM:.1f}°', color='red')
    a2.set_xlabel('ω (rad/s)'); a2.set_ylabel('phase (°)')
    a2.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.suptitle(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
