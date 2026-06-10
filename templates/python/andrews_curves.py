"""andrews_curves: Andrews 曲线（高维数据 Fourier 表示）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Andrews curves'):
    apply_theme(fig_size=(8, 4.5))
    rng = np.random.default_rng(0)
    n_per = 20
    X = np.vstack([rng.normal(c, 0.5, (n_per, 5)) for c in [(0,0,0,0,0),(2,1,-1,0.5,0),(-1,2,1,-0.5,0.5)]])
    labels = np.repeat(np.arange(3), n_per)
    t = np.linspace(-np.pi, np.pi, 200)
    fig, ax = plt.subplots()
    for k in range(3):
        for row in X[labels == k]:
            y = row[0]/np.sqrt(2) + row[1]*np.sin(t) + row[2]*np.cos(t) + row[3]*np.sin(2*t) + row[4]*np.cos(2*t)
            ax.plot(t, y, color=cycle(k), alpha=0.4, linewidth=0.8)
    ax.set_xlabel('t'); ax.set_ylabel('f(t)'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
