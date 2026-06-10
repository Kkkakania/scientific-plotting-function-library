"""bar_basic: 单系列柱状."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_groups

def make_figure(labels=None, values=None, title='Bar plot'):
    apply_theme()
    if labels is None:
        labels, V = gen_groups(n_cat=6, n_series=1); values = V[0]
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=cycle(0))
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
