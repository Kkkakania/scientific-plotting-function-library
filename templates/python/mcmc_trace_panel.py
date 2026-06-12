"""mcmc_trace_panel: MCMC 迹图面板（4 链 trace + 后验密度，双参数两列布局）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from theme import apply_theme
from palette import cycle

def _chains(rng, target, sd, n_chain=4, n_iter=600, rho=0.85):
    out = np.zeros((n_chain, n_iter))
    starts = target + np.array([-3, -1, 1, 3]) * sd
    for c in range(n_chain):
        e = rng.normal(0, sd * np.sqrt(1 - rho**2), n_iter)
        x = starts[c]
        for t in range(n_iter):
            x = target + rho * (x - target) + e[t]
            out[c, t] = x
    return out

def make_figure(title='MCMC traces and posterior densities'):
    apply_theme()
    rng = np.random.default_rng(15)
    params = [(r'$\mu$', 2.0, 0.4), (r'$\sigma$', 1.2, 0.2)]
    fig, axes = plt.subplots(2, 2, figsize=(7, 4.8),
                             gridspec_kw={'width_ratios': [2, 1]})
    for r, (name, mu, sd) in enumerate(params):
        ch = _chains(rng, mu, sd)
        warm = 100
        for c in range(ch.shape[0]):
            axes[r, 0].plot(ch[c], color=cycle(c), linewidth=0.6, alpha=0.8)
            kde = stats.gaussian_kde(ch[c, warm:])
            grid = np.linspace(ch[:, warm:].min(), ch[:, warm:].max(), 200)
            axes[r, 1].plot(grid, kde(grid), color=cycle(c), linewidth=1.0)
        axes[r, 0].axvspan(0, warm, color='gray', alpha=0.15)
        axes[r, 0].set_ylabel(name)
        axes[r, 0].set_title(f'trace: {name}', fontsize=9)
        axes[r, 1].set_title(f'posterior: {name}', fontsize=9)
        axes[r, 1].set_ylabel('density')
        for a in axes[r]:
            a.grid(True, linestyle=':', alpha=0.5)
    axes[1, 0].set_xlabel('iteration')
    axes[1, 1].set_xlabel('value')
    fig.suptitle(title, y=0.99)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
