"""smith_chart: Smith 阻抗圆图基底."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Smith chart'):
    apply_theme(fig_size=(6.5, 6.5))
    theta = np.linspace(0, 2*np.pi, 360)
    fig, ax = plt.subplots()
    ax.plot(np.cos(theta), np.sin(theta), 'k', linewidth=1)
    for r in [0.2, 0.5, 1.0, 2.0, 5.0]:
        cx, R = r/(r+1), 1/(r+1)
        ax.plot(cx + R*np.cos(theta), R*np.sin(theta), color='#888', linewidth=0.7)
        ax.text(cx + R - 0.02, 0.02, f'{r}', fontsize=7, color='#444')
    for x in [0.2, 0.5, 1.0, 2.0, 5.0, -0.2, -0.5, -1.0, -2.0, -5.0]:
        cx, cy = 1.0, 1/x; R = abs(1/x)
        pts = np.column_stack([cx + R*np.cos(theta), cy + R*np.sin(theta)])
        inside = (pts[:,0]**2 + pts[:,1]**2) <= 1.0 + 1e-9
        if inside.any():
            ax.plot(pts[inside,0], pts[inside,1], color='#bbb', linewidth=0.6)
    ax.plot([-1, 1], [0, 0], 'k', linewidth=0.8)
    ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1); ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
