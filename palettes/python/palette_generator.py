"""palette_generator: 程序化生成感知均匀调色板.

基于 CIE Lab/LCh 空间，不再靠手挑色。

四种生成器：
- hcl_sequential(n, hue, ...)        单色相 / 多色相顺序色板
- hcl_diverging(n, hue1, hue2, ...)  发散色板（两端各一种色相，中间过渡）
- hcl_qualitative(n, L, C, ...)      色相等距的分类色板
- gradient(stops_lab, n)             从任意 Lab 锚点插值

设计原则：
1. **L 通道单调变化** → 灰度打印仍能区分明暗
2. **色相在 LCh 空间均匀** → 避免视觉拥挤
3. **C（彩度）可控** → 跟期刊风格匹配

用法::

    from palette_generator import hcl_sequential, hcl_qualitative
    from matplotlib.colors import LinearSegmentedColormap

    cmap_hex = hcl_sequential(n=256, hue=240, L_range=(95, 30), C_max=70)
    cmap = LinearSegmentedColormap.from_list('my_blue', cmap_hex)
"""
import numpy as np
from color_lab import lab_to_srgb, lch_to_lab, rgb_to_hex, srgb_to_lab, lab_to_lch


# ============ 顺序色板 ============

def hcl_sequential(n=256, hue=240, L_range=(95, 25), C_max=70, C_min=10,
                   power_L=1.0, power_C=1.0, as_hex=False):
    """单色相顺序色板.

    参数
    ----
    n       : 颜色数
    hue     : 色相角（0~360 度）
    L_range : (L_high, L_low)，从亮到暗
    C_max   : 中间附近最大彩度
    C_min   : 两端最小彩度
    power_L : L 通道幂次（>1 → 偏暗，<1 → 偏亮）
    power_C : 彩度幂次

    返回 list[(R,G,B)] 或 list[hex]
    """
    t = np.linspace(0, 1, n)
    L = L_range[0] + (L_range[1] - L_range[0]) * t**power_L
    # 彩度抛物线：两端低，中间高
    C = C_min + (C_max - C_min) * (1 - np.abs(2*t - 1)**power_C) ** 0.7
    h = np.full(n, hue)
    lch = np.stack([L, C, h], axis=-1)
    rgb = lab_to_srgb(lch_to_lab(lch))
    if as_hex: return [rgb_to_hex(c) for c in rgb]
    return rgb


def hcl_sequential_multi_hue(n=256, hue_start=240, hue_end=10,
                              L_range=(95, 25), C_max=70, as_hex=False):
    """多色相顺序色板（hue 从 start 平滑过渡到 end）."""
    t = np.linspace(0, 1, n)
    L = L_range[0] + (L_range[1] - L_range[0]) * t
    # hue 用最短角度路径
    dh = (hue_end - hue_start) % 360
    if dh > 180: dh -= 360
    h = (hue_start + dh * t) % 360
    C = 10 + (C_max - 10) * (1 - np.abs(2*t - 1)**1.5) ** 0.7
    lch = np.stack([L, C, h], axis=-1)
    rgb = lab_to_srgb(lch_to_lab(lch))
    if as_hex: return [rgb_to_hex(c) for c in rgb]
    return rgb


# ============ 发散色板 ============

def hcl_diverging(n=256, hue_neg=240, hue_pos=10,
                  L_mid=97, L_end=30, C_max=75, power=1.0, as_hex=False):
    """发散色板：两端各一种色相，中间过白（或浅灰）.

    适合表达"正负偏离中心"的数据（误差、相关系数、温度异常）。
    """
    t = np.linspace(-1, 1, n)
    a = np.abs(t)
    L = L_mid - (L_mid - L_end) * a**power
    C = C_max * a**power
    h = np.where(t < 0, hue_neg, hue_pos).astype(float)
    lch = np.stack([L, C, h], axis=-1)
    rgb = lab_to_srgb(lch_to_lab(lch))
    if as_hex: return [rgb_to_hex(c) for c in rgb]
    return rgb


