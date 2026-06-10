"""ga_evolution: 遗传算法适应度演化（最佳/平均/最差）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='GA fitness evolution'):
    apply_theme()
    n_gen = 100; rng = np.random.default_rng(4)
    best = 1.0 / (1 + 0.1*np.arange(n_gen))
    avg = best + 0.2 + 0.05*rng.standard_normal(n_gen)
    worst = best + 0.6 + 0.15*rng.standard_normal(n_gen)
    fig, ax = plt.subplots()
    ax.fill_between(range(n_gen), best, worst, color=cycle(0), alpha=0.15)
    ax.plot(best,  color=cycle(0), label='best')
    ax.plot(avg,   color=cycle(1), label='mean', linestyle='--')
    ax.plot(worst, color=cycle(2), label='worst', linestyle=':')
    ax.set_xlabel('generation'); ax.set_ylabel('fitness'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
