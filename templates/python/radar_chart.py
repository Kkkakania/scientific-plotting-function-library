"""radar_chart: 雷达图（多指标对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(categories=None, series=None, names=None, title='Radar'):
    apply_theme()
    if categories is None:
        categories = ['speed', 'power', 'efficiency', 'cost', 'reliability', 'noise']
        rng = np.random.default_rng(0)
        series = rng.uniform(0.3, 1.0, (3, len(categories)))
        names = ['A', 'B', 'C']
    n = len(categories)
    angles = np.linspace(0, 2*np.pi, n, endpoint=False).tolist() + [0]
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    for i, vals in enumerate(series):
        v = list(vals) + [vals[0]]
        ax.plot(angles, v, color=cycle(i), label=names[i])
        ax.fill(angles, v, color=cycle(i), alpha=0.15)
    ax.set_xticks(angles[:-1]); ax.set_xticklabels(categories)
    ax.set_yticklabels([])
    ax.set_title(title); ax.legend(loc='lower right', bbox_to_anchor=(1.2, 0))
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
