"""hosting_capacity: 配电网光伏承载力箱线（按馈线类型）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='PV hosting capacity by feeder type'):
    apply_theme()
    rng = np.random.default_rng(4)
    groups = ['urban\nshort', 'urban\nlong', 'suburban', 'rural\nshort', 'rural\nlong']
    centers = [6.5, 4.8, 3.6, 2.4, 1.5]
    data = [np.clip(rng.normal(c, c*0.22, 60), 0.2, None) for c in centers]
    fig, ax = plt.subplots()
    bp = ax.boxplot(data, tick_labels=groups, patch_artist=True, widths=0.55,
                    medianprops=dict(color='k', lw=1.2))
    for i, box in enumerate(bp['boxes']):
        box.set(facecolor=cycle(i), alpha=0.55, edgecolor=cycle(i))
    for i, d in enumerate(data):
        x = rng.normal(i + 1, 0.06, d.size)
        ax.scatter(x, d, s=7, color=cycle(i), alpha=0.5, zorder=3)
    ax.set_ylabel('hosting capacity (MW)'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
