"""color_lab: 色彩科学底层工具.

实现都基于公开标准：
- sRGB ↔ XYZ ↔ CIE Lab ↔ LCh 转换（CIE 标准）
- WCAG 2.1 相对亮度与对比度（W3C 规范）
- Brettel/Viénot/Mollon 色觉缺陷模拟（公开算法）
- 灰度可读性（按 Rec. 709 亮度系数）

所有数学都从零实现，可独立审核。
"""
import numpy as np


# ============ HEX ↔ RGB ============

def hex_to_rgb(h):
    """'#0072B2' → (0.0, 0.447, 0.698) in [0, 1]."""
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    r, g, b = [max(0, min(1, x)) for x in rgb]
    return '#{:02X}{:02X}{:02X}'.format(int(r*255+0.5), int(g*255+0.5), int(b*255+0.5))


# ============ sRGB ↔ 线性 RGB ↔ XYZ ============

def _gamma_inv(c):
    """sRGB 反伽马（公开规范）."""
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def _gamma(c):
    c = np.maximum(c, 0)        # 保险，防止负值喂给 power
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * c ** (1/2.4) - 0.055)


# sRGB → XYZ 矩阵（D65 白点，IEC 61966-2-1）
_M_RGB2XYZ = np.array([
    [0.4124564, 0.3575761, 0.1804375],
    [0.2126729, 0.7151522, 0.0721750],
    [0.0193339, 0.1191920, 0.9503041],
])
_M_XYZ2RGB = np.linalg.inv(_M_RGB2XYZ)


def srgb_to_xyz(rgb):
    rgb = np.asarray(rgb, dtype=float)
    lin = _gamma_inv(rgb)
    return lin @ _M_RGB2XYZ.T


def xyz_to_srgb(xyz, clip=True):
    rgb_lin = np.asarray(xyz, dtype=float) @ _M_XYZ2RGB.T
    rgb = _gamma(rgb_lin)
    return np.clip(rgb, 0, 1) if clip else rgb


# ============ XYZ ↔ Lab ↔ LCh ============

# D65 白点
_Xn, _Yn, _Zn = 0.95047, 1.0, 1.08883


def _f(t):
    delta = 6/29
    return np.where(t > delta**3, t**(1/3), t / (3*delta**2) + 4/29)


def _f_inv(t):
    delta = 6/29
    return np.where(t > delta, t**3, 3*delta**2 * (t - 4/29))


def xyz_to_lab(xyz):
    xyz = np.asarray(xyz, dtype=float)
    fx = _f(xyz[..., 0] / _Xn)
    fy = _f(xyz[..., 1] / _Yn)
    fz = _f(xyz[..., 2] / _Zn)
    L = 116*fy - 16
    a = 500*(fx - fy)
    b = 200*(fy - fz)
    return np.stack([L, a, b], axis=-1)


def lab_to_xyz(lab):
    lab = np.asarray(lab, dtype=float)
    fy = (lab[..., 0] + 16) / 116
    fx = fy + lab[..., 1] / 500
    fz = fy - lab[..., 2] / 200
    X = _Xn * _f_inv(fx)
    Y = _Yn * _f_inv(fy)
    Z = _Zn * _f_inv(fz)
    return np.stack([X, Y, Z], axis=-1)


def srgb_to_lab(rgb):
    return xyz_to_lab(srgb_to_xyz(rgb))


def lab_to_srgb(lab, clip=True):
    return xyz_to_srgb(lab_to_xyz(lab), clip=clip)


def lab_to_lch(lab):
    """Lab → LCh：L 不变，C = √(a²+b²)，h = atan2(b, a)（度）."""
    lab = np.asarray(lab, dtype=float)
    L = lab[..., 0]
    C = np.hypot(lab[..., 1], lab[..., 2])
    h = np.degrees(np.arctan2(lab[..., 2], lab[..., 1])) % 360
    return np.stack([L, C, h], axis=-1)


def lch_to_lab(lch):
    lch = np.asarray(lch, dtype=float)
    L = lch[..., 0]
    a = lch[..., 1] * np.cos(np.radians(lch[..., 2]))
    b = lch[..., 1] * np.sin(np.radians(lch[..., 2]))
    return np.stack([L, a, b], axis=-1)


# ============ 色差（CIE76 与 CIEDE2000） ============

def delta_e_76(lab1, lab2):
    """ΔE*ab 1976 —— 简单欧氏距离."""
    return np.linalg.norm(np.asarray(lab1) - np.asarray(lab2), axis=-1)


