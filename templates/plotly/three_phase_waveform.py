"""three_phase_waveform: 三相正弦电压时域 + 相量图（Plotly 交互版，对应 templates/python/three_phase_waveform.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sci_palettes import get_palette

COLORS = get_palette('wong')


def make_figure(f=50, Um=311, title='Three-phase') -> go.Figure:
    t = np.linspace(0, 0.04, 1000)
    ua = Um * np.sin(2 * np.pi * f * t)
    ub = Um * np.sin(2 * np.pi * f * t - 2 * np.pi / 3)
    uc = Um * np.sin(2 * np.pi * f * t + 2 * np.pi / 3)
    fig = make_subplots(
        rows=1, cols=2, specs=[[{'type': 'xy'}, {'type': 'polar'}]],
        subplot_titles=('Time domain', 'Phasor'), column_widths=[0.62, 0.38],
    )
    waves = [ua, ub, uc]
    names = ['Ua', 'Ub', 'Uc']
    angles_deg = [0.0, -120.0, 120.0]
    for i, (u, lab) in enumerate(zip(waves, names)):
        c = COLORS[i % len(COLORS)]
        fig.add_trace(go.Scatter(
            x=t * 1000, y=u, mode='lines', name=lab,
            legendgroup=lab, line=dict(color=c, width=2),
        ), row=1, col=1)
        # 相量：从原点到 Um 的射线，端点用箭头形标记
        fig.add_trace(go.Scatterpolar(
            r=[0, Um], theta=[angles_deg[i], angles_deg[i]],
            mode='lines+markers', name=lab, legendgroup=lab, showlegend=False,
            line=dict(color=c, width=3),
            marker=dict(size=[0, 12], symbol='arrow', angleref='previous', color=c),
        ), row=1, col=2)
    fig.update_xaxes(title_text='t (ms)', row=1, col=1)
    fig.update_yaxes(title_text='voltage (V)', row=1, col=1, zeroline=True,
                     zerolinecolor='gray', zerolinewidth=1)
    fig.update_layout(
        template='plotly_white', font=dict(size=12),
        title=title, legend=dict(borderwidth=0),
        polar=dict(radialaxis=dict(tickvals=[100, 200, 300], range=[0, Um * 1.15])),
    )
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'three_phase_waveform.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
