"""ber_waterfall_3d: BER 三维瀑布（SNR x 调制阶数 x 误码率 log 面）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
from theme import apply_theme
from palette import cycle


def make_figure(title='M-QAM BER surface'):
    apply_theme(fig_size=(6.8, 5.2))
    ebn0_db = np.linspace(0, 24, 49)
    ks = np.array([2, 4, 6, 8])
    names = ['QPSK', '16-QAM', '64-QAM', '256-QAM']
    gamma = 10 ** (ebn0_db / 10)
    Z = np.zeros((ks.size, ebn0_db.size))
    for i, k in enumerate(ks):
        M = 2 ** k
        arg = np.sqrt(3 * k * gamma / (M - 1))
        pb = 4 / k * (1 - 1 / np.sqrt(M)) * 0.5 * erfc(arg / np.sqrt(2))
        Z[i] = np.log10(np.clip(pb, 1e-8, 0.5))
    X, Y = np.meshgrid(ebn0_db, ks)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.75)
    for i, k in enumerate(ks):
        ax.plot(ebn0_db, np.full_like(ebn0_db, k), Z[i],
                color=cycle(i), linewidth=1.8, label=names[i])
    ax.set_xlabel('$E_b/N_0$ (dB)'); ax.set_ylabel('bits per symbol')
    ax.set_zlabel('$\\log_{10}$(BER)')
    ax.set_yticks(ks)
    ax.set_title(title)
    ax.legend(frameon=False, loc='upper right', fontsize=7)
    ax.view_init(elev=25, azim=-130)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
