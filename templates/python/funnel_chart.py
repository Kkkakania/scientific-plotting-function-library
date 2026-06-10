"""funnel_chart: 漏斗图（流程转化率）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(title='Funnel chart'):
    apply_theme(fig_size=(6.5, 5))
    stages = ['visit', 'sign-up', 'add to cart', 'checkout', 'paid']
    values = [10000, 4800, 2100, 1200, 850]
    cmap = sequential(hue='blue')
    fig, ax = plt.subplots()
    max_v = max(values)
    for i, (s, v) in enumerate(zip(stages, values)):
        w = v / max_v
        y = len(stages) - i - 1
        ax.barh(y, w,  height=0.8, color=cmap(0.3 + 0.6*v/max_v))
        ax.barh(y, -w, height=0.8, color=cmap(0.3 + 0.6*v/max_v))
        ax.text(0, y, f'{s}: {v}', ha='center', va='center', color='white', fontweight='bold')
    ax.set_yticks([]); ax.set_xticks([])
    ax.set_xlim(-1.1, 1.1); ax.set_title(title)
    ax.spines[['top', 'right', 'bottom', 'left']].set_visible(False)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
