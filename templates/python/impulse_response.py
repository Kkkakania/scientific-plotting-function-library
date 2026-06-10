"""impulse_response: 二阶系统冲激响应."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(zetas=(0.1, 0.3, 0.707, 1.5), wn=2*np.pi, title='Impulse response'):
    apply_theme()
    t = np.linspace(0, 5, 500)
    fig, ax = plt.subplots()
    for i, z in enumerate(zetas):
        if z < 1:
            wd = wn*np.sqrt(1 - z**2)
            h = (wn/np.sqrt(1-z**2))*np.exp(-z*wn*t)*np.sin(wd*t)
        elif z == 1:
            h = wn**2 * t * np.exp(-wn*t)
        else:
            wd = wn*np.sqrt(z**2 - 1)
            h = (wn/np.sqrt(z**2-1))*np.exp(-z*wn*t)*np.sinh(wd*t)
        ax.plot(t, h, color=cycle(i), label=f'ζ = {z}')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.set_xlabel('t'); ax.set_ylabel('h(t)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
