"""choropleth_grid: 格点 choropleth（网格区域着色）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(title='Choropleth grid'):
    apply_theme(fig_size=(7, 5))
    rng = np.random.default_rng(3)
    grid = rng.uniform(0, 1, (8, 12))
    fig, ax = plt.subplots()
    im = ax.imshow(grid, cmap=sequential(hue='blue'), aspect='auto')
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            ax.text(j, i, f'R{i+1}C{j+1}' if j == 0 else '',
                    ha='center', va='center', fontsize=6, color='white' if grid[i, j] > 0.5 else 'black')
    fig.colorbar(im, ax=ax, label='rate', shrink=0.7)
    ax.set_xticks(range(12)); ax.set_yticks(range(8))
    ax.set_xticklabels([f'C{j+1}' for j in range(12)], fontsize=7)
    ax.set_yticklabels([f'R{i+1}' for i in range(8)], fontsize=7)
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
