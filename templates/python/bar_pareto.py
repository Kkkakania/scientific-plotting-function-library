"""bar_pareto: 帕累托图（降序柱状 + 累计百分比折线）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Pareto chart'):
    apply_theme()
    labels = [f'cause {i+1}' for i in range(8)]
    counts = np.sort(np.random.default_rng(4).uniform(5, 60, 8))[::-1]
    cum = np.cumsum(counts) / counts.sum() * 100
    fig, ax = plt.subplots()
    ax.bar(labels, counts, color=cycle(0))
    ax.set_ylabel('count'); ax.set_title(title)
    ax2 = ax.twinx()
    ax2.plot(labels, cum, '-o', color=cycle(1))
    ax2.axhline(80, color='gray', linestyle='--', linewidth=0.7)
    ax2.set_ylabel('cumulative (%)', color=cycle(1))
    ax2.set_ylim(0, 105); ax2.spines['right'].set_visible(True)
    ax2.tick_params(axis='y', labelcolor=cycle(1))
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
