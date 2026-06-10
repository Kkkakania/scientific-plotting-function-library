"""harmonic_spectrum: 谐波频谱（1~25 次，Plotly 交互版，对应 templates/python/harmonic_spectrum.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
from sci_palettes import get_palette

COLORS = get_palette('wong')


def make_figure(title='Harmonic spectrum') -> go.Figure:
    rng = np.random.default_rng(0)
    orders = np.arange(1, 26)
    amps = np.zeros(25)
    amps[0] = 1.0
    amps[[2, 4, 6, 10]] = [0.3, 0.18, 0.08, 0.05]
    amps += rng.uniform(0, 0.02, 25)
    fig = go.Figure(go.Bar(
        x=orders, y=amps * 100, width=0.6,
        marker_color=COLORS[5], name='amplitude',
        hovertemplate='order %{x}<br>%{y:.2f}%<extra></extra>',
    ))
    fig.update_layout(
        template='plotly_white', font=dict(size=12), showlegend=False,
        title=title, xaxis_title='harmonic order',
        yaxis_title='amplitude (% of fundamental)',
        legend=dict(borderwidth=0),
    )
    fig.update_xaxes(tickvals=list(orders[::2]))
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'harmonic_spectrum.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
