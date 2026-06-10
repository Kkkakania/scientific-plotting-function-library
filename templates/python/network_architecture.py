"""network_architecture: 简单全连接神经网络结构图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(sizes=(4, 6, 6, 3), title='Network architecture'):
    apply_theme(fig_size=(8, 5))
    fig, ax = plt.subplots()
    x_pos = np.linspace(0, 1, len(sizes))
    coords = []
    for li, s in enumerate(sizes):
        ys = np.linspace(0.1, 0.9, s)
        coords.append([(x_pos[li], y) for y in ys])
    # 画连接
    for i in range(len(sizes) - 1):
        for a in coords[i]:
            for b in coords[i+1]:
                ax.plot([a[0], b[0]], [a[1], b[1]], color='gray', linewidth=0.3, alpha=0.5)
    # 画节点
    for li, layer in enumerate(coords):
        for x, y in layer:
            ax.add_patch(plt.Circle((x, y), 0.025, color=cycle(li), zorder=5))
    layer_names = ['input'] + [f'hidden {i+1}' for i in range(len(sizes)-2)] + ['output']
    for x, name in zip(x_pos, layer_names):
        ax.text(x, 0.02, name, ha='center', fontsize=9)
    ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.02, 1)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_title(title)
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
