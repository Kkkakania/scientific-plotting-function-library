"""audit_all: 对全部 68 套预设调色板做体检，输出 Markdown 报告.

体检维度（与 palette_validator 一致）：
- 正常视觉两两最小 CIEDE2000
- 红/绿/蓝色盲下的最小色差
- 灰度打印 L 通道两两最小差
- 综合通过/警告/失败
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pathlib import Path
import numpy as np

from sci_palettes import PALETTES_CAT, PALETTES_SEQ, PALETTES_DIV, PALETTES_CYC, get_palette
from palette_validator import min_pairwise_delta_e, cvd_min_delta_e
from color_lab import grayscale_safe, hex_to_rgb, rgb_to_hex


def grade(d, thr_good=15, thr_ok=5):
    if d >= thr_good: return '✓'
    if d >= thr_ok:   return '!'
    return '✗'


def audit_categorical(name, colors):
    d_n, _ = min_pairwise_delta_e(colors)
    d_p, _ = cvd_min_delta_e(colors, 'protanopia')
    d_d, _ = cvd_min_delta_e(colors, 'deuteranopia')
    d_t, _ = cvd_min_delta_e(colors, 'tritanopia')
    ok_gray, dL = grayscale_safe(colors)
    overall = '✓' if (d_n > 15 and d_d > 8 and dL > 15) else (
              '!' if (d_n > 10 and d_d > 5) else '✗')
    return dict(name=name, n=len(colors), dE_n=d_n, dE_p=d_p, dE_d=d_d, dE_t=d_t,
                gray_dL=dL, overall=overall)


def audit_continuous(name, kind):
    """对连续色板取等距的 8 个采样点做体检."""
    cmap = get_palette(name)
    samples = [tuple(cmap(t)[:3]) for t in np.linspace(0, 1, 8)]
    hexes = [rgb_to_hex(c) for c in samples]
    d_n, _ = min_pairwise_delta_e(hexes)
    d_p, _ = cvd_min_delta_e(hexes, 'protanopia')
    d_d, _ = cvd_min_delta_e(hexes, 'deuteranopia')
    d_t, _ = cvd_min_delta_e(hexes, 'tritanopia')
    # 连续色板的 ΔL 我们看采样点是否单调
    from color_lab import srgb_to_lab
    labs = [srgb_to_lab(c) for c in samples]
    Ls = np.array([lab[0] for lab in labs])
    monotonic = bool(np.all(np.diff(Ls) > 0) or np.all(np.diff(Ls) < 0))
    overall = '✓' if (d_n > 5 and monotonic) else ('!' if d_n > 3 else '✗')
    return dict(name=name, kind=kind, dE_n=d_n, dE_p=d_p, dE_d=d_d, dE_t=d_t,
                L_monotonic=monotonic, overall=overall)


def build_report():
    cat_results = [audit_categorical(n, c) for n, c in PALETTES_CAT.items()]
    seq_results = [audit_continuous(n, 'seq') for n in PALETTES_SEQ]
    div_results = [audit_continuous(n, 'div') for n in PALETTES_DIV]
    cyc_results = [audit_continuous(n, 'cyc') for n in PALETTES_CYC]

    lines = ['# 68 套预设调色板体检报告', '',
             '自动生成。所有数据基于 CIEDE2000 色差和 CIE Lab 灰度计算。', '',
             '阈值说明：',
             '- 分类色：正常 ΔE > 15，绿色盲 ΔE > 8，灰度 ΔL > 15 视为通过',
             '- 连续色：8 等距采样点 ΔE > 5 且 L 单调视为通过', '']

    def cat_section(title, results):
        lines.append(f'## {title}\n')
        lines.append('| 名称 | n | 正常 ΔE | 红盲 | 绿盲 | 蓝盲 | 灰度 ΔL | 综评 |')
        lines.append('|---|---|---|---|---|---|---|---|')
        for r in results:
            lines.append(f"| `{r['name']}` | {r['n']} | "
                         f"{r['dE_n']:.1f} {grade(r['dE_n'])} | "
                         f"{r['dE_p']:.1f} {grade(r['dE_p'], 8, 4)} | "
                         f"{r['dE_d']:.1f} {grade(r['dE_d'], 8, 4)} | "
                         f"{r['dE_t']:.1f} {grade(r['dE_t'], 8, 4)} | "
                         f"{r['gray_dL']:.1f} {grade(r['gray_dL'])} | "
                         f"**{r['overall']}** |")
        lines.append('')

    def cont_section(title, results):
        lines.append(f'## {title}\n')
        lines.append('| 名称 | 正常 ΔE | 红盲 | 绿盲 | 蓝盲 | L 单调 | 综评 |')
        lines.append('|---|---|---|---|---|---|---|')
        for r in results:
            mono = '✓' if r['L_monotonic'] else '✗'
            lines.append(f"| `{r['name']}` | {r['dE_n']:.1f} | {r['dE_p']:.1f} | "
                         f"{r['dE_d']:.1f} | {r['dE_t']:.1f} | {mono} | "
                         f"**{r['overall']}** |")
        lines.append('')

    cat_section('分类调色板（17 套）', cat_results)
    cont_section('顺序调色板（14 套）', seq_results)
    cont_section('发散调色板（7 套）', div_results)
    cont_section('周期调色板（2 套）', cyc_results)

    # 汇总
    all_results = cat_results + seq_results + div_results + cyc_results
    n_pass = sum(1 for r in all_results if r['overall'] == '✓')
    n_warn = sum(1 for r in all_results if r['overall'] == '!')
    n_fail = sum(1 for r in all_results if r['overall'] == '✗')
    lines.insert(6, f'**汇总**: {n_pass} 通过 / {n_warn} 警告 / {n_fail} 不推荐'
                    f'（总数 {len(all_results)}）\n')

    # 推荐
    lines.append('## 推荐用法\n')
    lines.append('- **投顶刊（色盲安全是硬要求）**：从下面综评 ✓ 的分类色里选')
    cb_safe = [r['name'] for r in cat_results if r['overall'] == '✓']
    if cb_safe:
        lines.append('  - 推荐: ' + ', '.join(f'`{n}`' for n in cb_safe))
    lines.append('- **黑白印刷**：选灰度 ΔL > 15 的')
    bw_safe = [r['name'] for r in cat_results if r['gray_dL'] > 15]
    if bw_safe:
        lines.append('  - 推荐: ' + ', '.join(f'`{n}`' for n in bw_safe))
    lines.append('- **避坑**：综评 ✗ 的不要用于关键科研图\n')

    return '\n'.join(lines), all_results


if __name__ == '__main__':
    report, results = build_report()
    out = Path(__file__).parent.parent.parent / 'docs' / 'palette_audit_report.md'
    out.write_text(report, encoding='utf-8')
    print(f'wrote {out}')
    # 简要 stdout 输出
    n_pass = sum(1 for r in results if r['overall'] == '✓')
    n_warn = sum(1 for r in results if r['overall'] == '!')
    n_fail = sum(1 for r in results if r['overall'] == '✗')
    print(f'总评: {n_pass} ✓ / {n_warn} ! / {n_fail} ✗')
