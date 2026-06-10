"""energy_mix_area: 能源结构演化（堆叠面积，2000→2030）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Generation mix evolution'):
    apply_theme()
    yr = np.arange(2000, 2031)
    x = (yr - 2000)/30
    coal = 78 - 38*x**1.3
    hydro = 16 + 2*np.sin(x*3) + 1*x
    nuclear = 1.5 + 3.5*x
    wind = 0.3 + 12*x**1.8
    solar = 0.05 + 14*x**2.4
    total = coal + hydro + nuclear + wind + solar
    shares = np.vstack([coal, hydro, nuclear, wind, solar])/total*100
    labels = ['coal', 'hydro', 'nuclear', 'wind', 'solar']
    fig, ax = plt.subplots()
    ax.stackplot(yr, shares, labels=labels,
                 colors=[cycle(i) for i in range(5)], alpha=0.85)
    ax.set_xlabel('year'); ax.set_ylabel('share of generation (%)')
    ax.set_title(title); ax.set_xlim(2000, 2030); ax.set_ylim(0, 100)
    ax.legend(loc='center left', fontsize=8)
    ax.grid(True, linestyle=':', alpha=0.4)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
