"""unbalance_phasor: 三相不平衡相量分解（正/负/零序三组相量子图）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(vabc=None, title='Symmetrical component decomposition'):
    apply_theme(fig_size=(8, 3.2))
    a = np.exp(2j*np.pi/3)
    if vabc is None:
        # unbalanced three-phase set (single-phase load on phase B)
        vabc = np.array([1.00*np.exp(1j*np.deg2rad(0)),
                         0.78*np.exp(-1j*np.deg2rad(118)),
                         0.95*np.exp(1j*np.deg2rad(123))])
    # Fortescue transform: [V0, V1, V2] = (1/3) F [Va, Vb, Vc]
    F = np.array([[1, 1, 1], [1, a, a**2], [1, a**2, a]])/3
    v0, v1, v2 = F @ vabc
    # each sequence is itself a balanced three-phase set
    sets = [('Positive seq', [v1, a**2*v1, a*v1]),
            ('Negative seq', [v2, a*v2, a**2*v2]),
            ('Zero seq',     [v0, v0, v0])]
    vuf = abs(v2)/abs(v1)*100
    fig, axes = plt.subplots(1, 3, subplot_kw={'projection': 'polar'})
    for ax, (name, comp) in zip(axes, sets):
        for i, (v, lab) in enumerate(zip(comp, 'ABC')):
            ax.annotate('', xy=(np.angle(v), abs(v)), xytext=(0, 0),
                        arrowprops=dict(arrowstyle='->', color=cycle(i),
                                        linewidth=1.5))
            ax.text(np.angle(v), abs(v)*1.18 + 0.06, lab, color=cycle(i),
                    fontsize=8, ha='center', va='center')
        ax.set_rlim(0, 1.15)
        ax.set_rticks([0.5, 1.0]); ax.set_yticklabels([])
        ax.set_xticks(np.deg2rad([0, 90, 180, 270]))
        ax.tick_params(labelsize=7)
        mag = abs(comp[0])
        ax.set_title(f'{name}\n|V| = {mag:.3f} pu', fontsize=8)
    fig.suptitle(f'{title}  (VUF = {vuf:.1f}%)', fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
