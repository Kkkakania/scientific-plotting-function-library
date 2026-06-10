"""bar_combo: 柱状 + 折线组合（双 Y 轴）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Bar + line combo'):
    apply_theme()
    months = [f'M{i+1}' for i in range(12)]
    sales = np.random.default_rng(5).uniform(30, 100, 12)
    growth = np.gradient(sales) / sales * 100
    fig, ax = plt.subplots()
    ax.bar(months, sales, color=cycle(0), alpha=0.85, label='sales')
    ax.set_ylabel('sales', color=cycle(0))
    ax.tick_params(axis='y', labelcolor=cycle(0))
    ax2 = ax.twinx()
    ax2.plot(months, growth, '-o', color=cycle(1), label='growth %')
    ax2.set_ylabel('growth (%)', color=cycle(1))
    ax2.tick_params(axis='y', labelcolor=cycle(1))
    ax2.spines['right'].set_visible(True)
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
