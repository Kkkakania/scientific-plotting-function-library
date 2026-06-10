"""residual_history: CFD 迭代残差曲线（不同变量对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Residual history'):
    apply_theme()
    n = 2000
    it = np.arange(1, n+1)
    rng = np.random.default_rng(0)
    fig, ax = plt.subplots()
    for i, (name, tau, base) in enumerate([
        ('continuity', 600, 1e0), ('u-velocity', 400, 5e-1),
        ('v-velocity', 400, 4e-1), ('k', 300, 8e-1), ('epsilon', 350, 6e-1)]):
        res = base * np.exp(-it/tau) * (1 + 0.1*rng.standard_normal(n))
        ax.semilogy(it, np.abs(res), color=cycle(i), linewidth=1, label=name)
    ax.axhline(1e-4, color='gray', linestyle='--', linewidth=0.7, label='criterion')
    ax.set_xlabel('iteration'); ax.set_ylabel('residual'); ax.set_title(title)
    ax.legend(fontsize=7); ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
