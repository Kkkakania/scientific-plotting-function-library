"""12_apply_palette: 把我们的 sci_palettes 套到 Origin 折线/热力图.

Origin 允许程序化设置每条曲线的颜色，所以可以让任何配色
（包括我们 27 套）在 Origin 里复用。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', '..', 'palettes', 'python'))
import originpro as op
import numpy as np
from sci_palettes import get_palette


def apply_categorical_palette(gp_layer, palette_name='wong'):
    """把分类配色的 HEX 列表应用到当前 layer 的每条曲线."""
    colors = get_palette(palette_name)
    plots = gp_layer.plot_list()
    for plt, hex_c in zip(plots, colors):
        plt.color = hex_c


# 示例：8 条折线用 wong 配色
rng = np.random.default_rng(0)
wb = op.new_book(lname='PaletteDemo')
wks = wb[0]
x = np.linspace(0, 10, 100); wks.from_list(0, x.tolist(), axis='X')
for k in range(8):
    y = np.sin(x + k*np.pi/4) + 0.1*rng.standard_normal(100) + k*0.3
    wks.from_list(k+1, y.tolist(), axis='Y', lname=f'wong{k+1}')

gp = op.new_graph(template='line', lname='WongDemo')
gl = gp[0]
for k in range(8):
    gl.add_plot(wks, f'0,{k+1}', 'l')

apply_categorical_palette(gl, 'wong')
gl.rescale()
gl.add_legend()
print('palette "wong" applied to 8 lines')
