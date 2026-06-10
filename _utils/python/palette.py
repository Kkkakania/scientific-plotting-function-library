"""调色板."""
from matplotlib.colors import LinearSegmentedColormap

CATEGORICAL = [
    '#0072B2', '#D55E00', '#009E73', '#CC79A7',
    '#F0E442', '#56B4E9', '#E69F00', '#999999',
]


def sequential(hue='blue', n=256):
    base = {
        'blue':   [(1, 1, 1), (0.20, 0.45, 0.75)],
        'orange': [(1, 1, 1), (0.85, 0.40, 0.10)],
        'green':  [(1, 1, 1), (0.18, 0.55, 0.34)],
        'purple': [(1, 1, 1), (0.46, 0.16, 0.51)],
    }[hue]
    return LinearSegmentedColormap.from_list(f'seq_{hue}', base, N=n)


def diverging(n=256):
    return LinearSegmentedColormap.from_list(
        'div_br',
        [(0.13, 0.40, 0.67), (1, 1, 1), (0.80, 0.10, 0.13)],
        N=n,
    )


def cycle(i):
    return CATEGORICAL[i % len(CATEGORICAL)]
