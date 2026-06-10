"""transformer_efficiency: 变压器效率-负载率曲线族（不同功率因数）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(P_fe=0.01, P_cu=0.02, title='Transformer efficiency vs loading'):
    apply_theme()
    k = np.linspace(0.02, 1.4, 400)
    fig, ax = plt.subplots()
    for i, pf in enumerate([1.0, 0.9, 0.8]):
        eta = k*pf/(k*pf + P_fe + k**2*P_cu)*100
        ax.plot(k*100, eta, color=cycle(i), label=f'PF = {pf}')
        kmax = np.sqrt(P_fe/P_cu)
        ax.plot(kmax*100, kmax*pf/(kmax*pf + 2*P_fe)*100, 'o', color=cycle(i), ms=4)
    ax.annotate(r'$\eta_{max}$ at $k=\sqrt{P_{fe}/P_{cu}}$', xy=(71, 97.2),
                xytext=(85, 95.2), fontsize=8, arrowprops=dict(arrowstyle='->', lw=0.8))
    ax.set_xlabel('loading (%)'); ax.set_ylabel('efficiency (%)'); ax.set_title(title)
    ax.set_ylim(88, 100); ax.legend(loc='lower right')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
