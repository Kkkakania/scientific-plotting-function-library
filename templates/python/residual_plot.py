"""residual_plot: 回归残差图（检查模型偏差）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Residual plot'):
    apply_theme()
    rng = np.random.default_rng(10)
    x = rng.uniform(0, 10, 80); y = 1.5*x + 2 + rng.normal(0, 1.5, 80)
    p = np.polyfit(x, y, 1); resid = y - np.polyval(p, x)
    fig, ax = plt.subplots()
    ax.scatter(np.polyval(p, x), resid, s=30, c=cycle(0),
               alpha=0.7, edgecolors='w', linewidth=0.4)
    ax.axhline(0, color='k', linewidth=0.7)
    ax.set_xlabel('predicted'); ax.set_ylabel('residual'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
