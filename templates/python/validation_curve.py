"""validation_curve: 超参数 vs 训练/验证误差（U 形）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Validation curve'):
    apply_theme()
    param = np.logspace(-2, 2, 20)
    train = 0.4 - 0.35/(1 + 0.5/param)
    valid = train + 0.05 + 0.2*((np.log10(param) - 0.5)**2)
    rng = np.random.default_rng(7)
    train_std = 0.02 + 0.02*rng.uniform(0, 1, 20)
    valid_std = 0.04 + 0.03*rng.uniform(0, 1, 20)
    fig, ax = plt.subplots()
    ax.fill_between(param, train-train_std, train+train_std, color=cycle(0), alpha=0.2)
    ax.fill_between(param, valid-valid_std, valid+valid_std, color=cycle(1), alpha=0.2)
    ax.semilogx(param, train, '-o', color=cycle(0), label='train')
    ax.semilogx(param, valid, '-s', color=cycle(1), label='validation')
    ax.set_xlabel('hyperparameter'); ax.set_ylabel('error')
    ax.set_title(title); ax.legend()
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