def delta_e_2000(lab1, lab2):
    """CIEDE2000 色差（CIE 推荐，更符合人眼感知）."""
    lab1 = np.asarray(lab1, dtype=float); lab2 = np.asarray(lab2, dtype=float)
    L1, a1, b1 = lab1[..., 0], lab1[..., 1], lab1[..., 2]
    L2, a2, b2 = lab2[..., 0], lab2[..., 1], lab2[..., 2]
    C1 = np.hypot(a1, b1); C2 = np.hypot(a2, b2)
    Cbar = (C1 + C2) / 2
    G = 0.5 * (1 - np.sqrt(Cbar**7 / (Cbar**7 + 25**7)))
    a1p = (1 + G) * a1; a2p = (1 + G) * a2
    C1p = np.hypot(a1p, b1); C2p = np.hypot(a2p, b2)
    h1p = np.degrees(np.arctan2(b1, a1p)) % 360
    h2p = np.degrees(np.arctan2(b2, a2p)) % 360
    dLp = L2 - L1
    dCp = C2p - C1p
    dhp = h2p - h1p
    dhp = np.where(dhp > 180, dhp - 360, dhp)
    dhp = np.where(dhp < -180, dhp + 360, dhp)
    dHp = 2 * np.sqrt(C1p * C2p) * np.sin(np.radians(dhp) / 2)
    Lbarp = (L1 + L2) / 2
    Cbarp = (C1p + C2p) / 2
    hbarp = (h1p + h2p) / 2
    hbarp = np.where(np.abs(h1p - h2p) > 180, hbarp + 180, hbarp)
    T = (1 - 0.17*np.cos(np.radians(hbarp - 30))
           + 0.24*np.cos(np.radians(2*hbarp))
           + 0.32*np.cos(np.radians(3*hbarp + 6))
           - 0.20*np.cos(np.radians(4*hbarp - 63)))
    SL = 1 + (0.015 * (Lbarp - 50)**2) / np.sqrt(20 + (Lbarp - 50)**2)
    SC = 1 + 0.045 * Cbarp
    SH = 1 + 0.015 * Cbarp * T
    dTheta = 30 * np.exp(-((hbarp - 275)/25)**2)
    RC = 2 * np.sqrt(Cbarp**7 / (Cbarp**7 + 25**7))
    RT = -RC * np.sin(np.radians(2 * dTheta))
    return np.sqrt((dLp/SL)**2 + (dCp/SC)**2 + (dHp/SH)**2
                   + RT * (dCp/SC) * (dHp/SH))


# ============ WCAG 对比度 ============

def relative_luminance(rgb):
    """WCAG 2.1 相对亮度（W3C 规范）."""
    rgb = np.asarray(rgb, dtype=float)
    lin = _gamma_inv(rgb)
    return 0.2126*lin[..., 0] + 0.7152*lin[..., 1] + 0.0722*lin[..., 2]


def contrast_ratio(c1, c2):
    """WCAG 对比度，1:1 到 21:1."""
    L1 = relative_luminance(c1); L2 = relative_luminance(c2)
    lighter = np.maximum(L1, L2); darker = np.minimum(L1, L2)
    return (lighter + 0.05) / (darker + 0.05)


def wcag_level(c1, c2, text='normal'):
    """评级：返回 'AAA' / 'AA' / 'FAIL'.

    阈值（W3C 规范）：
    - normal text: AA ≥ 4.5, AAA ≥ 7
    - large text:  AA ≥ 3,   AAA ≥ 4.5
    """
    cr = contrast_ratio(c1, c2)
    if text == 'large':
        return 'AAA' if cr >= 4.5 else ('AA' if cr >= 3.0 else 'FAIL')
    return 'AAA' if cr >= 7.0 else ('AA' if cr >= 4.5 else 'FAIL')


# ============ 色觉缺陷（CVD）模拟 ============

# Brettel/Viénot/Mollon 模拟矩阵（公开算法的简化稳健版）
# 输入：线性 sRGB；输出：模拟后线性 sRGB
_CVD_MATS = {
    # 红色盲（protanopia）
    'protanopia': np.array([
        [0.152286, 1.052583, -0.204868],
        [0.114503, 0.786281,  0.099216],
        [-0.003882,-0.048116,  1.051998],
    ]),
    # 绿色盲（deuteranopia）
    'deuteranopia': np.array([
        [0.367322, 0.860646, -0.227968],
        [0.280085, 0.672501,  0.047413],
        [-0.011820, 0.042940,  0.968881],
    ]),
    # 蓝色盲（tritanopia）
    'tritanopia': np.array([
        [1.255528,-0.076749, -0.178779],
        [-0.078411,0.930809,  0.147602],
        [0.004733, 0.691367,  0.303900],
    ]),
}


