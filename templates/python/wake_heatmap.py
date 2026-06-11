"""wake_heatmap: 风电场尾流热力图（Jensen 尾流模型，8 台风机俯视风速云图）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(u0=10.0, ct=0.8, k=0.05, d=80.0,
                title='Wind farm wake map (Jensen model)'):
    """Jensen (Park) 尾流模型, 风沿 +x 吹:
    单机下游 x 处速度亏损  a = (1 - sqrt(1-Ct)) / (1 + 2k*x/D)^2,
    尾流半径线性扩张      r_w(x) = D/2 + k*x,
    多机尾流叠加取均方根  a_tot = sqrt(sum a_i^2)  (Katic 叠加),
    U(x,y) = U0 * (1 - a_tot)。Ct 推力系数, k 尾流衰减常数(陆上~0.05)。
    """
    apply_theme()
    # 8 台风机: 4 列 x 2 行交错网格 (间距 5D 顺风向, 3D 横风向)
    tx = np.array([0, 5, 10, 15, 0, 5, 10, 15]) * d
    ty = np.array([0, 0, 0, 0, 3, 3, 3, 3]) * d + np.array([0, 0.5, 0, 0.5, 0, 0.5, 0, 0.5]) * d
    x = np.linspace(-2 * d, 20 * d, 440)
    y = np.linspace(-2 * d, 6 * d, 180)
    X, Y = np.meshgrid(x, y)
    a_sq = np.zeros_like(X)
    for xt, yt in zip(tx, ty):                               # 8 台, 循环可接受
        dx, dy = X - xt, Y - yt
        rw = d / 2 + k * dx                                  # 尾流半径
        inwake = (dx > 0) & (np.abs(dy) < rw)
        a = (1 - np.sqrt(1 - ct)) / (1 + 2 * k * dx / d) ** 2
        a_sq += np.where(inwake, a ** 2, 0.0)
    U = u0 * (1 - np.sqrt(a_sq))
    fig, ax = plt.subplots(figsize=(7, 3.4))
    pm = ax.pcolormesh(X / d, Y / d, U, cmap=sequential('blue').reversed(),
                       shading='auto', vmin=0.45 * u0, vmax=u0)
    fig.colorbar(pm, ax=ax, label='wind speed (m/s)', pad=0.02)
    ax.plot(tx / d, ty / d, marker='o', linestyle='none', markersize=7,
            markerfacecolor='white', markeredgecolor='black',
            markeredgewidth=1.0, label='Turbine')
    # 风机转子线（垂直于来流）
    for xt, yt in zip(tx / d, ty / d):
        ax.plot([xt, xt], [yt - 0.5, yt + 0.5], color='black', linewidth=1.6)
    ax.annotate('wind', xy=(-0.6, 5.2), xytext=(-1.9, 5.2),
                arrowprops=dict(arrowstyle='->', lw=1.2), va='center', fontsize=9)
    ax.set_xlabel('x / D'); ax.set_ylabel('y / D'); ax.set_title(title)
    ax.set_aspect('equal')
    ax.legend(frameon=False, loc='lower right')
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
