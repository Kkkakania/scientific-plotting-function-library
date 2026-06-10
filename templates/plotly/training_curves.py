"""training_curves: 神经网络训练曲线（loss + accuracy 双子图，Plotly 交互版，对应 templates/python/training_curves.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sci_palettes import get_palette

COLORS = get_palette('wong')


def make_figure(title='Training curves') -> go.Figure:
    epochs = np.arange(1, 101)
    rng = np.random.default_rng(5)
    tr_loss = 2.5 * np.exp(-epochs / 30) + 0.1 + 0.04 * rng.standard_normal(100)
    va_loss = 2.5 * np.exp(-epochs / 30) + 0.25 + 0.08 * rng.standard_normal(100)
    tr_acc = 1 - tr_loss / 3
    va_acc = 1 - va_loss / 3
    fig = make_subplots(rows=1, cols=2, subplot_titles=('Loss', 'Accuracy'),
                        horizontal_spacing=0.1)
    c_tr, c_va = COLORS[5], COLORS[6]
    fig.add_trace(go.Scatter(x=epochs, y=tr_loss, mode='lines', name='train',
                             legendgroup='train', line=dict(color=c_tr, width=2)),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=epochs, y=va_loss, mode='lines', name='validation',
                             legendgroup='val', line=dict(color=c_va, width=2)),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=epochs, y=tr_acc, mode='lines', name='train',
                             legendgroup='train', showlegend=False,
                             line=dict(color=c_tr, width=2)), row=1, col=2)
    fig.add_trace(go.Scatter(x=epochs, y=va_acc, mode='lines', name='validation',
                             legendgroup='val', showlegend=False,
                             line=dict(color=c_va, width=2)), row=1, col=2)
    fig.update_xaxes(title_text='epoch', row=1, col=1)
    fig.update_xaxes(title_text='epoch', row=1, col=2)
    fig.update_yaxes(title_text='loss', row=1, col=1)
    fig.update_yaxes(title_text='accuracy', row=1, col=2)
    fig.update_layout(
        template='plotly_white', font=dict(size=12),
        title=title, legend=dict(borderwidth=0),
    )
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'training_curves.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
