"""qq_compare_grid: 多分布 QQ 阵（正态/t/对数正态偏态/均匀 与正态理论分位四宫格对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from theme import apply_theme
from palette import cycle

def make_figure(title='Q-Q plots vs normal'):
    apply_theme()
    rng = np.random.default_rng(5)
    n = 300
    samples = [
        ('Normal',      rng.normal(0, 1, n)),
        ("Student t (df=3)", rng.standard_t(3, n)),
        ('Log-normal (skewed)', rng.lognormal(0, 0.6, n)),
        ('Uniform',     rng.uniform(-1, 1, n)),
    ]
    p = (np.arange(1, n + 1) - 0.5) / n
    q_theo = stats.norm.ppf(p)
    fig, axes = plt.subplots(2, 2, figsize=(6.6, 6))
    for i, (ax, (name, x)) in enumerate(zip(axes.ravel(), samples)):
        z = np.sort((x - x.mean()) / x.std(ddof=1))
        ax.scatter(q_theo, z, s=10, color=cycle(i), alpha=0.6, edgecolors='none')
        lim = [min(q_theo.min(), z.min()), max(q_theo.max(), z.max())]
        ax.plot(lim, lim, '--', color='gray', linewidth=0.8)
        ax.set_title(name)
        ax.set_xlabel('theoretical quantiles'); ax.set_ylabel('sample quantiles')
        ax.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(title, y=0.995)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
