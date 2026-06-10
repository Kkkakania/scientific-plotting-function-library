"""histogram_basic: 直方图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_distribution

def make_figure(data=None, bins=30, title='Histogram'):
    apply_theme()
    if data is None:
        data = gen_distribution(n=600)
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, color=cycle(0), edgecolor='w', alpha=0.85)
    ax.set_xlabel('value'); ax.set_ylabel('count'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