# ============ 分类色板（色相等距） ============

def hcl_qualitative(n=8, L=60, C=70, h_start=15, h_range=360, as_hex=True):
    """分类色板：n 个色相在 LCh 平面上等距分布.

    L=60 是常用值（足够深以避免在白底淡化，又不至于太暗）。
    C=70 是中等饱和度；想更素就降到 40~55。

    返回 hex 列表（默认）或 RGB 列表。
    """
    hues = (h_start + np.arange(n) * (h_range / n)) % 360
    L_arr = np.full(n, L); C_arr = np.full(n, C)
    lch = np.stack([L_arr, C_arr, hues], axis=-1)
    rgb = lab_to_srgb(lch_to_lab(lch))
    if as_hex: return [rgb_to_hex(c) for c in rgb]
    return rgb


# ============ 任意 Lab 锚点插值 ============

def gradient(lab_stops, n=256, as_hex=False):
    """在任意 Lab 锚点之间做线性插值.

    lab_stops : list of (L, a, b) 或 list of hex
    """
    # 把 hex 转 Lab
    stops = []
    for s in lab_stops:
        if isinstance(s, str):
            stops.append(srgb_to_lab(
                tuple(int(s.lstrip('#')[i:i+2], 16)/255 for i in (0, 2, 4))
            ))
        else:
            stops.append(np.asarray(s, dtype=float))
    stops = np.array(stops)
    ts = np.linspace(0, 1, len(stops))
    t_query = np.linspace(0, 1, n)
    L = np.interp(t_query, ts, stops[:, 0])
    a = np.interp(t_query, ts, stops[:, 1])
    b = np.interp(t_query, ts, stops[:, 2])
    lab = np.stack([L, a, b], axis=-1)
    rgb = lab_to_srgb(lab)
    if as_hex: return [rgb_to_hex(c) for c in rgb]
    return rgb


# ============ 色相和声学（color harmonies） ============

def harmony(base_hex, kind='complementary'):
    """从一个基色生成色相和声.

    - complementary    : 互补色（h + 180）
    - analogous        : 类比色（h±30）
    - triadic          : 三色（h, h+120, h+240）
    - tetradic         : 四色（h, h+90, h+180, h+270）
    - split_complement : 分裂互补（h, h+150, h+210）

    返回 hex 列表。
    """
    rgb = tuple(int(base_hex.lstrip('#')[i:i+2], 16)/255 for i in (0, 2, 4))
    lch = lab_to_lch(srgb_to_lab(rgb))
    L, C, h = lch[0], lch[1], lch[2]
    if kind == 'complementary':       hues = [h, (h+180) % 360]
    elif kind == 'analogous':         hues = [(h-30) % 360, h, (h+30) % 360]
    elif kind == 'triadic':           hues = [h, (h+120) % 360, (h+240) % 360]
    elif kind == 'tetradic':          hues = [h, (h+90) % 360, (h+180) % 360, (h+270) % 360]
    elif kind == 'split_complement':  hues = [h, (h+150) % 360, (h+210) % 360]
    else: raise ValueError(kind)
    lchs = np.array([[L, C, hh] for hh in hues])
    rgbs = lab_to_srgb(lch_to_lab(lchs))
    return [rgb_to_hex(c) for c in rgbs]


# ============ 调整已有调色板 ============

def lighten(color, amount=10):
    """把单色在 Lab L 通道上 +amount."""
    rgb = tuple(int(color.lstrip('#')[i:i+2], 16)/255 for i in (0, 2, 4)) \
          if isinstance(color, str) else color
    lab = srgb_to_lab(rgb)
    lab[..., 0] = np.clip(lab[..., 0] + amount, 0, 100)
    out = lab_to_srgb(lab)
    return rgb_to_hex(out) if isinstance(color, str) else tuple(out)


def darken(color, amount=10):
    return lighten(color, -amount)


