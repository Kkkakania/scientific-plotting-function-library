"""feature_importance: 特征重要性排序条形图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(title='Feature importance'):
    apply_theme()
    names = [f'feat_{i+1}' for i in range(15)]
    rng = np.random.default_rng(5)
    imp = sorted(rng.exponential(1.0, 15), reverse=True)
    cmap = sequential(hue='blue')
    colors = [cmap(0.3 + 0.7*v/max(imp)) for v in imp]
    fig, ax = plt.subplots()
    ax.barh(names[::-1], imp[::-1], color=colors[::-1])
    ax.set_xlabel('importance'); ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
