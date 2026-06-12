"""bayesian_posterior_update: 先验→后验更新（Beta-Binomial 三阶段叠加演示）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from theme import apply_theme
from palette import cycle

def make_figure(a0=2, b0=2, title='Bayesian updating (Beta-Binomial)'):
    apply_theme()
    theta = np.linspace(0.001, 0.999, 500)
    # 阶段: 先验 -> 10 次试验(7 成功) -> 累计 50 次(32 成功)
    stages = [
        (a0,        b0,        'prior  Beta(2, 2)'),
        (a0 + 7,    b0 + 3,    'after 10 trials (7 successes)'),
        (a0 + 32,   b0 + 18,   'after 50 trials (32 successes)'),
    ]
    fig, ax = plt.subplots()
    for i, (a, b, name) in enumerate(stages):
        pdf = stats.beta.pdf(theta, a, b)
        ax.plot(theta, pdf, color=cycle(i), label=name)
        ax.fill_between(theta, 0, pdf, color=cycle(i), alpha=0.18)
        mode = (a - 1) / (a + b - 2)
        ax.axvline(mode, color=cycle(i), linestyle=':', linewidth=0.9, alpha=0.8)
    ax.set_xlabel(r'success probability $\theta$')
    ax.set_ylabel('density')
    ax.set_title(title)
    ax.legend(loc='upper left')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
