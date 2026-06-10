"""svpwm_hexagon: 空间矢量 PWM 六边形 + 旋转参考矢量."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='SVPWM hexagon'):
    apply_theme(fig_size=(6, 6))
    angles = np.linspace(0, 2*np.pi, 7)
    vx = np.cos(angles); vy = np.sin(angles)
    fig, ax = plt.subplots()
    ax.plot(vx, vy, color=cycle(0), linewidth=1.5)
    ax.scatter(vx[:-1], vy[:-1], s=60, color=cycle(0), zorder=5)
    for i in range(6):
        ax.text(vx[i]*1.12, vy[i]*1.12, f'V{i+1}', ha='center', va='center')
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(0.85*np.cos(theta), 0.85*np.sin(theta), '--', color='gray', linewidth=0.8)
    ref_ang = np.pi/6
    ax.annotate('', xy=(0.85*np.cos(ref_ang), 0.85*np.sin(ref_ang)), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=cycle(1), lw=2))
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_aspect('equal')
    ax.axhline(0, color='gray', linewidth=0.4); ax.axvline(0, color='gray', linewidth=0.4)
    ax.set_xlabel('α'); ax.set_ylabel('β'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
