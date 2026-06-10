"""apca: APCA 对比度（Accessible Perception of Color Algorithm）.

WCAG 2 用的对比度公式（(L1+0.05)/(L2+0.05)）有几个公认问题：
- 暗色文本和暗色背景常被误判（WCAG 数高，实际看不清）
- 不区分文本和背景的极性（黑底白字 vs 白底黑字一样的分数）
- 在中灰范围下经验上不准

APCA 是 WCAG 3 草案里推荐的新算法（Andrew Somers 设计），
基于"感知亮度差"和"软裁剪"两个心理物理学概念。
- 返回值有正负号：正 = 暗文本配亮背景，负 = 亮文本配暗背景
- 数值范围约 -108 ~ +106；阈值见 SC_THRESHOLDS

阈值建议（APCA 公开草案）
-----------------------
|Lc| < 15  : 不可读
|Lc| 15-30 : 仅适合 24pt+ 大字
|Lc| 30-45 : 18pt+
|Lc| 45-60 : 14pt+
|Lc| 60-75 : 正文 12pt（body text 推荐线）
|Lc| 75+   : 极佳

API
---
    apca(text_rgb, bg_rgb) -> float    # 返回 Lc（带符号）
    apca_grade(text_rgb, bg_rgb)       # 返回字号建议（'body' / 'large' / 'fail'）
"""
import numpy as np


# APCA 常数（公开草案 0.0.98G-4g）
_NTX = 0.57   # text power, normal
_NBG = 0.56   # bg power, normal
_RTX = 0.62   # text power, reverse
_RBG = 0.65   # bg power, reverse
_BoW = 1.14   # scale factor, dark text on light bg
_WoB = 1.14   # scale factor, light text on dark bg
_LOC = 0.027  # clamp offset
_CLAMP = 0.1  # near-black clamp


def _Ys(rgb):
    """APCA 的"灵敏度调整"亮度（不同于 WCAG 2 的相对亮度）."""
    r, g, b = np.asarray(rgb, dtype=float).T if np.asarray(rgb).ndim > 1 \
              else np.asarray(rgb, dtype=float)
    Y = 0.2126729 * r**2.4 + 0.7151522 * g**2.4 + 0.0721750 * b**2.4
    return Y


def apca(text_rgb, bg_rgb):
    """计算 APCA Lc（带符号的"感知对比度"）.

    text_rgb, bg_rgb : [0, 1] sRGB
    返回浮点：正值 = 暗文本/亮背景，负值 = 亮文本/暗背景
    数值范围约 -108 ~ +106
    """
    Y_t = _Ys(text_rgb)
    Y_b = _Ys(bg_rgb)

    # 软裁剪到接近黑色（避免数值不稳定）
    if Y_t < _CLAMP:
        Y_t = Y_t + (_CLAMP - Y_t) ** 1.414
    if Y_b < _CLAMP:
        Y_b = Y_b + (_CLAMP - Y_b) ** 1.414

    # 防止两端相同
    if abs(Y_t - Y_b) < 0.0005:
        return 0.0

    if Y_b > Y_t:
        # 暗文本配亮背景（正方向）
        S = Y_b ** _NBG - Y_t ** _NTX
        Lc = S * _BoW
    else:
        # 亮文本配暗背景（负方向）
        S = Y_b ** _RBG - Y_t ** _RTX
        Lc = S * _WoB

    Lc *= 100
    # 死区裁剪：太低的对比直接归 0
    if abs(Lc) < 7.5:
        return 0.0
    # 衰减小对比
    if Lc > 0:   Lc -= _LOC * 100
    else:        Lc += _LOC * 100
    return float(Lc)


def apca_grade(text_rgb, bg_rgb):
    """返回字号可读性等级.

    'excellent' : 任意字号
    'body'      : ≥ 12pt 正文可用
    'large'     : 只适合 14pt+
    'extra_large': 只适合 18pt+
    'huge_only' : 24pt+
    'fail'      : 不可读
    """
    Lc = abs(apca(text_rgb, bg_rgb))
    if Lc >= 75: return 'excellent'
    if Lc >= 60: return 'body'
    if Lc >= 45: return 'large'
    if Lc >= 30: return 'extra_large'
    if Lc >= 15: return 'huge_only'
    return 'fail'


def compare_wcag_apca(text_rgb, bg_rgb):
    """两个标准的并排对比，方便看出 APCA 哪里改进了."""
    from color_lab import contrast_ratio
    cr = contrast_ratio(text_rgb, bg_rgb)
    lc = apca(text_rgb, bg_rgb)
    grade = apca_grade(text_rgb, bg_rgb)
    wcag = 'AAA' if cr >= 7 else ('AA' if cr >= 4.5 else 'FAIL')
    return {'wcag_ratio': cr, 'wcag_level': wcag,
            'apca_Lc': lc, 'apca_grade': grade}


if __name__ == '__main__':
    from color_lab import hex_to_rgb

    cases = [
        # 经典：白底黑字
        ('#000000', '#FFFFFF', '黑字白底'),
        # 暗文本配暗背景：WCAG 经常误判
        ('#445566', '#223344', '暗灰字暗灰底'),
        # 灰字白底
        ('#888888', '#FFFFFF', '中灰字白底'),
        # 中蓝白
        ('#1A6FDF', '#FFFFFF', '蓝字白底'),
        # 反极性
        ('#FFFFFF', '#1A1A1A', '白字深底'),
        # 极小对比
        ('#777777', '#888888', '两个灰'),
    ]
    print(f'{"组合":<14} {"WCAG 比":>10} {"WCAG 评":>8} {"APCA Lc":>10} {"APCA 评":>14}')
    print('-' * 70)
    for tx, bg, desc in cases:
        r = compare_wcag_apca(np.array(hex_to_rgb(tx)), np.array(hex_to_rgb(bg)))
        print(f'{desc:<14} {r["wcag_ratio"]:>9.2f}  {r["wcag_level"]:>6}   '
              f'{r["apca_Lc"]:>+9.1f}   {r["apca_grade"]:>12}')
