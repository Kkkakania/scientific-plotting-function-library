"""generate_golden: 用 Python 端的 color_lab 算出一组参考值（"金标准"），
存成 JSON。MATLAB 端的测试脚本读这个文件后对自己实现做断言。

跑法::

    cd 科研绘图_函数库
    python tests/generate_golden.py     # → tests/golden_color_math.json
    matlab -batch "addpath('palettes/matlab'); run('tests/test_color_lab_matlab.m')"
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / 'palettes' / 'python'))

import numpy as np
from color_lab import (hex_to_rgb, rgb_to_hex, srgb_to_lab, lab_to_srgb,
                       lab_to_lch, lch_to_lab, delta_e_2000,
                       contrast_ratio, relative_luminance, simulate_cvd)

# 一组覆盖度好的测试 HEX
TEST_HEX = [
    '#000000', '#FFFFFF',                                    # 极端
    '#FF0000', '#00FF00', '#0000FF',                         # 三原色
    '#FFFF00', '#FF00FF', '#00FFFF',                         # 二级色
    '#0072B2', '#D55E00', '#009E73', '#CC79A7', '#F0E442',   # Wong 几个
    '#7F7F7F', '#404040', '#BFBFBF',                          # 灰阶
    '#1A6FDF', '#E8AA42', '#A23B72',                          # 中等饱和度
]


def round_(x, ndigits=6):
    """统一精度，方便跨语言比对（避免最后一位浮点偏差）."""
    if isinstance(x, (list, tuple)):
        return [round_(v, ndigits) for v in x]
    return float(round(float(x), ndigits))


def main():
    out = {'meta': {'description': 'golden color math values from Python color_lab.py',
                    'tolerance_recommended': 1e-4},
           'cases': []}

    for h in TEST_HEX:
        rgb = list(hex_to_rgb(h))
        lab = list(srgb_to_lab(np.array(rgb)))
        lch = list(lab_to_lch(np.array(lab)))
        Y = float(relative_luminance(np.array(rgb)))
        rgb_back = list(lab_to_srgb(np.array(lab)))
        cvd_d = list(simulate_cvd(np.array(rgb), 'deuteranopia'))
        cvd_p = list(simulate_cvd(np.array(rgb), 'protanopia'))
        out['cases'].append({
            'hex': h, 'rgb': round_(rgb),
            'lab': round_(lab), 'lch': round_(lch),
            'luminance': round_(Y),
            'lab_to_srgb': round_(rgb_back),
            'cvd_deut': round_(cvd_d), 'cvd_proto': round_(cvd_p),
        })

    # 两两 CIEDE2000 + 对比度
    pairs = []
    for i in range(0, len(TEST_HEX), 2):
        if i+1 >= len(TEST_HEX): break
        h1, h2 = TEST_HEX[i], TEST_HEX[i+1]
        rgb1, rgb2 = np.array(hex_to_rgb(h1)), np.array(hex_to_rgb(h2))
        lab1, lab2 = srgb_to_lab(rgb1), srgb_to_lab(rgb2)
        pairs.append({
            'hex1': h1, 'hex2': h2,
            'delta_e_2000': round_(float(delta_e_2000(lab1, lab2))),
            'contrast_ratio': round_(float(contrast_ratio(rgb1, rgb2))),
        })
    out['pairs'] = pairs

    p = ROOT / 'tests' / 'golden_color_math.json'
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f'wrote {len(out["cases"])} cases + {len(out["pairs"])} pairs → {p}')


if __name__ == '__main__':
    main()
