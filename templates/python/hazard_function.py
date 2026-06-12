"""hazard_function: 风险函数对比（Weibull 不同形状参数：递减/恒定/递增/浴盆侧）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(lam=2.0, shapes=(0.5, 1.0, 1.5, 2.5), title='Weibull hazard functions'):
    apply_theme()
    t = np.linspace(0.02, 6, 400)
    labels = {0.5: 'decreasing (early failures)', 1.0: 'constant (random)',
              1.5: 'increasing', 2.5: 'strongly increasing (wear-out)'}
    fig, ax = plt.subplots()
    for i, k in enumerate(shapes):
        h = (k / lam) * (t / lam) ** (k - 1)
        lbl = f'k = {k:g}' + (f', {labels[k]}' if k in labels else '')
        ax.plot(t, h, color=cycle(i), label=lbl)
    ax.set_ylim(0, 2.0)
    ax.set_xlabel('time'); ax.set_ylabel('hazard rate h(t)')
    ax.set_title(title)
    ax.legend(loc='upper center')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
