"""thd_bars: 多负载下的 THD 对比."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='THD comparison'):
    apply_theme()
    loads = ['LED', 'Motor', 'PC', 'Heater', 'EV charger', 'Inverter']
    rng = np.random.default_rng(1)
    thd_v = rng.uniform(2, 8, 6); thd_i = rng.uniform(5, 35, 6)
    x = np.arange(len(loads)); w = 0.38
    fig, ax = plt.subplots()
    ax.bar(x - w/2, thd_v, w, color=cycle(0), label='V THD')
    ax.bar(x + w/2, thd_i, w, color=cycle(1), label='I THD')
    ax.axhline(8, color='red', linestyle='--', linewidth=0.8, label='V limit (8%)')
    ax.set_xticks(x); ax.set_xticklabels(loads, rotation=20)
    ax.set_ylabel('THD (%)'); ax.set_title(title)
    ax.legend(); ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
