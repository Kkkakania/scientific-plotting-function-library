"""timeseries_basic: 单条时间序列."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_timeseries

def make_figure(t=None, y=None, title='Time series'):
    apply_theme(fig_size=(8, 3.5))
    if t is None:
        t, y = gen_timeseries(n=365)
    fig, ax = plt.subplots()
    ax.plot(t, y, color=cycle(0), linewidth=1)
    ax.set_xlabel('day'); ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
