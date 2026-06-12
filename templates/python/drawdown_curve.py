"""drawdown_curve: 净值曲线 + 回撤区域双面板（标注最大回撤）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Equity curve and drawdown'):
    apply_theme(fig_size=(7, 5))
    rng = np.random.default_rng(8)
    n = 750
    r = rng.normal(0.0006, 0.011, n)
    equity = np.cumprod(1 + r)
    peak = np.maximum.accumulate(equity)
    dd = equity / peak - 1
    t = np.arange(n)
    i_mdd = dd.argmin()
    fig, (ax, axd) = plt.subplots(2, 1, sharex=True,
                                  gridspec_kw={'height_ratios': [2, 1]})
    ax.plot(t, equity, color=cycle(0), label='equity (NAV)')
    ax.plot(t, peak, color=cycle(7), linewidth=1, linestyle='--',
            label='running peak')
    ax.set_ylabel('net asset value'); ax.set_title(title)
    ax.legend(frameon=False)
    ax.grid(True, linestyle=':', alpha=0.5)
    axd.fill_between(t, dd * 100, 0, color=cycle(1), alpha=0.5)
    axd.plot(t, dd * 100, color=cycle(1), linewidth=0.8)
    axd.plot(i_mdd, dd[i_mdd] * 100, 'v', color=cycle(1), markersize=6)
    axd.annotate(f'max DD {dd[i_mdd]*100:.1f}%', (i_mdd, dd[i_mdd] * 100),
                 textcoords='offset points', xytext=(8, -2), fontsize=8)
    axd.set_xlabel('trading day'); axd.set_ylabel('drawdown (%)')
    axd.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
