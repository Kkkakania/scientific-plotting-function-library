"""stream_graph: 河流图（堆叠面积 wiggle 基线，ThemeRiver 风格）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Stream graph'):
    apply_theme(fig_size=(8, 4))
    rng = np.random.default_rng(3)
    n, n_series = 200, 5
    x = np.linspace(0, 24, n)
    Y = np.zeros((n_series, n))
    for i in range(n_series):
        for _ in range(4):                       # 每条河流 = 几个高斯鼓包之和
            c, w, a = rng.uniform(2, 22), rng.uniform(1.5, 5), rng.uniform(0.5, 2)
            Y[i] += a * np.exp(-0.5 * ((x - c) / w)**2)
    base = -Y.sum(axis=0) / 2                    # wiggle 基线（对称轮廓）
    layers = base + np.vstack([np.zeros(n), np.cumsum(Y, axis=0)])
    fig, ax = plt.subplots()
    for i in range(n_series):
        ax.fill_between(x, layers[i], layers[i + 1], color=cycle(i),
                        alpha=0.85, linewidth=0.5, edgecolor='white',
                        label=f'topic {i+1}')
    ax.set_xlabel('time (month)'); ax.set_ylabel('flow magnitude')
    ax.set_title(title)
    ax.legend(frameon=False, ncol=5, loc='upper center',
              bbox_to_anchor=(0.5, -0.15))
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
