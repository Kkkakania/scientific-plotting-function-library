"""line_loading_heatmap: 输电线路负载率 时间×线路 热力图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Transmission line loading (% of rating)'):
    apply_theme()
    rng = np.random.default_rng(3)
    hours = np.arange(24); n_line = 10
    base = 40 + 28*np.exp(-((hours - 11)/3.2)**2) + 22*np.exp(-((hours - 19)/2.2)**2)
    load = np.clip(base[None, :]*rng.uniform(0.55, 1.25, (n_line, 1))
                   + rng.normal(0, 4, (n_line, 24)), 5, 130)
    fig, ax = plt.subplots(figsize=(7, 4))
    im = ax.imshow(load, aspect='auto', cmap='YlOrRd', vmin=0, vmax=130)
    # 越限标记
    yy, xx = np.where(load > 100)
    ax.scatter(xx, yy, marker='x', s=28, color='k', linewidths=1.1, label='overload')
    ax.set_xticks(range(0, 24, 3)); ax.set_xticklabels(range(0, 24, 3))
    ax.set_yticks(range(n_line)); ax.set_yticklabels([f'L{i+1}' for i in range(n_line)])
    ax.set_xlabel('hour'); ax.set_ylabel('line'); ax.set_title(title)
    ax.legend(loc='upper left', fontsize=8)
    fig.colorbar(im, ax=ax, label='loading (%)', pad=0.02)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
