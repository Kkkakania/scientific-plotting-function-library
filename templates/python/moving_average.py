"""moving_average: 原始 + 多窗口移动平均."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(t=None, y=None, windows=(5, 20, 60), title='Moving averages'):
    apply_theme(fig_size=(8, 4))
    if t is None:
        rng = np.random.default_rng(2)
        t = np.arange(500); y = np.cumsum(rng.standard_normal(500)) + 0.01*t
    fig, ax = plt.subplots()
    ax.plot(t, y, color='lightgray', linewidth=0.8, label='raw')
    for i, w in enumerate(windows):
        ma = np.convolve(y, np.ones(w)/w, mode='same')
        ax.plot(t, ma, color=cycle(i), linewidth=1.5, label=f'MA({w})')
    ax.set_xlabel('t'); ax.set_ylabel('value'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
