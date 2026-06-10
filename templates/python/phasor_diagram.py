"""phasor_diagram: 三相电压/电流相量图（极坐标箭头，电流滞后 30°）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from theme import apply_theme
from palette import cycle

def make_figure(v_mag=1.0, i_mag=0.8, phi_deg=30.0, title='Three-phase phasor diagram'):
    apply_theme(fig_size=(5.2, 5.2))
    v_ang = np.deg2rad([0.0, -120.0, 120.0])           # Va, Vb, Vc
    i_ang = v_ang - np.deg2rad(phi_deg)                 # currents lag by phi
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    names_v = ['$V_a$', '$V_b$', '$V_c$']
    names_i = ['$I_a$', '$I_b$', '$I_c$']
    for k in range(3):
        c = cycle(k)
        ax.annotate('', xy=(v_ang[k], v_mag), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='-|>', color=c, lw=1.8,
                                    shrinkA=0, shrinkB=0))
        ax.annotate('', xy=(i_ang[k], i_mag), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='-|>', color=c, lw=1.4,
                                    linestyle='--', shrinkA=0, shrinkB=0))
        ax.text(v_ang[k], v_mag*1.16,
                f'{names_v[k]}\n{v_mag:.2f} ang {np.rad2deg(v_ang[k]):.0f}°',
                ha='center', va='center', color=c, fontsize=8)
        ax.text(i_ang[k], i_mag*0.62,
                f'{names_i[k]}\n{i_mag:.2f} ang {np.rad2deg(i_ang[k]):.0f}°',
                ha='center', va='center', color=c, fontsize=7)
    ax.set_rmax(v_mag*1.35); ax.set_rticks([0.5, 1.0])
    ax.set_rlabel_position(45)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.set_title(title, pad=18)
    ax.set_xlabel('angle (deg)'); ax.set_ylabel('magnitude (p.u.)', labelpad=28)
    handles = [Line2D([], [], color='0.3', lw=1.8, label='voltage (solid)'),
               Line2D([], [], color='0.3', lw=1.4, linestyle='--',
                      label=f'current (lags {phi_deg:.0f}°)')]
    ax.legend(handles=handles, loc='upper left', bbox_to_anchor=(0.92, 1.08),
              frameon=False)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
