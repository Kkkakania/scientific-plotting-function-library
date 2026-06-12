"""qam_constellation_grid: QAM 星座阶梯（4/16/64/256-QAM 四宫格 + EVM 标注）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(snr_db=24, n_sym=1500, title='QAM constellations'):
    apply_theme(fig_size=(6.8, 6.6))
    rng = np.random.default_rng(0)
    fig, axes = plt.subplots(2, 2)
    for ax, M in zip(axes.ravel(), [4, 16, 64, 256]):
        m = int(np.sqrt(M))
        lv = 2 * np.arange(m) - (m - 1)
        pts = (lv[:, None] + 1j * lv[None, :]).ravel()
        pts = pts / np.sqrt(np.mean(np.abs(pts) ** 2))
        tx = pts[rng.integers(0, M, n_sym)]
        sigma = np.sqrt(10 ** (-snr_db / 10) / 2)
        rx = tx + sigma * (rng.standard_normal(n_sym) + 1j * rng.standard_normal(n_sym))
        evm = 100 * np.sqrt(np.mean(np.abs(rx - tx) ** 2) / np.mean(np.abs(pts) ** 2))
        ax.scatter(rx.real, rx.imag, s=3, color=cycle(0), alpha=0.35, linewidths=0)
        ax.scatter(pts.real, pts.imag, s=14, color=cycle(1), marker='+', linewidths=0.9)
        ax.text(0.04, 0.96, f'EVM = {evm:.1f}%', transform=ax.transAxes,
                fontsize=8, va='top')
        ax.set_title(f'{M}-QAM', fontsize=9)
        ax.set_xlabel('I'); ax.set_ylabel('Q')
        ax.set_aspect('equal'); ax.set_xlim(-1.7, 1.7); ax.set_ylim(-1.7, 1.7)
        ax.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(f'{title} (SNR = {snr_db} dB)', y=0.99)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
