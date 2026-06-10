"""ev_charging_load: 电动车充电负荷叠加（无序/有序对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='EV charging load: uncontrolled vs smart'):
    apply_theme()
    t = np.linspace(0, 24, 480)
    base = 55 + 14*np.exp(-0.5*((t - 10)/3.0)**2) + 20*np.exp(-0.5*((t - 19.5)/2.2)**2)
    ev_unc = 12*np.exp(-0.5*((t - 19)/1.6)**2) + 4*np.exp(-0.5*((t - 8.5)/1.2)**2)
    ev_smart = 12*np.exp(-0.5*((t - 2.5)/2.6)**2) + 4*np.exp(-0.5*((t - 13)/2.2)**2)
    fig, ax = plt.subplots()
    ax.plot(t, base, color='0.45', linestyle='--', linewidth=1.2, label='base load')
    ax.plot(t, base + ev_unc, color=cycle(1), label='uncontrolled charging')
    ax.plot(t, base + ev_smart, color=cycle(2), label='smart charging')
    ax.fill_between(t, base, base + ev_unc, color=cycle(1), alpha=0.18)
    ax.fill_between(t, base, base + ev_smart, color=cycle(2), alpha=0.18)
    ax.set_xlabel('hour of day'); ax.set_ylabel('load (MW)'); ax.set_title(title)
    ax.set_xlim(0, 24); ax.legend(fontsize=8); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
