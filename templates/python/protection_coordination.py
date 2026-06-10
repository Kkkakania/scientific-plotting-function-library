"""protection_coordination: 阶段式过流保护配合图（log-log 时间-电流曲线 + ΔT 标注）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def _staged_curve(i_pick3, tms, i_pick2, t2, i_pick1, t1, i_max=20000.0):
    """三段式：III 段反时限（IEC SI）→ II 段定时限 → I 段速断."""
    def t_of(i):
        i = np.asarray(i, dtype=float)
        t = tms*0.14/((i/i_pick3)**0.02 - 1)            # IEC standard inverse
        t = np.where(i >= i_pick2, np.minimum(t, t2), t)
        t = np.where(i >= i_pick1, t1, t)
        return t
    i = np.geomspace(i_pick3*1.05, i_max, 600)
    # insert step edges for clean vertical transitions
    for edge in (i_pick2, i_pick1):
        i = np.sort(np.concatenate([i, [edge*(1 - 1e-9), edge]]))
    return i, t_of(i)

def make_figure(title='Overcurrent protection coordination'):
    apply_theme(fig_size=(6.5, 4.8))
    # downstream relay R1 (feeder) and upstream relay R2 (transformer)
    i1, t1 = _staged_curve(200, 0.05, 800, 0.30, 2000, 0.05)
    i2, t2 = _staged_curve(400, 0.10, 1200, 0.62, 4000, 0.37)
    fig, ax = plt.subplots()
    ax.loglog(i1, t1, color=cycle(0), label='R1 downstream (3-stage)')
    ax.loglog(i2, t2, color=cycle(1), label='R2 upstream (3-stage)')
    # coordination margin at a common fault current
    i_f = 1500.0
    ta = np.interp(i_f, i1, t1); tb = np.interp(i_f, i2, t2)
    ax.annotate('', xy=(i_f, tb), xytext=(i_f, ta),
                arrowprops=dict(arrowstyle='<->', color=cycle(3), lw=1.2))
    ax.text(i_f*1.1, np.sqrt(ta*tb),
            f'$\\Delta T$ = {tb - ta:.2f} s $\\geq$ 0.3 s',
            color=cycle(3), fontsize=8, va='center')
    ax.axvline(i_f, color=cycle(3), linestyle=':', alpha=0.5, lw=0.8)
    ax.set_xlabel('fault current (A)'); ax.set_ylabel('operating time (s)')
    ax.set_title(title)
    ax.set_xlim(150, 20000); ax.set_ylim(0.02, 20)
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    ax.legend(frameon=False, loc='upper right')
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
