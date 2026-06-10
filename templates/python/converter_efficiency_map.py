"""converter_efficiency_map: 变流器效率 MAP 图（转速×转矩）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Inverter-motor efficiency map'):
    apply_theme()
    n = np.linspace(0, 6000, 200); T = np.linspace(0, 250, 200)
    N, TT = np.meshgrid(n, T)
    env = 250*np.minimum(1, 2500/np.maximum(N, 1))
    eta = 0.97 - 0.10*((N/6000 - 0.55)**2 + (TT/250 - 0.45)**2)           - 0.05*np.exp(-N/600) - 0.03*np.exp(-TT/25)
    eta = np.where(TT <= env, eta*100, np.nan)
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    levels = [80, 85, 88, 90, 92, 93, 94, 95]
    cf = ax.contourf(N, TT, eta, levels=np.linspace(78, 96, 19), cmap='viridis')
    cs = ax.contour(N, TT, eta, levels=levels, colors='w', linewidths=0.7)
    ax.clabel(cs, fmt='%d', fontsize=7)
    ax.plot(n, 250*np.minimum(1, 2500/np.maximum(n, 1)), color='k', lw=1.4)
    ax.set_xlabel('speed (rpm)'); ax.set_ylabel('torque (N·m)'); ax.set_title(title)
    fig.colorbar(cf, ax=ax, label='efficiency (%)', pad=0.02)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
