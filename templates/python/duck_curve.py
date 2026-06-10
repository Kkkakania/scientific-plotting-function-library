"""duck_curve: 净负荷鸭子曲线（光伏渗透率逐年上升）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(title='Duck curve: net load vs PV penetration'):
    apply_theme()
    t = np.linspace(0, 24, 480)
    load = 20 + 6*np.exp(-0.5*((t - 9)/2.6)**2) + 9*np.exp(-0.5*((t - 19.5)/2.0)**2)
    pv_shape = np.exp(-0.5*((t - 12.5)/2.7)**2)*(np.abs(t - 12.5) < 7)
    cmap = sequential('blue')
    fig, ax = plt.subplots()
    years = [2018, 2020, 2022, 2024, 2026]
    for i, yr in enumerate(years):
        net = load - (2.2*i)*pv_shape
        ax.plot(t, net, color=cmap(0.25 + 0.75*i/(len(years)-1)), label=str(yr))
    ax.annotate('growing ramp', xy=(16.6, 17), xytext=(12.6, 12.5),
                arrowprops=dict(arrowstyle='->', lw=0.9), fontsize=8)
    ax.set_xlabel('hour of day'); ax.set_ylabel('net load (GW)'); ax.set_title(title)
    ax.set_xlim(0, 24); ax.legend(title='year', fontsize=7)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
