"""small_multiples: 小型多图阵列（同样布局，多个变量）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Small multiples'):
    apply_theme(fig_size=(9, 5))
    rng = np.random.default_rng(4)
    t = np.linspace(0, 10, 100)
    fig, axes = plt.subplots(2, 4, sharex=True, sharey=True)
    for i, ax in enumerate(axes.ravel()):
        y = np.sin(t + i*0.5) * np.exp(-t/(5+i)) + 0.05*rng.standard_normal(100)
        ax.plot(t, y, color=cycle(i))
        ax.set_title(f'series {i+1}', fontsize=9)
        ax.grid(True, linestyle=':', alpha=0.4)
    for ax in axes[1]: ax.set_xlabel('t')
    for ax in axes[:, 0]: ax.set_ylabel('y')
    fig.suptitle(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
