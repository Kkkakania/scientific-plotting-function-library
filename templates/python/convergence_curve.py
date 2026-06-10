"""convergence_curve: 优化算法收敛曲线（多算法对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Convergence comparison'):
    apply_theme()
    n = 200; it = np.arange(1, n+1)
    rng = np.random.default_rng(1)
    fig, ax = plt.subplots()
    for i, (name, tau, init) in enumerate([
        ('GD', 80, 10), ('Momentum', 50, 10),
        ('Adam', 30, 10), ('L-BFGS', 25, 10)]):
        cur = init * np.exp(-it/tau) + 0.05 + 0.1*np.exp(-it/10)*np.abs(rng.standard_normal(n))
        ax.semilogy(it, cur, color=cycle(i), label=name)
    ax.set_xlabel('iteration'); ax.set_ylabel('loss'); ax.set_title(title)
    ax.legend(); ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
