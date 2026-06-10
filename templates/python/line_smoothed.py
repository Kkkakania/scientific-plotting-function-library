"""line_smoothed: 原始+滑动平均平滑."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, y=None, window=10, title='Raw vs smoothed'):
    apply_theme()
    if x is None:
        x = np.linspace(0, 10, 300)
        y = np.sin(x) + 0.3*np.random.default_rng(1).standard_normal(300)
    kernel = np.ones(window)/window
    y_s = np.convolve(y, kernel, mode='same')
    fig, ax = plt.subplots()
    ax.plot(x, y,   color='lightgray', label='raw', linewidth=0.8)
    ax.plot(x, y_s, color=cycle(0),   label=f'MA({window})')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