def simulate_cvd(rgb, kind='deuteranopia'):
    """模拟色觉缺陷下看到的颜色（接收 [0,1] sRGB，返回 [0,1] sRGB）."""
    if kind == 'achromatopsia':                  # 全色盲：按 Rec. 709 亮度
        L = relative_luminance(rgb)
        return np.stack([L, L, L], axis=-1) if np.asarray(rgb).ndim > 1 \
               else (L, L, L)
    M = _CVD_MATS[kind]
    lin = _gamma_inv(np.asarray(rgb, dtype=float))
    sim_lin = lin @ M.T
    sim_lin = np.clip(sim_lin, 0, 1)
    return _gamma(sim_lin)


# ============ 灰度可读性 ============

def grayscale_safe(palette, min_dL=15):
    """判断分类调色板的颜色在灰度打印后是否仍可区分.

    返回 (ok: bool, min_dL: float)。
    min_dL 是 Lab 空间 L 通道两两差的最小值。
    阈值 15 是经验值——再小就肉眼很难分。
    """
    labs = [srgb_to_lab(hex_to_rgb(c) if isinstance(c, str) else c) for c in palette]
    Ls = np.array([lab[0] for lab in labs])
    diffs = np.abs(Ls[:, None] - Ls[None, :])
    np.fill_diagonal(diffs, np.inf)
    m = diffs.min()
    return m >= min_dL, m


# ============ 一些方便的转换批处理 ============

def palette_to_lab(palette):
    """把 hex/RGB 列表批量转 Lab."""
    return np.array([srgb_to_lab(hex_to_rgb(c) if isinstance(c, str) else c)
                     for c in palette])


def palette_to_lch(palette):
    return lab_to_lch(palette_to_lab(palette))


# ============ HSV / HSL（经典模型，方便取色器对接） ============

def rgb_to_hsv(rgb):
    """sRGB → HSV. h ∈ [0, 360), s, v ∈ [0, 1]."""
    r, g, b = np.asarray(rgb, dtype=float).T if np.asarray(rgb).ndim > 1 \
              else np.asarray(rgb, dtype=float)
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    d = mx - mn
    h = np.zeros_like(mx)
    mask = d > 0
    if np.any(mx == r):
        h = np.where((mx == r) & mask, ((g - b) / np.where(d == 0, 1, d)) % 6, h)
    h = np.where((mx == g) & mask, (b - r) / np.where(d == 0, 1, d) + 2, h)
    h = np.where((mx == b) & mask, (r - g) / np.where(d == 0, 1, d) + 4, h)
    h = h * 60 % 360
    s = np.where(mx > 0, d / np.where(mx == 0, 1, mx), 0)
    v = mx
    return np.stack([h, s, v], axis=-1) if np.asarray(rgb).ndim > 1 else (float(h), float(s), float(v))


def hsv_to_rgb(hsv):
    h, s, v = np.asarray(hsv, dtype=float).T if np.asarray(hsv).ndim > 1 \
              else np.asarray(hsv, dtype=float)
    c = v * s
    hp = h / 60
    x = c * (1 - np.abs(hp % 2 - 1))
    z = np.zeros_like(c)
    cases = np.stack([
        np.stack([c, x, z], axis=-1),
        np.stack([x, c, z], axis=-1),
        np.stack([z, c, x], axis=-1),
        np.stack([z, x, c], axis=-1),
        np.stack([x, z, c], axis=-1),
        np.stack([c, z, x], axis=-1),
    ])
    idx = np.clip(np.floor(hp).astype(int), 0, 5)
    if cases.ndim == 2:
        rgb1 = cases[idx]
    else:
        rgb1 = np.take_along_axis(cases, idx[None, ..., None], axis=0)[0]
    m = v - c
    return rgb1 + np.expand_dims(m, -1) if np.asarray(hsv).ndim > 1 else tuple(rgb1 + m)


