"""gamut: sRGB 色域映射 + OKLCh 沿色相轴减彩度（chroma reduction）.

问题
----
OKLab/CIE Lab 是设备无关的，能表达 sRGB 表达不了的颜色。
比如 OKLCh=(0.6, 0.20, 60°) 这种饱和橙色就超出 sRGB 色域，
直接 clip 到 [0,1] 会让色相漂移甚至变成纯白/纯黑。

解法
----
保持 hue 和 L 不变，沿色相轴**只减小彩度 C**，直到颜色落入 sRGB。
二分搜索找到最大可用 C。这是 CSS Color 4 / Tailwind v4 的标准做法。

API
---
    in_gamut(rgb) -> bool                     # 是否在 sRGB 色域内
    clip_to_gamut(rgb) -> rgb                 # 简单 clip（不推荐）
    map_to_gamut_oklch(oklch) -> oklch        # 沿色相减彩度（推荐）
    map_to_gamut_lch(lch) -> lch              # CIE Lab 版本
    max_chroma(L, h, model='oklab') -> float  # 给定 L、hue 找最大 C
"""
import numpy as np
from color_lab import (oklab_to_srgb, oklch_to_oklab,
                       lab_to_srgb, lch_to_lab)


def in_gamut(rgb, tol=1e-6):
    """检测 sRGB 是否在 [0, 1] 立方体内."""
    rgb = np.asarray(rgb)
    return bool(np.all(rgb >= -tol) and np.all(rgb <= 1 + tol))


def clip_to_gamut(rgb):
    """简单 clip。会让超域颜色色相漂移，仅作 fallback."""
    return np.clip(np.asarray(rgb), 0, 1)


def max_chroma(L, hue, model='oklab', tol=1e-3):
    """给定 L 和色相 hue（度），二分搜索找最大可用彩度 C.

    model: 'oklab' 或 'cielab'
    """
    if model == 'oklab':
        to_rgb = lambda L, C, h: oklab_to_srgb(oklch_to_oklab(np.array([L, C, h])),
                                                clip=False)
    else:
        to_rgb = lambda L, C, h: lab_to_srgb(lch_to_lab(np.array([L, C, h])),
                                              clip=False)

    lo, hi = 0.0, 1.0 if model == 'oklab' else 150.0
    # 上限肯定不行，先验证 lo 在域内
    if not in_gamut(to_rgb(L, lo, hue)):
        return 0.0
    if in_gamut(to_rgb(L, hi, hue)):
        return hi
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if in_gamut(to_rgb(L, mid, hue)):
            lo = mid
        else:
            hi = mid
    return lo


def map_to_gamut_oklch(oklch, tol=1e-3):
    """OKLCh 沿色相轴减彩度直到落入 sRGB."""
    oklch = np.asarray(oklch, dtype=float).copy()
    L, C, h = oklch[..., 0], oklch[..., 1], oklch[..., 2]

    # 标量情况
    if oklch.ndim == 1:
        rgb = oklab_to_srgb(oklch_to_oklab(oklch), clip=False)
        if in_gamut(rgb):
            return np.clip(rgb, 0, 1)
        new_C = max_chroma(float(L), float(h), 'oklab', tol)
        return oklab_to_srgb(oklch_to_oklab(np.array([L, new_C, h])))

    # 批量
    out = np.zeros((*oklch.shape[:-1], 3))
    flat = oklch.reshape(-1, 3)
    out_flat = out.reshape(-1, 3)
    for i in range(len(flat)):
        rgb = oklab_to_srgb(oklch_to_oklab(flat[i]), clip=False)
        if in_gamut(rgb):
            out_flat[i] = np.clip(rgb, 0, 1)
        else:
            new_C = max_chroma(float(flat[i, 0]), float(flat[i, 2]), 'oklab', tol)
            out_flat[i] = oklab_to_srgb(oklch_to_oklab(
                np.array([flat[i, 0], new_C, flat[i, 2]])))
    return out


def map_to_gamut_lch(lch, tol=1e-2):
    """CIE LCh 沿色相轴减彩度（同思路）."""
    lch = np.asarray(lch, dtype=float)
    if lch.ndim == 1:
        rgb = lab_to_srgb(lch_to_lab(lch), clip=False)
        if in_gamut(rgb):
            return np.clip(rgb, 0, 1)
        new_C = max_chroma(float(lch[0]), float(lch[2]), 'cielab', tol)
        return lab_to_srgb(lch_to_lab(np.array([lch[0], new_C, lch[2]])))
    out = np.zeros((*lch.shape[:-1], 3))
    flat = lch.reshape(-1, 3); out_flat = out.reshape(-1, 3)
    for i in range(len(flat)):
        rgb = lab_to_srgb(lch_to_lab(flat[i]), clip=False)
        if in_gamut(rgb):
            out_flat[i] = np.clip(rgb, 0, 1)
        else:
            new_C = max_chroma(float(flat[i, 0]), float(flat[i, 2]), 'cielab', tol)
            out_flat[i] = lab_to_srgb(lch_to_lab(
                np.array([flat[i, 0], new_C, flat[i, 2]])))
    return out


if __name__ == '__main__':
    # 演示：一个超域的鲜艳橙色
    from color_lab import rgb_to_hex
    test = np.array([0.7, 0.22, 60])     # OKLCh
    print('OKLCh 输入  :', test)
    rgb_clip = clip_to_gamut(oklab_to_srgb(oklch_to_oklab(test), clip=False))
    rgb_map  = map_to_gamut_oklch(test)
    print(f'简单 clip   : {rgb_to_hex(rgb_clip)}  (色相会漂)')
    print(f'色域映射    : {rgb_to_hex(rgb_map)}   (色相保留)')

    print(f'\n最大可用彩度：')
    for L in [0.3, 0.5, 0.7, 0.9]:
        for h in [30, 120, 240]:
            cmax = max_chroma(L, h, 'oklab')
            print(f'  L={L}, h={h:3d}°: C_max = {cmax:.3f}')
