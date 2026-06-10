"""scatter_regression: 散点 + 线性拟合 + 95% 置信带."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, y=None, title='Scatter with regression'):
    apply_theme()
    if x is None:
        rng = np.random.default_rng(5)
        x = rng.uniform(0, 10, 60); y = 1.5*x + 2 + rng.normal(0, 2, 60)
    p, cov = np.polyfit(x, y, 1, cov=True)
    xs = np.linspace(x.min(), x.max(), 100)
    ys = np.polyval(p, xs)
    se = np.sqrt(np.diag(cov))
    ci = 1.96 * np.sqrt((se[0]*xs)**2 + se[1]**2)
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=30, c=cycle(0), alpha=0.7, edgecolors='w', linewidth=0.4)
    ax.fill_between(xs, ys-ci, ys+ci, color=cycle(0), alpha=0.2, label='95% CI')
    ax.plot(xs, ys, color=cycle(0), label=f'y = {p[0]:.2f}x + {p[1]:.2f}')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
