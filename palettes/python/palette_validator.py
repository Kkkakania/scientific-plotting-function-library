"""palette_validator: 全方位调色板体检.

体检项：
- 色盲（红/绿/蓝色盲 + 全色盲）下能否区分各类别
- 灰度打印是否仍可读
- WCAG 对比度（与白底、黑底各跑一次）
- 相邻色 CIEDE2000 色差（确保肉眼能分）

用法::

    from palette_validator import validate, validate_report

    ok = validate(['#0072B2', '#D55E00', '#009E73'])
    print(validate_report(my_palette))
"""
import numpy as np
from color_lab import (hex_to_rgb, simulate_cvd, contrast_ratio,
                       grayscale_safe, srgb_to_lab, delta_e_2000,
                       rgb_to_hex)


def _to_rgb_list(palette):
    return [hex_to_rgb(c) if isinstance(c, str) else tuple(c) for c in palette]


def min_pairwise_delta_e(palette):
    """所有颜色两两的最小色差（CIEDE2000）.

    经验阈值：
    - > 30  : 远远不同（轻松区分）
    - 15-30 : 较容易区分
    - 5-15  : 仔细看才能分
    - < 5   : 肉眼几乎一样
    """
    rgbs = _to_rgb_list(palette)
    labs = [srgb_to_lab(r) for r in rgbs]
    n = len(labs)
    dmin = np.inf
    pair = (None, None)
    for i in range(n):
        for j in range(i+1, n):
            d = delta_e_2000(labs[i], labs[j])
            if d < dmin:
                dmin = d; pair = (i, j)
    return float(dmin), pair


def cvd_min_delta_e(palette, kind='deuteranopia'):
    """在指定 CVD 下的最小两两色差."""
    sim = [simulate_cvd(np.array(c)) for c in _to_rgb_list(palette)]
    sim_hex = [rgb_to_hex(c) for c in sim]
    return min_pairwise_delta_e(sim_hex)


def wcag_summary(palette):
    """每个颜色对白底/黑底的对比度评级."""
    out = []
    for c in palette:
        rgb = hex_to_rgb(c) if isinstance(c, str) else tuple(c)
        cr_w = contrast_ratio(rgb, (1, 1, 1))
        cr_k = contrast_ratio(rgb, (0, 0, 0))
        out.append({
            'color': c if isinstance(c, str) else rgb_to_hex(rgb),
            'vs_white': float(cr_w),
            'vs_black': float(cr_k),
        })
    return out


def validate(palette, min_delta_e=15, min_gray_dL=15):
    """快速布尔判定：是否同时满足色盲安全 + 灰度安全 + 色差足够."""
    d_normal, _ = min_pairwise_delta_e(palette)
    if d_normal < min_delta_e: return False
    for kind in ('protanopia', 'deuteranopia', 'tritanopia'):
        d, _ = cvd_min_delta_e(palette, kind)
        if d < min_delta_e * 0.6:        # CVD 下放宽阈值
            return False
    ok_gray, _ = grayscale_safe(palette, min_dL=min_gray_dL)
    return ok_gray


def validate_report(palette):
    """生成可读的体检报告（字符串）."""
    rgbs = _to_rgb_list(palette)
    palette_hex = [c if isinstance(c, str) else rgb_to_hex(c) for c in palette]

    d_normal, pair_n = min_pairwise_delta_e(palette)
    d_prot, _ = cvd_min_delta_e(palette, 'protanopia')
    d_deut, _ = cvd_min_delta_e(palette, 'deuteranopia')
    d_trit, _ = cvd_min_delta_e(palette, 'tritanopia')
    ok_gray, gray_dL = grayscale_safe(palette)
    wcag = wcag_summary(palette)

    def lvl(d):  # 把 ΔE 转可读评级
        if d > 30: return f'✓ {d:5.1f}  优秀'
        if d > 15: return f'✓ {d:5.1f}  良好'
        if d > 5:  return f'! {d:5.1f}  勉强'
        return f'✗ {d:5.1f}  不行'

    lines = [f'调色板（{len(palette)} 色）: {", ".join(palette_hex)}', '']
    lines.append('— 色差体检（CIEDE2000，两两最小值，越大越易区分）')
    lines.append(f'  正常视觉      : {lvl(d_normal)}')
    lines.append(f'  红色盲(proto.): {lvl(d_prot)}')
    lines.append(f'  绿色盲(deut.) : {lvl(d_deut)}')
    lines.append(f'  蓝色盲(trit.) : {lvl(d_trit)}')
    lines.append('')
    lines.append(f'— 灰度打印安全（L 通道两两最小差）: '
                 f'{"✓" if ok_gray else "✗"} ΔL = {gray_dL:.1f}')
    lines.append('')
    lines.append('— WCAG 对比度（每色 vs 白/黑底）')
    lines.append('  色号       vs 白底         vs 黑底')
    for w in wcag:
        def grade(cr):
            if cr >= 7: return 'AAA'
            if cr >= 4.5: return 'AA '
            if cr >= 3: return 'AA*'
            return 'FAIL'
        lines.append(f'  {w["color"]}  {w["vs_white"]:5.2f}:1 {grade(w["vs_white"])}  '
                     f'{w["vs_black"]:5.2f}:1 {grade(w["vs_black"])}')
    return '\n'.join(lines)


if __name__ == '__main__':
    wong = ['#000000', '#E69F00', '#56B4E9', '#009E73',
            '#F0E442', '#0072B2', '#D55E00', '#CC79A7']
    print(validate_report(wong))
    print()
    print('Wong 通过快速校验？', validate(wong))
