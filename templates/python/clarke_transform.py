"""clarke_transform: abc → αβ 静止坐标轨迹（圆形）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='αβ trajectory (Clarke)'):
    apply_theme(fig_size=(6, 5))
    t = np.linspace(0, 0.04, 500); w = 2*np.pi*50
    a = np.sin(w*t); b = np.sin(w*t - 2*np.pi/3); c = np.sin(w*t + 2*np.pi/3)
    alpha = (2/3)*(a - 0.5*b - 0.5*c)
    beta  = (2/3)*(np.sqrt(3)/2*b - np.sqrt(3)/2*c)
    fig, ax = plt.subplots()
    ax.plot(alpha, beta, color=cycle(0), linewidth=1.5)
    ax.axhline(0, color='gray', linewidth=0.5); ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlabel('α'); ax.set_ylabel('β'); ax.set_title(title)
    ax.set_aspect('equal'); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
