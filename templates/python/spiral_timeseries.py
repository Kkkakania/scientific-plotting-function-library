"""spiral_timeseries: 时间螺旋图（极坐标按年盘旋一圈，颜色编码数值）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(title='Time spiral (3 years, weekly)'):
    apply_theme(fig_size=(5.5, 5.5))
    rng = np.random.default_rng(23)
    n_years, n_w = 3, 52
    w = np.arange(n_years * n_w)
    val = 12 + 8 * np.sin((w % n_w - 6) * 2 * np.pi / n_w) \
        + 0.06 * w + rng.normal(0, 1.2, len(w))
    theta = 2 * np.pi * (w % n_w) / n_w
    r = 1.0 + w / n_w                              # 每年盘旋一圈
    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')
    ax.set_theta_zero_location('N'); ax.set_theta_direction(-1)
    sc = ax.scatter(theta, r, c=val, cmap=sequential('blue'), s=22)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax.set_xticks(np.arange(12) * 2 * np.pi / 12)
    ax.set_xticklabels(months, fontsize=8)
    ax.set_yticks([1.5, 2.5, 3.5])
    ax.set_yticklabels(['yr 1', 'yr 2', 'yr 3'], fontsize=7)
    ax.set_rlim(0, n_years + 1.3)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.set_title(title, pad=18)
    cb = fig.colorbar(sc, ax=ax, shrink=0.7, pad=0.10)
    cb.set_label('value')
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
