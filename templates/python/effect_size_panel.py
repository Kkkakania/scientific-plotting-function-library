"""effect_size_panel: 效应量面板（两分布重叠可视化 + Cohen's d 标尺）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(mu1=0.0, mu2=1.2, sd=1.0, title="Effect size: Cohen's d"):
    apply_theme()
    d = (mu2 - mu1) / sd
    x = np.linspace(min(mu1, mu2) - 4*sd, max(mu1, mu2) + 4*sd, 500)
    pdf1 = np.exp(-0.5*((x - mu1)/sd)**2) / (sd*np.sqrt(2*np.pi))
    pdf2 = np.exp(-0.5*((x - mu2)/sd)**2) / (sd*np.sqrt(2*np.pi))
    overlap = np.minimum(pdf1, pdf2)
    fig, ax = plt.subplots()
    ax.plot(x, pdf1, color=cycle(0), label='group 1')
    ax.plot(x, pdf2, color=cycle(1), label='group 2')
    ax.fill_between(x, 0, overlap, color='gray', alpha=0.35, label='overlap')
    ymax = pdf1.max()
    ax.annotate('', xy=(mu2, ymax*1.06), xytext=(mu1, ymax*1.06),
                arrowprops=dict(arrowstyle='<->', color='k', lw=1.1))
    ax.text((mu1 + mu2)/2, ymax*1.10, f"d = {d:.2f}", ha='center', fontsize=9)
    for bench, lbl in [(0.2, 'small'), (0.5, 'medium'), (0.8, 'large')]:
        xb = mu1 + bench*sd
        ax.plot([xb, xb], [ymax*1.00, ymax*1.03], color='gray', linewidth=0.9)
        ax.text(xb, ymax*0.965, lbl, ha='center', fontsize=7, color='gray')
    ax.axvline(mu1, color=cycle(0), linestyle=':', linewidth=0.9)
    ax.axvline(mu2, color=cycle(1), linestyle=':', linewidth=0.9)
    ax.set_ylim(0, ymax*1.22)
    ax.set_xlabel('outcome value'); ax.set_ylabel('density')
    ax.set_title(title)
    ax.legend(loc='upper left')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
