"""18_apply_v15_palette: 把 v1.5 新配色应用到当前图（增量调色板演示）.

依赖 12_apply_palette.py 同样的思路，但直接内嵌 v1.5 hex，
不需要先导出调色板文件。
"""
import originpro as op

V15 = {
    'dark_bright7': ['#E6CF65', '#00CFDD', '#F58A4A', '#77D3A6',
                     '#8190E6', '#FF7B80', '#E1D4D7'],
    'vivid6':       ['#005AAB', '#DE1655', '#379F3D', '#F28D1F',
                     '#00CFE5', '#A5439D'],
    'safe10':       ['#004C85', '#AC2B59', '#37804F', '#D75E43', '#00A1CC',
                     '#B98DEC', '#D8AA30', '#6AD3C0', '#FEC6A7', '#D0DFEB'],
    'mono_blue4':   ['#B5C9D7', '#00A4DE', '#0077AD', '#324550'],
}


def hex_to_origin(hex_color):
    """'#RRGGBB' → Origin 的 BGR int."""
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return (b << 16) | (g << 8) | r


def apply_palette(graph=None, name='vivid6'):
    """给当前（或指定）graph 的每条曲线按 v1.5 调色板着色."""
    gp = graph or op.find_graph()
    gl = gp[0]
    colors = V15[name]
    for i, plot in enumerate(gl.plot_list()):
        plot.color = hex_to_origin(colors[i % len(colors)])
    return gp


if __name__ == '__main__':
    apply_palette(name='vivid6')
    print('applied v1.5 palette')
