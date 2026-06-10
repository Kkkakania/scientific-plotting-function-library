"""box_basic: 箱线图（Plotly 交互版，对应 templates/python/box_basic.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
from sci_palettes import get_palette

COLORS = get_palette('wong')


def make_figure(arrays=None, labels=None, title='Box plot') -> go.Figure:
    if arrays is None:
        rng = np.random.default_rng(3)
        arrays = [rng.normal(loc, 1, 100) for loc in [0, 1, 2, 1.5, 0.5]]
        labels = list('ABCDE')
    fig = go.Figure()
    for i, (arr, lab) in enumerate(zip(arrays, labels)):
        c = COLORS[i % len(COLORS)]
        fig.add_trace(go.Box(
            y=arr, name=lab, marker_color=c, fillcolor=c,
            opacity=0.6, line=dict(color=c), boxpoints='outliers',
        ))
    fig.update_layout(
        template='plotly_white', font=dict(size=12), showlegend=False,
        title=title, xaxis_title='group', yaxis_title='value',
        legend=dict(borderwidth=0),
    )
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'box_basic.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
