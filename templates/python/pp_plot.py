"""pp_plot: P-P 概率图（经验累积概率 vs 拟合正态理论累积概率）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from theme import apply_theme
from palette import cycle

def make_figure(title='P-P plot vs fitted normal'):
    apply_theme()
    rng = np.random.default_rng(9)
    n = 250
    samples = [
        ('normal sample', rng.normal(5, 2, n)),
        ('right-skewed sample', rng.gamma(2.0, 2.0, n)),
    ]
    fig, ax = plt.subplots(figsize=(5, 4.6))
    ax.plot([0, 1], [0, 1], '--', color='gray', linewidth=0.8, label='reference')
    p_emp = (np.arange(1, n + 1) - 0.5) / n
    for i, (name, x) in enumerate(samples):
        xs = np.sort(x)
        p_theo = stats.norm.cdf(xs, loc=x.mean(), scale=x.std(ddof=1))
        ax.scatter(p_theo, p_emp, s=12, color=cycle(i), alpha=0.6,
                   edgecolors='none', label=name)
    ax.set_xlim(-0.02, 1.02); ax.set_ylim(-0.02, 1.02)
    ax.set_xlabel('theoretical cumulative probability')
    ax.set_ylabel('empirical cumulative probability')
    ax.set_title(title)
    ax.legend(loc='upper left')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
