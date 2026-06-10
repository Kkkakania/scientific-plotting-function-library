"""event_timeline: 多分类事件时间轴."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Event timeline'):
    apply_theme(fig_size=(8, 3.5))
    rng = np.random.default_rng(19)
    cats = ['build', 'test', 'deploy', 'rollback']
    fig, ax = plt.subplots()
    for i, c in enumerate(cats):
        times = np.sort(rng.uniform(0, 100, 6))
        ax.plot(times, [i]*len(times), 'o', color=cycle(i), markersize=10, label=c)
    ax.set_yticks(range(len(cats))); ax.set_yticklabels(cats)
    ax.set_xlabel('time'); ax.set_title(title)
    ax.legend(loc='lower right'); ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
