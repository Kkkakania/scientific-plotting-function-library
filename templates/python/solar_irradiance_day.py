"""solar_irradiance_day: 典型日辐照度曲线（晴/多云/阴雨）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Daily solar irradiance profiles'):
    apply_theme()
    rng = np.random.default_rng(2)
    t = np.linspace(0, 24, 600)
    clear = 950*np.exp(-0.5*((t - 12.5)/3.1)**2)*(np.abs(t - 12.5) < 7.5)
    cloud_mod = 1 - 0.55*np.clip(np.sin(t*2.1) + 0.4*np.sin(t*5.3 + 1), 0, None)
    cloudy = clear*np.clip(cloud_mod + rng.normal(0, 0.05, t.size), 0.1, 1)
    rainy = 0.25*clear*np.clip(1 + rng.normal(0, 0.15, t.size), 0.3, 1.4)
    fig, ax = plt.subplots()
    for i, (y, lab) in enumerate([(clear, 'clear'), (cloudy, 'cloudy'), (rainy, 'rainy')]):
        ax.plot(t, y, color=cycle(i), label=lab)
        ax.fill_between(t, 0, y, color=cycle(i), alpha=0.12)
    ax.set_xlabel('hour of day'); ax.set_ylabel(r'irradiance (W/m$^2$)')
    ax.set_title(title); ax.set_xlim(4, 21); ax.legend()
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
