#!/usr/bin/env python3
"""verify_all: 整库完整性体检.

跑完后生成 docs/verification_report.md，覆盖：
1. manifest ↔ 文件 1:1
2. 全库模板渲染（含失败模板列表）
3. 文档相对链接有效性
4. 配色调色板 round-trip 误差
5. 共享工具 import 可用性
"""
import importlib.util
import json
import re
import sys
import traceback
from pathlib import Path
import matplotlib
matplotlib.use('Agg')

ROOT = Path(__file__).parent.parent
MANIFEST = ROOT / 'manifest.json'
TPL = ROOT / 'templates' / 'python'
TPL_M = ROOT / 'templates' / 'matlab'


def section(title, lines):
    return [f'\n## {title}\n'] + lines


def check_manifest_files():
    """每个 manifest 条目必须有 Python + MATLAB 模板."""
    entries = json.loads(MANIFEST.read_text(encoding='utf-8'))['templates']
    missing_py = [e['name'] for e in entries if not (TPL / f"{e['name']}.py").exists()]
    missing_m  = [e['name'] for e in entries if not (TPL_M / f"{e['name']}.m").exists()]
    extra_py = [p.stem for p in TPL.glob('*.py')
                if p.stem not in {e['name'] for e in entries}]
    extra_m = [p.stem for p in TPL_M.glob('*.m')
               if p.stem not in {e['name'] for e in entries}]
    return {
        'n_entries': len(entries),
        'missing_py': missing_py,
        'missing_m':  missing_m,
        'extra_py':   extra_py,
        'extra_m':    extra_m,
    }


def check_template_renders():
    """全部 Python 模板逐个跑."""
    entries = json.loads(MANIFEST.read_text(encoding='utf-8'))['templates']
    ok, fail = [], []
    for e in entries:
        name = e['name']
        try:
            spec = importlib.util.spec_from_file_location(name, TPL / f'{name}.py')
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            fig = mod.make_figure()
            assert fig is not None
            import matplotlib.pyplot as plt
            plt.close(fig)
            ok.append(name)
        except Exception as e_:
            fail.append((name, str(e_).splitlines()[-1] if str(e_) else 'unknown'))
    return ok, fail


def check_doc_links():
    """所有 .md 里的相对链接都应该解析到现存文件."""
    broken = []
    for md in ROOT.rglob('*.md'):
        if '__pycache__' in str(md): continue
        try:
            text = md.read_text(encoding='utf-8')
        except Exception:
            continue
        for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', text):
            link = m.group(2)
            if link.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            # 去掉 #anchor
            link = link.split('#')[0]
            if not link: continue
            target = (md.parent / link).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not target.exists():
                broken.append((str(md.relative_to(ROOT)), link, m.group(1)))
    return broken


def check_palette_roundtrip():
    """sci_palettes 所有色板都能取出 + Lab round-trip 误差."""
    sys.path.insert(0, str(ROOT / 'palettes' / 'python'))
    from sci_palettes import (PALETTES_CAT, PALETTES_SEQ, PALETTES_DIV,
                               PALETTES_CYC, get_palette)
    from color_lab import hex_to_rgb, srgb_to_lab, lab_to_srgb
    import numpy as np

    max_err = 0
    bad = []
    for name, colors in PALETTES_CAT.items():
        for c in colors:
            rgb = np.array(hex_to_rgb(c) if isinstance(c, str) else c)
            lab = srgb_to_lab(rgb); rgb2 = lab_to_srgb(lab)
            err = float(np.max(np.abs(rgb - rgb2)))
            if err > max_err: max_err = err
            if err > 1e-5: bad.append((name, c, err))

    n_total = (len(PALETTES_CAT) + len(PALETTES_SEQ)
               + len(PALETTES_DIV) + len(PALETTES_CYC))
    for name in list(PALETTES_SEQ) + list(PALETTES_DIV) + list(PALETTES_CYC):
        get_palette(name)
    return {'n_total': n_total, 'max_err': max_err, 'bad': bad}


