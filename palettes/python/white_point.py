"""white_point: 色彩白点适应（chromatic adaptation transform, CAT）.

为什么要这个
-----------
屏幕用 D65 白点（6504K），但很多印刷标准（特别是 ICC 配置文件）用 D50（5003K）。
直接把屏幕颜色丢去印刷会偏色。Bradford 变换是 ICC 推荐的标准 CAT。

四个内置标准白点 XYZ（CIE 公开规范）：
- D50: 印刷 / ICC PCS（5003K 偏暖）
- D55: 平均日光（5503K）
- D65: 屏幕 sRGB（6504K，默认）
- D75: 北方天空（7504K 偏冷）

API
---
    adapt_xyz(xyz, src='D65', dst='D50', method='bradford')
    adapt_rgb_for_print(rgb)         # 屏幕 → 印刷快捷方式
    color_temperature(xyz)           # 估算色温（K）
"""
import numpy as np

# 标准白点 XYZ（D50 → 暖；D65 → 中性；D75 → 冷）
WHITE_POINTS = {
    'D50': np.array([0.96422, 1.00000, 0.82521]),
    'D55': np.array([0.95682, 1.00000, 0.92149]),
    'D65': np.array([0.95047, 1.00000, 1.08883]),
    'D75': np.array([0.94972, 1.00000, 1.22638]),
}

# Bradford 锥响应空间转换矩阵（ICC 标准）
_M_BRADFORD = np.array([
    [ 0.8951,  0.2664, -0.1614],
    [-0.7502,  1.7135,  0.0367],
    [ 0.0389, -0.0685,  1.0296],
])
_M_BRADFORD_INV = np.linalg.inv(_M_BRADFORD)

# 备选：von Kries（更老）和 CAT02（更新）
_M_VON_KRIES = np.array([
    [ 0.4002, 0.7076, -0.0808],
    [-0.2263, 1.1653,  0.0457],
    [ 0,      0,       0.9182],
])
_M_VON_KRIES_INV = np.linalg.inv(_M_VON_KRIES)

_M_CAT02 = np.array([
    [ 0.7328, 0.4296, -0.1624],
    [-0.7036, 1.6975,  0.0061],
    [ 0.0030, 0.0136,  0.9834],
])
_M_CAT02_INV = np.linalg.inv(_M_CAT02)

_METHODS = {
    'bradford':  (_M_BRADFORD, _M_BRADFORD_INV),
    'von_kries': (_M_VON_KRIES, _M_VON_KRIES_INV),
    'cat02':     (_M_CAT02, _M_CAT02_INV),
}


def adapt_xyz(xyz, src='D65', dst='D50', method='bradford'):
    """XYZ 色彩在两个白点间转换.

    src, dst : 任一标准白点名（'D50'/'D55'/'D65'/'D75'）或 (X,Y,Z) 数组
    method   : 'bradford'（ICC 推荐）/ 'von_kries' / 'cat02'（更现代）
    """
    M, Minv = _METHODS[method]
    if isinstance(src, str): src = WHITE_POINTS[src]
    if isinstance(dst, str): dst = WHITE_POINTS[dst]
    src = np.asarray(src, dtype=float); dst = np.asarray(dst, dtype=float)

    src_lms = M @ src
    dst_lms = M @ dst
    # 缩放矩阵
    scale = np.diag(dst_lms / src_lms)
    # 完整变换 = Minv @ scale @ M
    T = Minv @ scale @ M
    xyz = np.asarray(xyz, dtype=float)
    if xyz.ndim == 1:
        return T @ xyz
    return xyz @ T.T


def adapt_rgb_for_print(rgb, method='bradford'):
    """快捷方式：屏幕 D65 sRGB → 印刷 D50 XYZ → D50 sRGB.

    把屏幕上看到的颜色"适配"到 D50 标准（印刷物理黑白点接近 D50）。
    返回的 RGB 仍然是 [0,1] 但已做过白点偏移。
    """
    from color_lab import srgb_to_xyz, xyz_to_srgb
    xyz_d65 = srgb_to_xyz(rgb)
    xyz_d50 = adapt_xyz(xyz_d65, 'D65', 'D50', method)
    return xyz_to_srgb(xyz_d50)


def color_temperature(xyz):
    """McCamy 1992 公式从 xy 色度估算关联色温（CCT，单位 K）.

    适用于 2856~6500K 范围。结果误差通常 < 50K。
    """
    xyz = np.asarray(xyz, dtype=float)
    s = xyz.sum() if xyz.ndim == 1 else xyz.sum(axis=-1, keepdims=False)
    x = xyz[..., 0] / s
    y = xyz[..., 1] / s
    n = (x - 0.3320) / (0.1858 - y)
    return float(437*n**3 + 3601*n**2 + 6861*n + 5517)


if __name__ == '__main__':
    from color_lab import srgb_to_xyz, xyz_to_srgb, hex_to_rgb, rgb_to_hex

    print('=== 标准白点 XYZ ===')
    for name, xyz in WHITE_POINTS.items():
        print(f'  {name}: {xyz}  → CCT ≈ {color_temperature(xyz):.0f}K')

    print('\n=== 屏幕 D65 → 印刷 D50（Bradford）===')
    for h in ['#0072B2', '#D55E00', '#009E73', '#FFFFFF']:
        rgb = np.array(hex_to_rgb(h))
        rgb_print = adapt_rgb_for_print(rgb)
        print(f'  {h}  →  {rgb_to_hex(rgb_print)}')

    print('\n=== 三种 CAT 方法对比（同色 D65 → D50）===')
    rgb = np.array(hex_to_rgb('#0072B2'))
    for m in ['bradford', 'von_kries', 'cat02']:
        out = adapt_rgb_for_print(rgb, method=m)
        print(f'  {m:10s} → {rgb_to_hex(out)}')
