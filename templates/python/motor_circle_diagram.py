"""motor_circle_diagram: 感应电机 Heyland 圆图（电流轨迹、功率线/转矩线、损耗分段与效率刻度）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def _stator_current(s, v=230.0, r1=0.5, x1=1.5, r2=0.6, x2=1.5, xm=40.0,
                    rc=800.0, with_rotor=False):
    """单相等效电路: Zm = jXm // Rc (含励磁与铁耗), Z2 = R2/s + jX2,
    I1 = V / (R1 + jX1 + Zm//Z2);  I2 = I1 * Zm/(Zm+Z2) (分流)。
    定 Zm 并联下 I1(s) 轨迹为圆 (Heyland 圆)。s 为转差率。
    """
    s = np.asarray(s, dtype=float)
    z2 = r2 / s + 1j * x2
    zm = 1j * xm * rc / (rc + 1j * xm)
    i1 = v / (r1 + 1j * x1 + zm * z2 / (zm + z2))
    if with_rotor:
        return i1, i1 * zm / (zm + z2)
    return i1

def make_figure(s_rated=0.04, title='Induction motor circle diagram (Heyland)'):
    apply_theme()
    v, r1 = 230.0, 0.5
    # 横轴 = 无功分量 Im(-I1), 纵轴 = 有功分量 Re(I1)（V 沿纵轴）
    to_xy = lambda i1: (-i1.imag, i1.real)
    s_arc = np.concatenate([np.logspace(-4, -1, 200), np.linspace(0.1, 1.0, 200)])
    x_arc, y_arc = to_xy(_stator_current(s_arc))
    o = _stator_current(1e-4)       # 空载点 (s→0)
    sc = _stator_current(1.0)       # 堵转点 (s=1)
    tt = _stator_current(1e6)       # s→∞ 点 (转矩线另一端)
    a = _stator_current(s_rated)    # 额定工作点
    # 三点定圆 (轨迹解析上是圆)
    zo, zs, zt = (-o.imag + 1j * o.real, -sc.imag + 1j * sc.real,
                  -tt.imag + 1j * tt.real)
    w = (zt - zo) / (zs - zo)
    zc = zo + (zs - zo) * (w - abs(w) ** 2) / (2j * w.imag)  # 外接圆圆心
    rad = abs(zo - zc)
    th = np.linspace(0, 2 * np.pi, 300)
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    ax.plot(zc.real + rad * np.cos(th), zc.imag + rad * np.sin(th),
            color='0.75', linewidth=0.8, linestyle='--')
    ax.plot(x_arc, y_arc, color=cycle(0), linewidth=1.8, label='Current locus (0<s<1)')
    xo, yo = to_xy(o); xs, ys = to_xy(sc); xt, yt = to_xy(tt); xa, ya = to_xy(a)
    ax.plot([xo, xs], [yo, ys], color=cycle(1), linewidth=1.2, label='Output line')
    ax.plot([xo, xt], [yo, yt], color=cycle(2), linewidth=1.2, label='Torque line')
    # 额定点垂线: A→输出线=输出功率, →转矩线=转子铜耗, →空载水平线=定子铜耗, →x轴=固定损耗
    kout = (ys - yo) / (xs - xo); ktq = (yt - yo) / (xt - xo)
    y_out = yo + kout * (xa - xo); y_tq = yo + ktq * (xa - xo)
    ax.plot([xa, xa], [0, ya], color='0.4', linewidth=0.9, linestyle=':')
    ax.annotate('P_out', (xa, (y_out + ya) / 2), xytext=(6, 0),
                textcoords='offset points', fontsize=7, va='center')
    for y0, y1, lab, dy in [(y_tq, y_out, 'P_cu,rotor', 16),
                            (yo, y_tq, 'P_cu,stator', 2),
                            (0, yo, 'P_fixed', -12)]:        # 小段用引线错开标注
        ax.annotate(lab, (xa, (y0 + y1) / 2), xytext=(34, dy),
                    textcoords='offset points', fontsize=7, va='center',
                    arrowprops=dict(arrowstyle='-', lw=0.5, color='0.4'))
    # 效率刻度: 沿轨迹在选定转差处标注效率值
    # eta = P_mech/P_in, P_mech = 3*|I2|^2*R2*(1-s)/s, P_in = 3*V*Re(I1)
    s_tick = np.array([0.01, 0.02, 0.05, 0.10, 0.30])
    i_tick, i2_tick = _stator_current(s_tick, with_rotor=True)
    r2 = 0.6
    eta_t = (3 * np.abs(i2_tick) ** 2 * r2 * (1 - s_tick) / s_tick) \
            / (3 * v * i_tick.real)
    xk, yk = to_xy(i_tick)
    ax.plot(xk, yk, linestyle='none', marker='_', markersize=7, color=cycle(3))
    for x_, y_, e in zip(xk, yk, eta_t):
        ax.annotate(f'η={e*100:.0f}%', (x_, y_), xytext=(-6, 4),
                    textcoords='offset points', fontsize=7, color=cycle(3),
                    ha='right')
    for x_, y_, lab, dy in [(xo, yo, 'O (no load)', -12), (xs, ys, 'S (s=1)', 6),
                            (xa, ya, f'A (s={s_rated:g})', 8)]:
        ax.plot(x_, y_, marker='o', markersize=5, color=cycle(0))
        ax.annotate(lab, (x_, y_), xytext=(4, dy), textcoords='offset points',
                    fontsize=8)
    ax.set_xlabel('reactive current (A)'); ax.set_ylabel('active current (A)')
    ax.set_title(title)
    ax.set_aspect('equal'); ax.set_xlim(-5, None); ax.set_ylim(-5, None)
    ax.legend(frameon=False, loc='upper right', fontsize=7)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
