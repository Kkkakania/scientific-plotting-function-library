"""13_export_pub: 论文级导出（矢量 + 高分辨率）.

期刊规范常见：
- PDF 矢量（首选）
- EMF 矢量（Word 兼容）
- TIFF 300 dpi（部分期刊要求）
"""
import originpro as op
from pathlib import Path

OUT = Path.cwd() / 'origin_exports'
OUT.mkdir(exist_ok=True)


def export_publication(graph_name, basename):
    gp = op.find_graph(graph_name)
    if gp is None:
        raise RuntimeError(f'graph not found: {graph_name}')

    # 单栏宽度 8.9 cm；双栏 18.3 cm；按需调整
    gp.set_int('width',  890)     # 0.01 mm 为单位
    gp.set_int('height', 670)

    for fmt, ext in [('PDF', 'pdf'), ('EMF', 'emf'),
                     ('TIFF', 'tif'), ('PNG', 'png')]:
        p = OUT / f'{basename}.{ext}'
        gp.save_fig(str(p), type=fmt, dpi=300)
        print(f'  → {p}')


if __name__ == '__main__':
    # 假设当前 Project 里有名为 'LinePlot' 的图
    export_publication('LinePlot', 'lineplot_pub')
