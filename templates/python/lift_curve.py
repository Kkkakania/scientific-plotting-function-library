"""lift_curve: 增益/提升曲线（营销响应分析）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Lift / Gain curve'):
    apply_theme()
    rng = np.random.default_rng(13)
    n = 1000
    scores = rng.uniform(0, 1, n)
    y = (rng.uniform(0, 1, n) < scores*0.8).astype(int)
    order = np.argsort(-scores); y = y[order]
    pct = np.arange(1, n+1) / n * 100
    gain = np.cumsum(y) / y.sum() * 100
    fig, ax = plt.subplots()
    ax.plot(pct, gain, color=cycle(0), label='model')
    ax.plot([0, 100], [0, 100], '--', color='gray', linewidth=0.8, label='random')
    ax.set_xlabel('population (%)'); ax.set_ylabel('cumulative gain (%)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
