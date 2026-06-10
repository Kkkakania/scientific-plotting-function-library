"""scatter_marginal_rug: 散点 + 轴边缘 rug 短线."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Scatter with rug'):
    apply_theme()
    rng = np.random.default_rng(0)
    x = rng.normal(0, 1, 120); y = 0.7*x + rng.normal(0, 0.6, 120)
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=25, color=cycle(0), alpha=0.7, edgecolors='w', linewidth=0.4)
    for xi in x: ax.plot([xi, xi], [ax.get_ylim()[0], ax.get_ylim()[0]+0.05*(ax.get_ylim()[1]-ax.get_ylim()[0])], color=cycle(0), linewidth=0.6, transform=ax.get_xaxis_transform(), clip_on=False)
    for yi in y: ax.plot([0, 0.012], [yi, yi], color=cycle(0), linewidth=0.6, transform=ax.get_yaxis_transform(), clip_on=False)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
