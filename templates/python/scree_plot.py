"""scree_plot: 特征值碎石图（PCA 选维度）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Scree plot'):
    apply_theme()
    rng = np.random.default_rng(5)
    eigvals = sorted(rng.exponential(2, 10) + np.linspace(8, 0.1, 10), reverse=True)
    cum = np.cumsum(eigvals) / sum(eigvals) * 100
    x = np.arange(1, len(eigvals)+1)
    fig, ax1 = plt.subplots()
    ax1.bar(x, eigvals, color=cycle(0), label='eigenvalue')
    ax1.set_xlabel('component'); ax1.set_ylabel('eigenvalue', color=cycle(0))
    ax1.tick_params(axis='y', labelcolor=cycle(0))
    ax2 = ax1.twinx()
    ax2.plot(x, cum, '-o', color=cycle(1), label='cumulative %')
    ax2.set_ylabel('cumulative variance (%)', color=cycle(1))
    ax2.tick_params(axis='y', labelcolor=cycle(1))
    ax2.spines['right'].set_visible(True)
    ax2.axhline(80, color='gray', linestyle='--', linewidth=0.7)
    ax1.set_title(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
