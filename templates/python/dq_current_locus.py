"""dq_current_locus: dq 轴电流轨迹（启动暂态螺旋收敛到稳态点 + MTPA 虚线）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(id_ss=-12.0, iq_ss=35.0, title='dq-axis current locus'):
    apply_theme(fig_size=(6, 5))
    # transient: damped spiral converging from (0,0) to steady-state point
    t = np.linspace(0, 0.12, 800)
    z_ss = id_ss + 1j*iq_ss
    z = z_ss*(1 - np.exp(-(35 + 1j*2*np.pi*60)*t))
    # MTPA curve (dashed), parabolic approximation through the steady point
    iq_m = np.linspace(0, 1.25*iq_ss, 200)
    id_m = id_ss*(iq_m/iq_ss)**2
    fig, ax = plt.subplots()
    ax.plot(id_m, iq_m, linestyle='--', color=cycle(1), label='MTPA trajectory')
    ax.plot(z.real, z.imag, color=cycle(0), lw=1.2, label='start-up transient')
    ax.plot(0, 0, marker='o', color=cycle(2), linestyle='none', label='start (0, 0)')
    ax.plot(id_ss, iq_ss, marker='*', markersize=11, color=cycle(3),
            linestyle='none', label='steady-state point')
    ax.annotate(f'({id_ss:.0f}, {iq_ss:.0f}) A', xy=(id_ss, iq_ss),
                xytext=(id_ss + 4, iq_ss + 3), fontsize=8)
    ax.set_xlabel('$i_d$ (A)'); ax.set_ylabel('$i_q$ (A)'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.legend(frameon=False, loc='lower left')
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
