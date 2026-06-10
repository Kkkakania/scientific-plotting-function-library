"""scatter_grouped: 按类别着色的散点（Plotly 交互版，对应 templates/python/scatter_grouped.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
from sci_palettes import get_palette

COLORS = get_palette('wong')


def make_figure(x=None, y=None, groups=None, title='Grouped scatter') -> go.Figure:
    if x is None:
        rng = np.random.default_rng(0)
        n, n_groups, separation = 80, 3, 2.5
        X, Y, G = [], [], []
        for k in range(n_groups):
            X.append(rng.normal(k * separation, 1, n))
            Y.append(rng.normal(k * separation, 1, n))
            G.append(np.full(n, k))
        x, y, groups = np.concatenate(X), np.concatenate(Y), np.concatenate(G)
    fig = go.Figure()
    for g in np.unique(groups):
        m = groups == g
        fig.add_trace(go.Scatter(
            x=x[m], y=y[m], mode='markers', name=f'class {int(g)}',
            marker=dict(size=8, color=COLORS[int(g) % len(COLORS)], opacity=0.7,
                        line=dict(color='white', width=0.5)),
        ))
    fig.update_layout(
        template='plotly_white', font=dict(size=12),
        title=title, xaxis_title='feature 1', yaxis_title='feature 2',
        legend=dict(borderwidth=0),
    )
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'scatter_grouped.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
