"""area_signed: 正负填充区（贡献符号）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(x=None, y=None, title='Signed area'):
    apply_theme(fig_size=(8, 3.5))
    if x is None:
        x = np.linspace(0, 4*np.pi, 300)
        y = np.sin(x) * np.exp(-x/8)
    fig, ax = plt.subplots()
    ax.fill_between(x, 0, y, where=y >= 0, color=cycle(0), alpha=0.6, label='positive')
    ax.fill_between(x, 0, y, where=y <  0, color=cycle(1), alpha=0.6, label='negative')
    ax.plot(x, y, color='k', linewidth=0.8)
    ax.axhline(0, color='k', linewidth=0.5)
    ax.set_xlabel('t'); ax.set_ylabel('value'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
