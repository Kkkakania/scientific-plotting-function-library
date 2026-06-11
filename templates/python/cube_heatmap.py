"""cube_heatmap: 魔方热图（M*M*M 体素按值着色，留缝呈魔方状）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from theme import apply_theme
from palette import sequential

# 单位立方体 6 个面的顶点索引（8 顶点编码为 (x,y,z) 的 0/1 组合）
_CORNERS = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                     [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]], dtype=float)
_FACES = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4],
                   [2, 3, 7, 6], [1, 2, 6, 5], [0, 3, 7, 4]])


def make_figure(data=None, size=0.82, title='Cube heatmap'):
    apply_theme()
    if data is None:
        rng = np.random.default_rng(3)
        m = 4
        i, j, k = np.meshgrid(np.arange(m), np.arange(m), np.arange(m),
                              indexing='ij')
        data = np.sin(0.9 * i) + np.cos(0.7 * j) + 0.5 * k
        data += rng.normal(0, 0.15, data.shape)
    data = np.asarray(data, dtype=float)
    m = data.shape[0]
    cmap = sequential('blue')
    norm = plt.Normalize(data.min(), data.max())

    # 所有体素的原点坐标 (n,3) 与对应值 (n,)
    grid = np.stack(np.meshgrid(np.arange(m), np.arange(m), np.arange(m),
                                indexing='ij'), axis=-1).reshape(-1, 3)
    vals = data.reshape(-1)
    # 顶点：每个体素 8 个角点，整体一次性广播组装 (n,8,3)
    verts = grid[:, None, :] + size * _CORNERS[None, :, :]
    # 面：每个体素 6 面 → (n*6, 4, 3)
    polys = verts[:, _FACES, :].reshape(-1, 4, 3)
    face_colors = np.repeat(cmap(norm(vals)), 6, axis=0)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    pc = Poly3DCollection(polys, facecolors=face_colors,
                          edgecolors='white', linewidths=0.3)
    ax.add_collection3d(pc)
    lim = (-0.2, m - 1 + size + 0.2)
    ax.set_xlim(lim); ax.set_ylim(lim); ax.set_zlim(lim)
    ticks = np.arange(m) + size / 2
    ax.set_xticks(ticks); ax.set_yticks(ticks); ax.set_zticks(ticks)
    ax.set_xticklabels(np.arange(m)); ax.set_yticklabels(np.arange(m))
    ax.set_zticklabels(np.arange(m))
    ax.set_xlabel('i'); ax.set_ylabel('j'); ax.set_zlabel('k')
    ax.set_title(title)
    ax.set_box_aspect((1, 1, 1))
    mappable = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    fig.colorbar(mappable, ax=ax, shrink=0.6, pad=0.1, label='value')
    return fig


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
