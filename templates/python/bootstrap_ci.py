"""bootstrap_ci: Bootstrap 抽样分布（直方图 + BCa 置信区间 + 原始统计量标注）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from theme import apply_theme
from palette import cycle

def _bca(data, boot, theta_hat, alpha=0.05):
    z0 = stats.norm.ppf((boot < theta_hat).mean())
    n = len(data)
    jack = np.array([np.delete(data, i).mean() for i in range(n)])
    d = jack.mean() - jack
    a = (d**3).sum() / (6.0 * ((d**2).sum())**1.5)
    z = stats.norm.ppf([alpha / 2, 1 - alpha / 2])
    p = stats.norm.cdf(z0 + (z0 + z) / (1 - a * (z0 + z)))
    return np.quantile(boot, p)

def make_figure(data=None, n_boot=4000, title='Bootstrap distribution of the mean'):
    apply_theme()
    rng = np.random.default_rng(2)
    if data is None:
        data = rng.gamma(2.0, 1.5, 60)          # 偏态原始样本
    theta_hat = data.mean()
    idx = rng.integers(0, len(data), (n_boot, len(data)))
    boot = data[idx].mean(axis=1)
    lo, hi = _bca(data, boot, theta_hat)
    fig, ax = plt.subplots()
    ax.hist(boot, bins=40, color=cycle(0), alpha=0.75, edgecolor='w',
            linewidth=0.3, density=True)
    ax.axvline(theta_hat, color=cycle(1), linewidth=1.5,
               label=f'sample mean = {theta_hat:.2f}')
    ax.axvline(lo, color='gray', linestyle='--', linewidth=1.1,
               label=f'BCa 95% CI [{lo:.2f}, {hi:.2f}]')
    ax.axvline(hi, color='gray', linestyle='--', linewidth=1.1)
    ax.set_xlabel('bootstrap statistic (mean)')
    ax.set_ylabel('density')
    ax.set_title(title)
    ax.legend(loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
