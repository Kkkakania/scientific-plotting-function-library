"""joint_marginal: 主散点 + 边缘直方图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, y=None, title='Joint + marginals'):
    apply_theme(fig_size=(6, 6))
    if x is None:
        rng = np.random.default_rng(3)
        x = rng.normal(0, 1, 600); y = 0.6*x + rng.normal(0, 0.7, 600)
    fig = plt.figure()
    gs = fig.add_gridspec(4, 4, hspace=0.05, wspace=0.05)
    ax_main = fig.add_subplot(gs[1:, :-1])
    ax_top  = fig.add_subplot(gs[0, :-1], sharex=ax_main)
    ax_right= fig.add_subplot(gs[1:, -1], sharey=ax_main)
    ax_main.scatter(x, y, s=10, color=cycle(0), alpha=0.6, edgecolors='none')
    ax_top.hist(x,   bins=30, color=cycle(0), edgecolor='w')
    ax_right.hist(y, bins=30, color=cycle(0), edgecolor='w', orientation='horizontal')
    ax_top.tick_params(labelbottom=False)
    ax_right.tick_params(labelleft=False)
    ax_main.set_xlabel('x'); ax_main.set_ylabel('y')
    fig.suptitle(title)
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
