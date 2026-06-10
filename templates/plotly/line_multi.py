"""line_multi: 多条折线对比（Plotly 交互版，对应 templates/python/line_multi.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
from sci_palettes import get_palette

COLORS = get_palette('wong')


def make_figure(x=None, Y=None, labels=None, title='Multi-line') -> go.Figure:
    if x is None:
        rng = np.random.default_rng(0)
        n, n_series = 100, 4
        x = np.linspace(0, 10, n)
        Y = np.array([np.sin(x + i * np.pi / 4) + 0.05 * rng.standard_normal(n)
                      for i in range(n_series)])
        labels = [f'series {i + 1}' for i in range(n_series)]
    fig = go.Figure()
    for i, y in enumerate(Y):
        fig.add_trace(go.Scatter(
            x=x, y=y, mode='lines',
            name=labels[i] if labels else f'series {i + 1}',
            line=dict(color=COLORS[i % len(COLORS)], width=2),
        ))
    fig.update_layout(
        template='plotly_white', font=dict(size=12),
        title=title, xaxis_title='x', yaxis_title='y',
        legend=dict(borderwidth=0),
    )
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'line_multi.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
