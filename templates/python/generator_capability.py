"""generator_capability: 同步发电机 P-Q 运行极限圆图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Synchronous generator capability curve'):
    apply_theme()
    fig, ax = plt.subplots(figsize=(5.4, 5))
    S = 1.0; Xs = 1.6; E_max = 2.3; V = 1.0
    th = np.linspace(0, np.pi, 300)
    # 定子电流极限（圆心原点，半径 S）
    ax.plot(S*np.sin(th), S*np.cos(th), color=cycle(0), label='armature limit')
    # 励磁极限（圆心 (0, -V^2/Xs)）
    r_f = V*E_max/Xs; c_f = -V**2/Xs
    thf = np.linspace(0, np.pi, 300)
    Pf, Qf = r_f*np.sin(thf), c_f + r_f*np.cos(thf)
    m = Qf >= -0.05
    ax.plot(Pf[m], Qf[m], color=cycle(1), label='field limit')
    # 原动机限制 + 进相裕度
    ax.axhline(0, color='0.5', linewidth=0.8)
    ax.plot([0.95, 0.95], [-0.35, 1.05], color=cycle(2), linestyle='--', label='turbine limit')
    ax.plot([0, 0.95], [-0.35, -0.35], color=cycle(3), linestyle='-.', label='end-region heating')
    ax.fill_betweenx(np.linspace(-0.3, 0.85, 50),
                     0, np.minimum(0.93, np.sqrt(np.clip(S**2 - np.linspace(-0.3, 0.85, 50)**2, 0, None))),
                     color=cycle(0), alpha=0.08)
    ax.text(0.35, 0.25, 'safe operating\nregion', ha='center', fontsize=9)
    ax.set_xlabel('P (p.u.)'); ax.set_ylabel('Q (p.u.)'); ax.set_title(title)
    ax.legend(loc='upper right', fontsize=7); ax.grid(True, linestyle=':', alpha=0.5)
    ax.set_xlim(0, 1.45); ax.set_ylim(-0.55, 1.2)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
