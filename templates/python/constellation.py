"""constellation: 16-QAM 星座图（受噪声扰动）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(snr_db=20, title='16-QAM constellation'):
    apply_theme(fig_size=(5.5, 5.5))
    rng = np.random.default_rng(0)
    points = np.array([(i, q) for i in [-3, -1, 1, 3] for q in [-3, -1, 1, 3]])
    n_sym = 800
    idx = rng.integers(0, 16, n_sym)
    tx = points[idx]
    snr = 10**(snr_db/10)
    noise = rng.normal(0, np.sqrt(1/snr), tx.shape) * np.sqrt(np.mean(np.sum(points**2, axis=1))/2)
    rx = tx + noise
    fig, ax = plt.subplots()
    ax.scatter(rx[:, 0], rx[:, 1], s=8, color=cycle(0), alpha=0.4)
    ax.scatter(points[:, 0], points[:, 1], s=80, color='red', marker='+', linewidth=2)
    ax.set_xlabel('I'); ax.set_ylabel('Q')
    ax.set_title(f'{title} (SNR={snr_db} dB)')
    ax.set_aspect('equal'); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