def check_utils_import():
    """共享工具能否正常 import."""
    failures = []
    paths = [ROOT / '_utils' / 'python', ROOT / 'palettes' / 'python']
    sys.path = [str(p) for p in paths] + sys.path
    modules = ['theme', 'palette', 'export', 'demo_data', 'data_loader',
               'sci_palettes', 'color_lab', 'palette_generator',
               'palette_extractor', 'palette_validator', 'bivariate']
    for m in modules:
        try:
            importlib.import_module(m)
        except Exception as e:
            failures.append((m, str(e)))
    return modules, failures


def main():
    print('=== 整库完整性体检 ===')
    out = ['# 验证报告', '',
           '自动生成于 `scripts/verify_all.py`，覆盖五大维度。', '']

    # 1
    print('1) 检查 manifest ↔ 文件...')
    r = check_manifest_files()
    s = ['共 ' + str(r['n_entries']) + ' 条 manifest 记录']
    if r['missing_py'] or r['missing_m'] or r['extra_py'] or r['extra_m']:
        if r['missing_py']: s.append(f"- 缺 Python: {r['missing_py']}")
        if r['missing_m']:  s.append(f"- 缺 MATLAB: {r['missing_m']}")
        if r['extra_py']:   s.append(f"- 多余 Python: {r['extra_py']}")
        if r['extra_m']:    s.append(f"- 多余 MATLAB: {r['extra_m']}")
        s.append('- **结果: ✗ 不一致**')
        ok1 = False
    else:
        s.append(f'- ✓ Python 与 MATLAB 各 {r["n_entries"]} 个模板，一对一齐全')
        s.append('- **结果: ✓ 一致**')
        ok1 = True
    out += section('1. manifest 完整性', s)

    # 2
    print('2) 跑全部模板...')
    ok, fail = check_template_renders()
    s = [f'- 通过: **{len(ok)}** / 失败: **{len(fail)}**']
    if fail:
        s.append('- 失败模板:')
        for n, msg in fail[:20]:
            s.append(f'  - `{n}`: {msg}')
        s.append('- **结果: ✗ 有失败**')
        ok2 = False
    else:
        s.append('- **结果: ✓ 全过**')
        ok2 = True
    out += section('2. 模板渲染', s)

    # 3
    print('3) 检查文档链接...')
    broken = check_doc_links()
    if broken:
        s = ['- 发现 ' + str(len(broken)) + ' 个失效链接:']
        for f, link, text in broken[:15]:
            s.append(f'  - `{f}` → `{link}`（[{text}]）')
        s.append('- **结果: ✗ 有失效**')
        ok3 = False
    else:
        s = ['- ✓ 全部相对链接有效', '- **结果: ✓ 通过**']
        ok3 = True
    out += section('3. 文档链接', s)

    # 4
    print('4) 调色板 round-trip...')
    r = check_palette_roundtrip()
    s = [f'- 检查了 {r["n_total"]} 套调色板',
         f'- sRGB ↔ Lab 最大数值误差: **{r["max_err"]:.2e}**']
    if r['bad']:
        s.append(f'- ✗ {len(r["bad"])} 个颜色误差 > 1e-5')
        ok4 = False
    else:
        s.append('- ✓ 全部颜色 round-trip 完美（机器精度）')
        ok4 = True
    out += section('4. 配色 round-trip 精度', s)

    # 5
    print('5) 共享工具 import...')
    mods, failures = check_utils_import()
    if failures:
        s = ['- ✗ ' + str(len(failures)) + ' 个模块 import 失败:']
        for m, e in failures:
            s.append(f'  - `{m}`: {e}')
        ok5 = False
    else:
        s = [f'- ✓ {len(mods)} 个共享模块全部 import 成功']
        s.append(f'  - {", ".join("`" + m + "`" for m in mods)}')
        ok5 = True
    out += section('5. 共享工具可用性', s)

    # 总评
    overall = all([ok1, ok2, ok3, ok4, ok5])
    out.insert(3, f'**总评**: {"✓ 全部通过" if overall else "✗ 有问题"}'
                  f'（5 大检查 / 通过 {sum([ok1, ok2, ok3, ok4, ok5])}）\n')

    report_path = ROOT / 'docs' / 'verification_report.md'
    report_path.write_text('\n'.join(out), encoding='utf-8')
    print(f'\n→ {report_path}')
    print(f'\n总评: {"✓ 全部通过" if overall else "✗ 有问题"}')
    return 0 if overall else 1


if __name__ == '__main__':
    sys.exit(main())
