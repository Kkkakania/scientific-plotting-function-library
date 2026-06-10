"""star_plot: 星形图（多变量观测，每个观测一个雷达）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Star plots'):
    apply_theme(fig_size=(8, 5))
    rng = np.random.default_rng(1)
    n_obs = 6; n_var = 6
    data = rng.uniform(0.3, 1, (n_obs, n_var))
    angles = np.linspace(0, 2*np.pi, n_var, endpoint=False).tolist() + [0]
    fig, axes = plt.subplots(2, 3, subplot_kw={'projection': 'polar'})
    for i, ax in enumerate(axes.ravel()):
        v = list(data[i]) + [data[i, 0]]
        ax.plot(angles, v, color=cycle(i))
        ax.fill(angles, v, color=cycle(i), alpha=0.3)
        ax.set_yticklabels([]); ax.set_xticks([])
        ax.set_title(f'obs {i+1}', fontsize=9)
    fig.suptitle(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
