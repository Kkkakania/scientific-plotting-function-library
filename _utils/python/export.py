"""一次性导出 PNG/SVG/PDF."""
from pathlib import Path


def save_figure(fig, basename, out_dir='.', formats=('png',)):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    paths = []
    for fmt in formats:
        p = out / f'{basename}.{fmt}'
        fig.savefig(p, format=fmt)
        paths.append(p)
    return paths
