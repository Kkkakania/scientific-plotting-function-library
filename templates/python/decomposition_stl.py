"""decomposition_stl: 时序分解四联图（原始/趋势/季节/残差，居中移动平均法）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Time-series decomposition'):
    apply_theme(fig_size=(7, 6.5))
    rng = np.random.default_rng(9)
    n_years, period = 8, 12
    n = n_years * period
    t = np.arange(n)
    y = 20 + 0.08 * t + 2 * np.sin(2 * np.pi * t / 96) \
        + 4 * np.sin(2 * np.pi * t / period) \
        + 1.5 * np.cos(4 * np.pi * t / period) \
        + rng.normal(0, 0.8, n)
    # 2x12 居中移动平均求趋势
    w = np.ones(period) / period
    ma = np.convolve(y, w, mode='valid')
    trend = np.full(n, np.nan)
    trend[period // 2: period // 2 + len(ma) - 1] = (ma[:-1] + ma[1:]) / 2
    detr = y - trend
    seas_m = np.array([np.nanmean(detr[m::period]) for m in range(period)])
    seas_m -= seas_m.mean()
    seasonal = np.tile(seas_m, n_years)
    resid = y - trend - seasonal
    parts = [(y, 'observed'), (trend, 'trend'),
             (seasonal, 'seasonal'), (resid, 'residual')]
    fig, axes = plt.subplots(4, 1, sharex=True)
    for ax, (v, name), i in zip(axes, parts, range(4)):
        if name == 'residual':
            ax.plot(t, v, '.', color=cycle(3), markersize=3)
            ax.axhline(0, color='#666666', linewidth=0.8)
        else:
            ax.plot(t, v, color=cycle(i), linewidth=1.2)
        ax.set_ylabel(name)
        ax.grid(True, linestyle=':', alpha=0.5)
    axes[0].set_title(title)
    axes[-1].set_xlabel('time (month index)')
    fig.tight_layout(h_pad=0.4)
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
