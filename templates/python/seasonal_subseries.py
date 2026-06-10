"""seasonal_subseries: 按季节切片的子序列图（揭示季节模式）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Seasonal subseries'):
    apply_theme(fig_size=(8, 4))
    rng = np.random.default_rng(17)
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    n_years = 5
    M = np.zeros((n_years, 12))
    for y in range(n_years):
        season = 5 + 3*np.sin(np.arange(12)*np.pi/6)
        M[y] = season + y*0.4 + rng.normal(0, 0.3, 12)
    fig, ax = plt.subplots()
    for m in range(12):
        xs = m + np.linspace(-0.3, 0.3, n_years)
        ax.plot(xs, M[:, m], '-o', color=cycle(0), markersize=3)
        ax.hlines(M[:, m].mean(), m-0.35, m+0.35, color=cycle(1), linewidth=1.5)
    ax.set_xticks(range(12)); ax.set_xticklabels(months)
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
