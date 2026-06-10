"""timeseries_multi: 多条时间序列对比."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_timeseries

def make_figure(t=None, Y=None, labels=None, title='Multi-series time'):
    apply_theme(fig_size=(8, 4))
    if t is None:
        t, Y = gen_timeseries(n=365, n_series=4)
        labels = [f'series {i+1}' for i in range(4)]
    fig, ax = plt.subplots()
    for i, y in enumerate(Y):
        ax.plot(t, y, color=cycle(i), linewidth=1, label=labels[i])
    ax.set_xlabel('day'); ax.set_ylabel('value'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
