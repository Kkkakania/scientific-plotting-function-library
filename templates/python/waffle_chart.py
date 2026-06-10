"""waffle_chart: 华夫饼图（百分比构成）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(values=None, labels=None, rows=10, cols=10, title='Waffle chart'):
    apply_theme(fig_size=(6, 4.5))
    if values is None:
        values = [35, 25, 20, 12, 8]
        labels = ['A', 'B', 'C', 'D', 'E']
    total = rows * cols
    parts = np.round(np.array(values) / sum(values) * total).astype(int)
    # 修整使总和正好等于 total
    diff = total - parts.sum()
    parts[0] += diff
    grid = np.zeros((rows, cols), dtype=int)
    flat = []
    for i, p in enumerate(parts):
        flat += [i+1] * p
    flat = flat[:total]
    grid = np.array(flat).reshape(rows, cols)
    fig, ax = plt.subplots()
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(plt.Rectangle((c, rows-1-r), 0.9, 0.9,
                                       color=cycle(int(grid[r,c])-1)))
    ax.set_xlim(0, cols); ax.set_ylim(0, rows)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    handles = [plt.Rectangle((0,0),1,1, color=cycle(i)) for i in range(len(labels))]
    ax.legend(handles, [f'{l} ({v}%)' for l, v in zip(labels, values)],
              loc='center left', bbox_to_anchor=(1.02, 0.5))
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
