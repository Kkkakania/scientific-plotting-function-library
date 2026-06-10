"""bivariate: 二维双色调色板.

普通调色板编码一维数据；双变量调色板用一个 2D 网格颜色块同时编码两维。
经典场景：人口密度 × 收入、温度 × 降水、X 偏差 × Y 偏差等。

实现思路：选两个色相对，按 X 方向插 hue1，按 Y 方向插 hue2，
在 Lab 空间叠加再投回 sRGB。

用法::

    from bivariate import bivariate_cmap, bivariate_legend
    import matplotlib.pyplot as plt

    cmap_grid = bivariate_cmap(n=4, scheme='blue_red')   # 4×4 颜色矩阵
    # 给数据上色：x_idx ∈ [0..n-1], y_idx ∈ [0..n-1]
    colors = cmap_grid[y_idx, x_idx]
"""
import numpy as np
from color_lab import lch_to_lab, lab_to_srgb, rgb_to_hex


SCHEMES = {
    # X 偏蓝，Y 偏红 —— 经典 "+x+y → 紫"
    'blue_red':   {'hueX': 240, 'hueY': 10,  'L_low': 95, 'L_high': 30, 'C_max': 65},
    # X 偏蓝，Y 偏黄 —— 适合 (湿度 × 温度)
    'blue_yellow':{'hueX': 240, 'hueY': 90,  'L_low': 95, 'L_high': 35, 'C_max': 70},
    # X 偏青，Y 偏品红
    'cyan_magenta':{'hueX': 180,'hueY': 320, 'L_low': 95, 'L_high': 30, 'C_max': 60},
    # X 偏绿，Y 偏红
    'green_red':  {'hueX': 130, 'hueY': 10,  'L_low': 95, 'L_high': 30, 'C_max': 65},
    # 棕橙 × 灰青（地学风）
    'tan_teal':   {'hueX': 60,  'hueY': 200, 'L_low': 92, 'L_high': 32, 'C_max': 55},
}


def bivariate_cmap(n=4, scheme='blue_red', as_hex=False):
    """生成 n×n 颜色矩阵.

    返回 shape (n, n, 3) RGB（[0,1]）或 list[list[hex]]。
    grid[i, j] 对应 (y_idx=i, x_idx=j)；i=0 是 y 轴最低（亮），
    i=n-1 是 y 轴最高（暗）。
    """
    cfg = SCHEMES[scheme]
    grid = np.zeros((n, n, 3))
    for i in range(n):                       # y
        for j in range(n):                   # x
            tx = j / (n - 1)
            ty = i / (n - 1)
            # 在 Lab 空间分别加两个轴的偏移
            L = cfg['L_low'] - (cfg['L_low'] - cfg['L_high']) * np.sqrt(tx**2 + ty**2) / np.sqrt(2)
            # X 轴贡献：hueX 方向的偏移
            Cx = cfg['C_max'] * tx
            Cy = cfg['C_max'] * ty
            ax = Cx * np.cos(np.deg2rad(cfg['hueX']))
            bx = Cx * np.sin(np.deg2rad(cfg['hueX']))
            ay = Cy * np.cos(np.deg2rad(cfg['hueY']))
            by = Cy * np.sin(np.deg2rad(cfg['hueY']))
            lab = np.array([L, ax + ay, bx + by])
            grid[i, j] = lab_to_srgb(lab)
    if as_hex:
        return [[rgb_to_hex(grid[i, j]) for j in range(n)] for i in range(n)]
    return grid


def bivariate_legend(ax, grid, x_label='X', y_label='Y'):
    """在给定 axes 上画双变量调色板的 N×N 色块图例."""
    n = grid.shape[0]
    for i in range(n):
        for j in range(n):
            ax.add_patch(__import__('matplotlib.patches', fromlist=['Rectangle'])
                        .Rectangle((j, i), 1, 1, color=grid[i, j]))
    ax.set_xlim(0, n); ax.set_ylim(0, n)
    ax.set_aspect('equal')
    ax.set_xticks([0.5, n - 0.5]); ax.set_xticklabels(['low', 'high'])
    ax.set_yticks([0.5, n - 0.5]); ax.set_yticklabels(['low', 'high'])
    ax.set_xlabel(x_label); ax.set_ylabel(y_label)


if __name__ == '__main__':
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, len(SCHEMES), figsize=(2.4 * len(SCHEMES), 2.4))
    for ax, name in zip(axes, SCHEMES):
        g = bivariate_cmap(n=5, scheme=name)
        bivariate_legend(ax, g, 'X', 'Y')
        ax.set_title(name, fontsize=9, family='monospace')
    fig.suptitle('Bivariate palettes (5x5)', fontsize=11, fontweight='bold')
    fig.tight_layout()
    fig.savefig('bivariate_preview.png', dpi=200, bbox_inches='tight')
    print('bivariate_preview.png written')
