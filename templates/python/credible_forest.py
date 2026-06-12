"""credible_forest: 贝叶斯可信区间森林图（多参数后验中位数 + 94% HDI）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def _hdi(x, cred=0.94):
    xs = np.sort(x)
    n = len(xs)
    m = int(np.ceil(cred * n))
    widths = xs[m - 1:] - xs[:n - m + 1]
    i = np.argmin(widths)
    return xs[i], xs[i + m - 1]

def make_figure(title='Posterior medians with 94% HDI'):
    apply_theme()
    rng = np.random.default_rng(8)
    params = [('intercept', 1.8, 0.30), ('slope_x1', 0.65, 0.18),
              ('slope_x2', -0.42, 0.15), ('slope_x3', 0.08, 0.20),
              ('interaction', -0.95, 0.35), ('group_sd', 0.55, 0.12),
              ('noise_sd', 1.10, 0.10)]
    fig, ax = plt.subplots(figsize=(6, 4.4))
    ypos = np.arange(len(params))[::-1]
    for y, (name, mu, sd) in zip(ypos, params):
        draws = rng.normal(mu, sd, 4000) + 0.1 * sd * rng.standard_t(5, 4000)
        lo, hi = _hdi(draws)
        med = np.median(draws)
        ax.plot([lo, hi], [y, y], color=cycle(0), linewidth=2.2,
                solid_capstyle='round')
        ax.plot(med, y, 'o', color=cycle(1), markersize=6, zorder=3)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.9)
    ax.set_yticks(ypos)
    ax.set_yticklabels([p[0] for p in params])
    ax.set_xlabel('parameter value'); ax.set_ylabel('parameter')
    ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
