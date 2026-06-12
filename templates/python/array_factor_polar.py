"""array_factor_polar: 均匀线阵阵因子极坐标对比（4/8/16 元）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(elements=(4, 8, 16), d=0.5, floor_db=-40,
                title='Uniform linear array factor (d=0.5$\\lambda$)'):
    apply_theme(fig_size=(6, 6))
    theta = np.linspace(-np.pi, np.pi, 1441)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    for i, n in enumerate(elements):
        psi = 2 * np.pi * d * np.sin(theta)
        num = np.sin(n * psi / 2)
        den = n * np.sin(psi / 2)
        af = np.abs(np.where(np.abs(den) < 1e-9, 1.0,
                             num / np.where(np.abs(den) < 1e-9, 1, den)))
        db = np.clip(20 * np.log10(af + 1e-9), floor_db, 0)
        ax.plot(theta, db - floor_db, color=cycle(i), label=f'N={n}')
    ax.set_theta_zero_location('N')
    ax.set_rlim(0, -floor_db)
    ax.set_rticks([10, 20, 30, 40])
    ax.set_yticklabels(['-30', '-20', '-10', '0 dB'])
    ax.set_title(title, pad=18)
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.14), ncol=3, frameon=False)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
