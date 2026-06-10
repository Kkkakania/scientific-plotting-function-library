"""dist_mixture: 高斯混合 PDF + 直方图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Gaussian mixture'):
    apply_theme()
    rng = np.random.default_rng(6)
    n = 1500
    comps = [(0.3, -2, 0.7), (0.4, 0.5, 1.0), (0.3, 3, 0.6)]
    samples = []
    for w, mu, sd in comps:
        samples.append(rng.normal(mu, sd, int(n*w)))
    data = np.concatenate(samples)
    x = np.linspace(-5, 6, 500)
    pdf = sum(w / (sd*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2*sd**2)) for w, mu, sd in comps)
    fig, ax = plt.subplots()
    ax.hist(data, bins=60, density=True, color='lightgray', edgecolor='w', alpha=0.8)
    for i, (w, mu, sd) in enumerate(comps):
        comp = w / (sd*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2*sd**2))
        ax.plot(x, comp, '--', color=cycle(i), label=f'comp {i+1}')
    ax.plot(x, pdf, color='k', linewidth=1.5, label='mixture')
    ax.set_xlabel('x'); ax.set_ylabel('PDF'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
