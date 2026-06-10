"""violin_basic: 小提琴图（密度+箱线信息合一）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(arrays=None, labels=None, title='Violin plot'):
    apply_theme()
    if arrays is None:
        rng = np.random.default_rng(6)
        arrays = [rng.normal(loc, scale, 300)
                  for loc, scale in [(0,1), (1,0.6), (1.5,1.2), (0.5,0.8)]]
        labels = list('ABCD')
    fig, ax = plt.subplots()
    vp = ax.violinplot(arrays, showmeans=True, showmedians=True)
    for i, body in enumerate(vp['bodies']):
        body.set_facecolor(cycle(i)); body.set_alpha(0.5)
    ax.set_xticks(range(1, len(labels)+1)); ax.set_xticklabels(labels)
    ax.set_ylabel('value'); ax.set_title(title)
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