def saturate(color, amount=10):
    """彩度增加（LCh 的 C 通道）."""
    rgb = tuple(int(color.lstrip('#')[i:i+2], 16)/255 for i in (0, 2, 4)) \
          if isinstance(color, str) else color
    lch = lab_to_lch(srgb_to_lab(rgb))
    lch[..., 1] = max(0, lch[..., 1] + amount)
    out = lab_to_srgb(lch_to_lab(lch))
    return rgb_to_hex(out) if isinstance(color, str) else tuple(out)


def desaturate(color, amount=10):
    return saturate(color, -amount)


# ============ OKLab 生成器（现代标准，比 CIE Lab 更感知均匀） ============

from color_lab import oklab_to_srgb, oklch_to_oklab


def oklch_qualitative(n=8, L=0.65, C=0.13, h_start=30, h_range=360, as_hex=True):
    """OKLab 空间分类色：色相在 OKLCh 上等距分布.

    OKLab 的优势：蓝紫色域不再"挤"，色相均匀感更接近人眼真实判断。

    参数
    ----
    n       : 颜色数
    L       : 明度（OKLab 的 L ∈ [0, 1]）；推荐 0.55~0.70
    C       : 彩度；推荐 0.10~0.18（>0.20 可能超出 sRGB 色域被裁剪）
    h_start : 起始色相（度）
    h_range : 色相总跨度（度，默认 360 全圈均匀）

    返回 list[hex]（默认）或 list[RGB]。
    """
    hues = (h_start + np.arange(n) * (h_range / n)) % 360
    L_arr = np.full(n, L); C_arr = np.full(n, C)
    oklch = np.stack([L_arr, C_arr, hues], axis=-1)
    rgb = oklab_to_srgb(oklch_to_oklab(oklch))
    if as_hex:
        from color_lab import rgb_to_hex
        return [rgb_to_hex(c) for c in rgb]
    return rgb


def oklch_sequential(n=256, hue=240, L_range=(0.95, 0.30),
                      C_max=0.15, C_min=0.02, as_hex=False):
    """OKLab 顺序色板：单色相，明度+彩度递变.

    L_range : (L_high, L_low)，从亮到暗
    C_max   : 中段彩度峰值
    """
    t = np.linspace(0, 1, n)
    L = L_range[0] + (L_range[1] - L_range[0]) * t
    # 彩度抛物：两端低，中间高
    C = C_min + (C_max - C_min) * (1 - np.abs(2*t - 1)) ** 0.7
    h = np.full(n, hue)
    oklch = np.stack([L, C, h], axis=-1)
    rgb = oklab_to_srgb(oklch_to_oklab(oklch))
    if as_hex:
        from color_lab import rgb_to_hex
        return [rgb_to_hex(c) for c in rgb]
    return rgb


def oklch_diverging(n=256, hue_neg=240, hue_pos=30,
                     L_mid=0.95, L_end=0.35, C_max=0.18, as_hex=False):
    """OKLab 发散色板：负端 hue_neg、正端 hue_pos，中心浅."""
    t = np.linspace(-1, 1, n)
    a = np.abs(t)
    L = L_mid - (L_mid - L_end) * a
    C = C_max * a
    h = np.where(t < 0, hue_neg, hue_pos).astype(float)
    oklch = np.stack([L, C, h], axis=-1)
    rgb = oklab_to_srgb(oklch_to_oklab(oklch))
    if as_hex:
        from color_lab import rgb_to_hex
        return [rgb_to_hex(c) for c in rgb]
    return rgb


if __name__ == '__main__':
    # 演示：4 种生成器各出一组
    print('hcl_qualitative(6):')
    print(' ', hcl_qualitative(n=6, L=55, C=65))
    print('\nhcl_sequential(5, hue=220):')
    print(' ', hcl_sequential(n=5, hue=220, as_hex=True))
    print('\nhcl_diverging(5):')
    print(' ', hcl_diverging(n=5, as_hex=True))
    print('\nharmony("#0072B2", "triadic"):')
    print(' ', harmony('#0072B2', 'triadic'))
