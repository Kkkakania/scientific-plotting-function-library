"""generator_selftest: 生成器自验闭环.

证明思路：用 palette_generator 在不同参数下生成调色板，立即用
palette_validator 体检。如果生成器数学正确，应该绝大多数能通过
（前提是参数合理）。

这套测试也是最好的"生成器调参指南"——告诉你 L、C 设多大才能保证
色盲安全 + 灰度安全。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from palette_generator import (hcl_qualitative, oklch_qualitative,
                                hcl_sequential, oklch_sequential,
                                hcl_diverging, oklch_diverging)
from palette_validator import (min_pairwise_delta_e, cvd_min_delta_e)
from color_lab import grayscale_safe


def grade(d, thr=8): return '✓' if d > thr else '!'


def test_qualitative():
    print('=== 分类生成器自验（n=8）===')
    print('生成器           L    C    正常ΔE  绿盲ΔE  灰度ΔL  评判')
    print('-' * 70)
    rows = []
    # CIE Lab HCL
    for L, C in [(50, 50), (55, 60), (60, 70), (65, 80), (70, 60)]:
        pal = hcl_qualitative(n=8, L=L, C=C)
        dE, _ = min_pairwise_delta_e(pal)
        d_deut, _ = cvd_min_delta_e(pal, 'deuteranopia')
        ok_g, dL = grayscale_safe(pal)
        cb_ok = d_deut > 8
        rows.append({'gen':'hcl_qualitative','L':L,'C':C,
                     'dE':dE,'d_deut':d_deut,'dL':dL,
                     'cb':cb_ok,'gray':ok_g})
        print(f'  hcl_qualitative  {L:<4} {C:<4} '
              f'{dE:6.1f} {grade(dE,15)}  {d_deut:6.1f} {grade(d_deut)}  '
              f'{dL:6.1f} {grade(dL,15)}  CB={cb_ok} GRAY={ok_g}')
    print()
    # OKLab HCL（新增）
    for L, C in [(0.55, 0.12), (0.60, 0.14), (0.65, 0.16),
                  (0.55, 0.15), (0.45, 0.18)]:
        pal = oklch_qualitative(n=8, L=L, C=C)
        dE, _ = min_pairwise_delta_e(pal)
        d_deut, _ = cvd_min_delta_e(pal, 'deuteranopia')
        ok_g, dL = grayscale_safe(pal)
        cb_ok = d_deut > 8
        rows.append({'gen':'oklch_qualitative','L':L,'C':C,
                     'dE':dE,'d_deut':d_deut,'dL':dL,
                     'cb':cb_ok,'gray':ok_g})
        print(f'  oklch_qualitative {L:<4.2f} {C:<4.2f} '
              f'{dE:6.1f} {grade(dE,15)}  {d_deut:6.1f} {grade(d_deut)}  '
              f'{dL:6.1f} {grade(dL,15)}  CB={cb_ok} GRAY={ok_g}')
    return rows


def test_sequential():
    print('\n=== 顺序生成器自验（n=256，采样 8 点）===')
    print('生成器              色相  正常ΔE  绿盲ΔE  L单调  评判')
    print('-' * 70)
    rows = []
    for label, fn, hues in [
        ('hcl_sequential', hcl_sequential, [60, 130, 220, 280]),
        ('oklch_sequential', oklch_sequential, [60, 130, 220, 280]),
    ]:
        for hue in hues:
            cmap_pts = fn(n=8, hue=hue, as_hex=False)
            from color_lab import srgb_to_lab, rgb_to_hex
            labs = [srgb_to_lab(c) for c in cmap_pts]
            Ls = np.array([l[0] for l in labs])
            monotonic = np.all(np.diff(Ls) < 0) or np.all(np.diff(Ls) > 0)
            hexes = [rgb_to_hex(c) for c in cmap_pts]
            dE, _ = min_pairwise_delta_e(hexes)
            d_deut, _ = cvd_min_delta_e(hexes, 'deuteranopia')
            print(f'  {label:<18} {hue:<5} {dE:6.1f} {grade(dE,5)}  '
                  f'{d_deut:6.1f} {grade(d_deut,4)}  '
                  f'{"✓" if monotonic else "✗"}    OK={dE>5 and monotonic}')
            rows.append({'gen':label, 'hue':hue, 'dE':dE, 'd_deut':d_deut,
                          'monotonic':monotonic, 'ok':dE>5 and monotonic})
    return rows


def test_diverging():
    print('\n=== 发散生成器自验（n=256，采样 8 点）===')
    print('生成器              负相 正相  正常ΔE  绿盲ΔE  评判')
    print('-' * 70)
    rows = []
    for label, fn in [('hcl_diverging', hcl_diverging),
                       ('oklch_diverging', oklch_diverging)]:
        for h_neg, h_pos in [(240, 10), (220, 30), (180, 320)]:
            cmap_pts = fn(n=8, hue_neg=h_neg, hue_pos=h_pos, as_hex=False)
            from color_lab import rgb_to_hex
            hexes = [rgb_to_hex(c) for c in cmap_pts]
            dE, _ = min_pairwise_delta_e(hexes)
            d_deut, _ = cvd_min_delta_e(hexes, 'deuteranopia')
            rows.append({'gen':label, 'h_neg':h_neg, 'h_pos':h_pos,
                          'dE':dE, 'd_deut':d_deut})
            print(f'  {label:<18} {h_neg:<4} {h_pos:<4}  '
                  f'{dE:6.1f} {grade(dE,5)}  {d_deut:6.1f} {grade(d_deut,4)}')
    return rows


def main():
    r1 = test_qualitative()
    r2 = test_sequential()
    r3 = test_diverging()

    # 汇总：找最佳推荐
    print('\n=== 推荐配置（达到 CB ✓ + GRAY ✓ 的）===')
    best_q = [r for r in r1 if r['cb'] and r['gray']]
    if best_q:
        for r in best_q:
            print(f"  {r['gen']}(n=8, L={r['L']}, C={r['C']})")
    else:
        print('  (分类 8 色严格双安全确实很难，是这个领域的硬约束)')

    print('\n=== 顺序生成器都能通过基本检验 ===')
    pass_seq = sum(1 for r in r2 if r['ok'])
    print(f'  {pass_seq}/{len(r2)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