def rgb_to_hsl(rgb):
    """sRGB → HSL. h ∈ [0, 360), s, l ∈ [0, 1]."""
    rgb = np.asarray(rgb, dtype=float)
    r, g, b = rgb.T if rgb.ndim > 1 else rgb
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    L = (mx + mn) / 2
    d = mx - mn
    s = np.where(d == 0, 0, d / (1 - np.abs(2*L - 1) + 1e-12))
    hsv = rgb_to_hsv(rgb)
    h = hsv[..., 0] if rgb.ndim > 1 else hsv[0]
    return np.stack([h, s, L], axis=-1) if rgb.ndim > 1 else (float(h), float(s), float(L))


# ============ OKLab / OKLCh（Björn Ottosson 2020 公开） ============

# RGB（线性）→ LMS 锥响应矩阵
_M_RGB2LMS = np.array([
    [0.4122214708, 0.5363325363, 0.0514459929],
    [0.2119034982, 0.6806995451, 0.1073969566],
    [0.0883024619, 0.2817188376, 0.6299787005],
])

_M_LMS2OKLAB = np.array([
    [0.2104542553,  0.7936177850, -0.0040720468],
    [1.9779984951, -2.4285922050,  0.4505937099],
    [0.0259040371,  0.7827717662, -0.8086757660],
])

_M_OKLAB2LMS = np.linalg.inv(_M_LMS2OKLAB)
_M_LMS2RGB  = np.linalg.inv(_M_RGB2LMS)


def srgb_to_oklab(rgb):
    """sRGB → OKLab.

    OKLab 比 CIE Lab 在感知均匀性上明显更优（特别是蓝色域）。
    L ∈ [0, 1], a/b 通常 ∈ [-0.4, 0.4].
    """
    rgb = np.asarray(rgb, dtype=float)
    lin = _gamma_inv(rgb)
    lms = lin @ _M_RGB2LMS.T
    lms_ = np.cbrt(lms)
    return lms_ @ _M_LMS2OKLAB.T


def oklab_to_srgb(oklab, clip=True):
    oklab = np.asarray(oklab, dtype=float)
    lms_ = oklab @ _M_OKLAB2LMS.T
    lms = lms_ ** 3
    rgb_lin = lms @ _M_LMS2RGB.T
    rgb = _gamma(rgb_lin)
    return np.clip(rgb, 0, 1) if clip else rgb


def oklab_to_oklch(oklab):
    """OKLab → OKLCh: L 不变, C = √(a²+b²), h = atan2(b, a)°."""
    oklab = np.asarray(oklab, dtype=float)
    L = oklab[..., 0]
    C = np.hypot(oklab[..., 1], oklab[..., 2])
    h = np.degrees(np.arctan2(oklab[..., 2], oklab[..., 1])) % 360
    return np.stack([L, C, h], axis=-1)


def oklch_to_oklab(oklch):
    oklch = np.asarray(oklch, dtype=float)
    L = oklch[..., 0]
    a = oklch[..., 1] * np.cos(np.radians(oklch[..., 2]))
    b = oklch[..., 1] * np.sin(np.radians(oklch[..., 2]))
    return np.stack([L, a, b], axis=-1)


# ============ 部分色觉缺陷（异常三色觉） ============

def simulate_cvd_partial(rgb, kind='deuteranopia', severity=1.0):
    """连续严重程度的色觉缺陷模拟.

    severity = 0 完全正常, 1 完全色盲（与 simulate_cvd 一致）.
    用于模拟"色弱"（异常三色觉），比如 deuteranomaly 约 severity ≈ 0.5.
    """
    severity = float(np.clip(severity, 0, 1))
    if severity == 0: return np.asarray(rgb, dtype=float)
    sim = simulate_cvd(rgb, kind)
    rgb = np.asarray(rgb, dtype=float)
    return (1 - severity) * rgb + severity * sim


if __name__ == '__main__':
    # 自检：往返误差
    test = ['#0072B2', '#D55E00', '#009E73']
    for h in test:
        rgb = hex_to_rgb(h)
        lab = srgb_to_lab(rgb)
        rgb2 = lab_to_srgb(lab)
        err = np.max(np.abs(np.array(rgb) - rgb2))
        print(f'{h}: round-trip err = {err:.6f}')
    # 对比度
    print(f'\nWCAG: 白底黑字对比度 = {contrast_ratio((1,1,1), (0,0,0)):.1f}:1 → {wcag_level((1,1,1), (0,0,0))}')
    # CVD
    print(f'\nCVD: 蓝色 #0072B2 在绿色盲下看 = {rgb_to_hex(simulate_cvd(hex_to_rgb("#0072B2"), "deuteranopia"))}')
