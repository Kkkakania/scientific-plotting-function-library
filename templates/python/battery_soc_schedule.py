"""battery_soc_schedule: 储能充放电调度（功率 + SOC 双轴）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='BESS dispatch and state of charge'):
    apply_theme()
    h = np.arange(24)
    P = np.array([1.2, 1.4, 1.5, 1.5, 1.3, 0.6, -0.4, -1.2, -0.8, -0.2, 0.4, 0.8,
                  1.0, 0.6, 0.2, -0.3, -1.0, -1.6, -1.8, -1.4, -0.6, 0.2, 0.8, 1.1])
    soc = 35 + np.cumsum(-P)*100/ (2*24/1.5) ; soc = np.clip(soc, 10, 95)
    fig, ax1 = plt.subplots()
    colors = [cycle(0) if p >= 0 else cycle(1) for p in P]
    ax1.bar(h, P, color=colors, width=0.8, alpha=0.85)
    ax1.axhline(0, color='0.3', linewidth=0.8)
    ax1.set_xlabel('hour'); ax1.set_ylabel('power (MW)  +charge / −discharge')
    ax2 = ax1.twinx()
    ax2.plot(h, soc, 'o-', color=cycle(2), ms=4, label='SOC')
    ax2.set_ylabel('SOC (%)'); ax2.set_ylim(0, 100)
    ax2.spines['right'].set_visible(True)
    ax1.set_title(title)
    ax1.grid(True, axis='y', linestyle=':', alpha=0.5)
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    ax1.legend(handles=[Patch(color=cycle(0), label='charging'),
                        Patch(color=cycle(1), label='discharging'),
                        Line2D([], [], color=cycle(2), marker='o', label='SOC')],
               loc='upper left', fontsize=7)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
