"""fan_chart: 扇形预测图（历史序列 + 分位数渐变带随预测步长逐步加宽）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from theme import apply_theme
from palette import cycle

def make_figure(title='Fan chart forecast'):
    apply_theme()
    rng = np.random.default_rng(17)
    t_hist = np.arange(0, 31)
    y_hist = 50 + 0.6*t_hist + 3*np.sin(t_hist/3) + rng.normal(0, 1.2, 31)
    h = np.arange(0, 21)
    t_fc = 30 + h
    center = y_hist[-1] + 0.55*h
    sigma = 1.5 * np.sqrt(np.maximum(h, 1e-9))
    qs = [0.05, 0.10, 0.20, 0.35]            # 与 1-q 成对的渐变带
    fig, ax = plt.subplots()
    for i, q in enumerate(qs):
        z = stats.norm.ppf(1 - q)
        ax.fill_between(t_fc, center - z*sigma, center + z*sigma,
                        color=cycle(0), alpha=0.13 + 0.07*i, linewidth=0,
                        label=f'{int((1-2*q)*100)}% band' if i in (0, len(qs)-1) else None)
    ax.plot(t_hist, y_hist, color='k', linewidth=1.2, label='observed')
    ax.plot(t_fc, center, color=cycle(1), linestyle='--', linewidth=1.3,
            label='median forecast')
    ax.axvline(30, color='gray', linestyle=':', linewidth=0.9)
    ax.text(30.4, ax.get_ylim()[0] + 1, 'forecast start', fontsize=7,
            color='gray', rotation=90, va='bottom')
    ax.set_xlabel('time'); ax.set_ylabel('value')
    ax.set_title(title)
    ax.legend(loc='upper left')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
