"""bump_chart: 排名随时间变化的凹凸图（6 项目 x 10 期，平滑过渡）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Ranking over time (bump chart)'):
    apply_theme(fig_size=(7, 4))
    rng = np.random.default_rng(11)
    n_item, n_per = 6, 10
    scores = np.cumsum(rng.normal(0, 1, (n_item, n_per)), axis=1)
    ranks = scores.shape[0] - np.argsort(np.argsort(scores, axis=0), axis=0)
    labels = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
    t_fine = np.linspace(0, n_per - 1, 200)
    seg = np.clip(np.floor(t_fine).astype(int), 0, n_per - 2)
    frac = t_fine - seg
    ease = 3 * frac**2 - 2 * frac**3          # smoothstep easing
    fig, ax = plt.subplots()
    for i in range(n_item):
        y = ranks[i, seg] + (ranks[i, seg + 1] - ranks[i, seg]) * ease
        ax.plot(t_fine, y, color=cycle(i), linewidth=2)
        ax.plot(np.arange(n_per), ranks[i], 'o', color=cycle(i), markersize=5)
        ax.text(n_per - 0.7, ranks[i, -1], labels[i], color=cycle(i),
                va='center', fontsize=8)
    ax.set_xlim(-0.3, n_per + 1.0)
    ax.invert_yaxis()
    ax.set_yticks(np.arange(1, n_item + 1))
    ax.set_xticks(np.arange(n_per))
    ax.set_xticklabels([f'Q{q+1}' for q in range(n_per)])
    ax.set_xlabel('period'); ax.set_ylabel('rank'); ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
