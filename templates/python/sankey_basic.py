"""sankey_basic: 桑基流图（两阶段流量）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
from theme import apply_theme

def make_figure(flows=None, labels=None, title='Sankey'):
    apply_theme(fig_size=(7, 5))
    if flows is None:
        flows  = [1.0,  0.4, -0.3, -0.5, -0.2, -0.4]
        labels = ['in', 'recycle', 'out 1', 'out 2', 'out 3', 'out 4']
    fig, ax = plt.subplots()
    ax.set_axis_off()
    s = Sankey(ax=ax, flows=flows, labels=labels,
               orientations=[0, 1, 0, -1, 1, 0],
               unit='', scale=0.5)
    s.finish()
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
