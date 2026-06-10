"""bode_diagram: 幅频+相频两子图（Plotly 交互版，对应 templates/python/bode_diagram.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sci_palettes import get_palette

COLORS = get_palette('wong')


def make_figure(zetas=(0.1, 0.3, 0.707, 1.5), fn=100, title='Bode diagram') -> go.Figure:
    wn = 2 * np.pi * fn
    w = np.logspace(0, 4, 500) * 2 * np.pi
    f_hz = w / (2 * np.pi)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.06)
    for i, z in enumerate(zetas):
        s = 1j * w
        H = wn ** 2 / (s ** 2 + 2 * z * wn * s + wn ** 2)
        c = COLORS[i % len(COLORS)]
        fig.add_trace(go.Scatter(
            x=f_hz, y=20 * np.log10(np.abs(H)), mode='lines',
            name=f'ζ={z}', legendgroup=f'z{i}', line=dict(color=c, width=2),
        ), row=1, col=1)
        fig.add_trace(go.Scatter(
            x=f_hz, y=np.unwrap(np.angle(H)) * 180 / np.pi, mode='lines',
            name=f'ζ={z}', legendgroup=f'z{i}', showlegend=False,
            line=dict(color=c, width=2),
        ), row=2, col=1)
    fig.add_hline(y=-3, line=dict(color='gray', dash='dash', width=1), row=1, col=1)
    fig.update_xaxes(type='log', row=1, col=1)
    fig.update_xaxes(type='log', title_text='frequency (Hz)', row=2, col=1)
    fig.update_yaxes(title_text='magnitude (dB)', row=1, col=1)
    fig.update_yaxes(title_text='phase (deg)',
                     tickvals=[0, -45, -90, -135, -180], row=2, col=1)
    fig.update_layout(
        template='plotly_white', font=dict(size=12),
        title=title, legend=dict(borderwidth=0),
    )
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'bode_diagram.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
