"""power_factor_locus: 不同负载下功率因数随时间变化."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Power factor over day'):
    apply_theme()
    h = np.linspace(0, 24, 200)
    pf_resi = 0.95 - 0.05*np.sin((h-12)*np.pi/12)
    pf_indu = 0.75 + 0.15*np.sin((h-12)*np.pi/12)
    pf_comm = 0.85 + 0.08*np.cos((h-14)*np.pi/12)
    fig, ax = plt.subplots()
    for i, (lab, pf) in enumerate([('residential', pf_resi), ('industrial', pf_indu),
                                    ('commercial', pf_comm)]):
        ax.plot(h, pf, color=cycle(i), label=lab)
    ax.axhline(0.9, color='red', linestyle='--', linewidth=0.7, label='target ≥ 0.9')
    ax.set_xlabel('hour'); ax.set_ylabel('power factor'); ax.set_title(title)
    ax.set_xticks(range(0, 25, 3)); ax.legend()
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
