"""root_locus: 根轨迹（K 变化时极点在 s 平面的移动）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle, sequential

def make_figure(title='Root locus'):
    apply_theme(fig_size=(6, 5))
    poles_OL = np.array([0, -2, -5])
    Ks = np.logspace(-1, 2.3, 80)
    locus = np.zeros((len(Ks), 3), dtype=complex)
    for i, K in enumerate(Ks):
        coefs = np.poly(poles_OL).real
        coefs[-1] += K
        locus[i] = np.roots(coefs)
    cmap = sequential(hue='blue')
    fig, ax = plt.subplots()
    for j in range(3):
        ax.scatter(locus[:, j].real, locus[:, j].imag, c=Ks, cmap=cmap, s=12)
    ax.plot(poles_OL.real, poles_OL.imag, 'x', markersize=12, color='red', markeredgewidth=2, label='open-loop poles')
    ax.axhline(0, color='gray', linewidth=0.5); ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlabel('Re'); ax.set_ylabel('Im'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
