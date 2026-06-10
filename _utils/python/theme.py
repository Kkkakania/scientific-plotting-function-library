"""统一论文风格 matplotlib 主题."""
import matplotlib as mpl


def apply_theme(font_size=9, fig_size=(6, 4), dark=False):
    """统一主题；dark=True 切换深色模式（PPT/网页/dashboard 友好）.

    深色模式建议配合 sci_palettes 的 dark_bright7 / dark_muted6 /
    dark_lumen / dark_div 使用。
    """
    mpl.rcParams.update({
        'figure.figsize':   fig_size,
        'figure.dpi':       110,
        'savefig.dpi':      300,
        'savefig.bbox':     'tight',
        'font.size':        font_size,
        'font.family':      'sans-serif',
        'font.sans-serif':  ['Arial', 'Helvetica', 'DejaVu Sans'],
        'axes.linewidth':   0.8,
        'axes.labelsize':   font_size,
        'axes.titlesize':   font_size + 1,
        'axes.spines.top':   False,
        'axes.spines.right': False,
        'xtick.direction':  'out',
        'ytick.direction':  'out',
        'xtick.major.width': 0.8,
        'ytick.major.width': 0.8,
        'legend.frameon':   False,
        'legend.fontsize':  font_size - 1,
        'lines.linewidth':  1.5,
        'grid.linestyle':   ':',
        'grid.alpha':       0.5,
    })
    if dark:
        fg, bg = '#E8E6E3', '#15171C'
        mpl.rcParams.update({
            'figure.facecolor':  bg,
            'savefig.facecolor': bg,
            'axes.facecolor':    bg,
            'axes.edgecolor':    fg,
            'axes.labelcolor':   fg,
            'text.color':        fg,
            'xtick.color':       fg,
            'ytick.color':       fg,
            'grid.color':        '#4A4E58',
            'legend.labelcolor': fg,
        })


def chinese_friendly():
    mpl.rcParams['font.sans-serif'] = ['PingFang SC', 'Microsoft YaHei',
                                        'SimHei', 'Arial Unicode MS']
    mpl.rcParams['axes.unicode_minus'] = False
