"""population_pyramid: 人口金字塔/双向对比条形图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Population pyramid'):
    apply_theme()
    rng = np.random.default_rng(1)
    ages = [f'{i*5}-{i*5+4}' for i in range(18)] + ['90+']
    n = len(ages)
    base = 4.2*np.exp(-((np.arange(n) - 6)/7.5)**2) + 0.4
    male = base*(1 + rng.uniform(-0.08, 0.08, n))
    female = base*(1 + rng.uniform(-0.08, 0.08, n)); female[-4:] *= 1.25
    y = np.arange(n)
    fig, ax = plt.subplots(figsize=(6.4, 5))
    ax.barh(y, -male, color=cycle(0), alpha=0.85, label='male')
    ax.barh(y, female, color=cycle(1), alpha=0.85, label='female')
    ax.axvline(0, color='0.25', lw=0.8)
    ax.set_yticks(y[::2]); ax.set_yticklabels(ages[::2], fontsize=7)
    mx = max(male.max(), female.max())*1.15
    ax.set_xlim(-mx, mx)
    xticks = ax.get_xticks()
    ax.set_xticks(xticks)
    ax.set_xticklabels([f'{abs(v):.0f}' for v in xticks])
    ax.set_xlabel('population (%)'); ax.set_ylabel('age group')
    ax.set_title(title); ax.legend(); ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
