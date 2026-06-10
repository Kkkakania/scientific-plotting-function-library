"""bar_dumbbell: 哑铃图（两个时间点对比，每行一条段两个端点）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle
from demo_data import gen_categorical_pairs

def make_figure(labels=None, before=None, after=None, title='Dumbbell'):
    apply_theme()
    if labels is None:
        labels, before, after = gen_categorical_pairs(n=8)
    y = np.arange(len(labels))
    fig, ax = plt.subplots()
    ax.hlines(y, before, after, color='lightgray', linewidth=2)
    ax.plot(before, y, 'o', color=cycle(0), markersize=8, label='before')
    ax.plot(after,  y, 'o', color=cycle(1), markersize=8, label='after')
    ax.set_yticks(y); ax.set_yticklabels(labels)
    ax.set_xlabel('value'); ax.set_title(title)
    ax.legend(); ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
