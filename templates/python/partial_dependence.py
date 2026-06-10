"""partial_dependence: PDP 偏依赖曲线（多特征子图）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Partial dependence'):
    apply_theme(fig_size=(8, 4))
    rng = np.random.default_rng(6)
    x = np.linspace(0, 1, 100)
    pdps = [
        np.log(x + 0.1) + 1.5 + 0.05*rng.standard_normal(100),
        2*x - x**2 + 0.05*rng.standard_normal(100),
        np.sin(3*np.pi*x) + 0.05*rng.standard_normal(100),
        np.where(x > 0.5, 1, 0) + 0.05*rng.standard_normal(100),
    ]
    fig, axes = plt.subplots(1, 4, sharey=True)
    for i, (ax, y) in enumerate(zip(axes, pdps)):
        ax.plot(x, y, color=cycle(i))
        ax.set_xlabel(f'feat_{i+1}')
        ax.grid(True, linestyle=':', alpha=0.5)
    axes[0].set_ylabel('partial dependence')
    fig.suptitle(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
