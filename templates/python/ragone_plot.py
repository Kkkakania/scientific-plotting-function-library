"""ragone_plot: Ragone 图（能量密度 vs 功率密度，储能技术对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from matplotlib.patches import Ellipse

def make_figure(title='Ragone plot of storage technologies'):
    apply_theme()
    techs = [  # (能量密度Wh/kg 中心, 功率密度W/kg 中心, dex_E, dex_P, label)
        (180, 300, 0.25, 0.45, 'Li-ion'),
        (35, 150, 0.30, 0.40, 'Lead-acid'),
        (90, 180, 0.30, 0.45, 'NiMH'),
        (5, 4000, 0.45, 0.50, 'Supercapacitor'),
        (0.05, 8000, 0.50, 0.40, 'Electrolytic cap.'),
        (30, 1200, 0.35, 0.40, 'Flywheel'),
        (450, 60, 0.30, 0.50, 'Fuel cell'),
    ]
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    for i, (E, P, dE, dP, lab) in enumerate(techs):
        ell = Ellipse((np.log10(E), np.log10(P)), 2*dE, 2*dP,
                      facecolor=cycle(i), alpha=0.4, edgecolor=cycle(i), lw=1.2)
        ax.add_patch(ell)
        ax.text(np.log10(E), np.log10(P), lab, ha='center', va='center', fontsize=7.5)
    for tau, lab in [(36, '1 min'), (3600, '1 h'), (36000, '10 h')]:
        x = np.array([-2, 3.2])
        ax.plot(x, x + np.log10(3600/tau), color='0.75', linestyle=':', linewidth=0.9)
        ax.text(2.45, 2.45 + np.log10(3600/tau) + 0.08, lab, fontsize=7, color='0.4', rotation=38)
    ax.set_xlim(-2, 3.2); ax.set_ylim(0.5, 4.3)
    fmt = lambda v: f'$10^{{{int(v)}}}$'
    ax.set_xticks(range(-2, 4)); ax.set_xticklabels([fmt(v) for v in range(-2, 4)])
    ax.set_yticks(range(1, 5)); ax.set_yticklabels([fmt(v) for v in range(1, 5)])
    ax.set_xlabel('specific energy (Wh/kg)'); ax.set_ylabel('specific power (W/kg)')
    ax.set_title(title); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
