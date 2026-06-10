"""learning_curve: 训练样本数 vs 训练/验证误差."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Learning curve'):
    apply_theme()
    n = np.logspace(1, 3.5, 12).astype(int)
    rng = np.random.default_rng(0)
    train = 0.05 + 0.3/np.sqrt(n) + 0.01*rng.standard_normal(len(n))
    valid = 0.18 + 0.5/np.sqrt(n) + 0.02*rng.standard_normal(len(n))
    fig, ax = plt.subplots()
    ax.semilogx(n, train, '-o', color=cycle(0), label='train')
    ax.semilogx(n, valid, '-s', color=cycle(1), label='validation')
    ax.fill_between(n, train-0.02, train+0.02, color=cycle(0), alpha=0.15)
    ax.fill_between(n, valid-0.03, valid+0.03, color=cycle(1), alpha=0.15)
    ax.set_xlabel('training set size'); ax.set_ylabel('error')
    ax.set_title(title); ax.legend()
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
