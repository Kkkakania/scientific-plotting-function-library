"""likert_diverging: Likert 量表发散柱状（同意/反对中心对齐）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Likert diverging bars'):
    apply_theme(fig_size=(8, 4))
    questions = [f'Q{i+1}' for i in range(6)]
    # strongly disagree, disagree, neutral, agree, strongly agree (%)
    rng = np.random.default_rng(2)
    M = rng.uniform(5, 25, (6, 5))
    M = M / M.sum(axis=1, keepdims=True) * 100
    colors = [cycle(1), cycle(7), '#bdbdbd', cycle(5), cycle(0)]
    fig, ax = plt.subplots()
    left = -(M[:, 0] + M[:, 1] + M[:, 2]/2)
    for k, c in enumerate(colors):
        ax.barh(questions, M[:, k], left=left, color=c, edgecolor='w', label=f'cat {k+1}')
        left += M[:, k]
    ax.axvline(0, color='k', linewidth=0.7)
    ax.set_xlabel('% of respondents'); ax.set_title(title)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=5, fontsize=7)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
