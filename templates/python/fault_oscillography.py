"""fault_oscillography: 三相短路故障录波（含直流分量衰减）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(t_fault=0.04, title='Three-phase fault oscillography'):
    apply_theme()
    t = np.linspace(0, 0.2, 4000); w = 2*np.pi*50
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(6, 5))
    for i, (ax, ph) in enumerate(zip(axes, 'abc')):
        th = -2*np.pi*i/3
        pre = np.sin(w*t + th)
        tau = 0.045
        dc = -6*np.sin(th + w*t_fault)*np.exp(-(t - t_fault)/tau)
        post = 6*np.sin(w*t + th) + dc
        ia = np.where(t < t_fault, pre, post)
        ax.plot(t*1000, ia, color=cycle(i), linewidth=1.2)
        ax.axvline(t_fault*1000, color='0.4', linestyle='--', linewidth=0.8)
        ax.set_ylabel(f'i_{ph} (p.u.)')
        ax.grid(True, linestyle=':', alpha=0.5)
    axes[0].set_title(title); axes[-1].set_xlabel('time (ms)')
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
