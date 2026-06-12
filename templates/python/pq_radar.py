"""pq_radar: 电能质量雷达图（THD/不平衡/闪变/频偏/暂降 5 维多场景对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(series=None, names=None, title='Power quality radar'):
    apply_theme(fig_size=(6, 5))
    # each index normalized to its standard limit (1.0 = limit):
    # THD/5%, VUF/2%, Pst/1.0, |df|/0.2 Hz, sag count / planning level
    cats = ['THD', 'unbalance', 'flicker Pst', 'freq deviation', 'sag rate']
    if series is None:
        series = np.array([[0.45, 0.30, 0.40, 0.25, 0.35],   # residential feeder
                           [0.95, 0.70, 1.25, 0.40, 1.10],   # industrial feeder
                           [0.55, 0.45, 0.60, 0.35, 0.50]])  # after APF mitigation
        names = ['residential', 'industrial', 'after mitigation']
    n = len(cats)
    ang = np.linspace(0, 2*np.pi, n, endpoint=False).tolist()
    ang += [ang[0]]
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # unity polygon = compliance limit
    ax.plot(ang, [1.0]*(n + 1), color='0.4', linestyle='--', linewidth=1.2,
            label='standard limit')
    for i, vals in enumerate(series):
        v = list(vals) + [vals[0]]
        ax.plot(ang, v, color=cycle(i), label=names[i])
        ax.fill(ang, v, color=cycle(i), alpha=0.12)
    ax.set_xticks(ang[:-1]); ax.set_xticklabels(cats, fontsize=8)
    ax.set_rlim(0, 1.4); ax.set_rticks([0.5, 1.0])
    ax.set_title(title)
    ax.legend(loc='lower right', bbox_to_anchor=(1.25, -0.05), fontsize=7)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
