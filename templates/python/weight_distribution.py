"""weight_distribution: 各层权重分布对比（训练前后）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Weight distribution'):
    apply_theme(fig_size=(8, 4))
    rng = np.random.default_rng(8)
    layers = ['conv1', 'conv2', 'fc1', 'fc2']
    fig, axes = plt.subplots(1, 4, sharey=True)
    for i, (ax, name) in enumerate(zip(axes, layers)):
        init = rng.normal(0, 0.3, 2000)
        trained = rng.normal(0.05*i, 0.5 - 0.05*i, 2000)
        ax.hist(init,    bins=40, color='lightgray', alpha=0.6, label='init')
        ax.hist(trained, bins=40, color=cycle(i),    alpha=0.6, label='trained')
        ax.set_title(name, fontsize=10); ax.legend(fontsize=7)
        ax.grid(True, linestyle=':', alpha=0.5)
    axes[0].set_ylabel('count')
    fig.suptitle(title); fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
