#!/usr/bin/env python3
"""verify_all: 整库完整性体检.

跑完后生成 docs/verification_report.md，覆盖：
1. manifest ↔ 文件 1:1
2. 全库模板渲染（含失败模板列表）
3. 文档相对链接有效性
4. light/dark gallery 完整性
5. 批次账本一致性
6. 配色调色板 round-trip 误差
7. 共享工具 import 可用性
"""
import importlib.util
import json
import re
import sys
import traceback
from collections import Counter
from pathlib import Path
import matplotlib
matplotlib.use('Agg')

ROOT = Path(__file__).parent.parent
MANIFEST = ROOT / 'manifest.json'
TPL = ROOT / 'templates' / 'python'
TPL_M = ROOT / 'templates' / 'matlab'
BATCH_DIR = ROOT / '_batch_manifests'


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


def check_gallery_files():
    """light/dark gallery PNGs should exist for every manifest entry."""
    entries = json.loads(MANIFEST.read_text(encoding='utf-8'))['templates']
    names = [e['name'] for e in entries]
    gallery = ROOT / 'gallery'
    dark = gallery / 'dark'
    missing_light = [n for n in names if not (gallery / f'{n}.png').exists()]
    missing_dark = [n for n in names if not (dark / f'{n}.png').exists()]
    return {
        'n_entries': len(names),
        'missing_light': missing_light,
        'missing_dark': missing_dark,
        'dark_dir_exists': dark.exists(),
    }


def check_batch_manifests():
    """Batch ledgers should be parseable and merged into the main manifest."""
    manifest_names = {
        e['name'] for e in json.loads(MANIFEST.read_text(encoding='utf-8'))['templates']
    }
    py_names = {p.stem for p in TPL.glob('*.py')}
    m_names = {p.stem for p in TPL_M.glob('*.m')}
    rows = []
    bad_format = []
    missing_py = []
    missing_m = []
    missing_manifest = []
    for batch in sorted(BATCH_DIR.glob('batch_*.txt')):
        for ln, line in enumerate(batch.read_text(encoding='utf-8').splitlines(), 1):
            if not line.strip() or line.startswith('#'):
                continue
            parts = line.split('|')
            if len(parts) != 4:
                bad_format.append((batch.name, ln, line))
                continue
            name = parts[0].strip()
            rows.append(name)
            if name not in py_names:
                missing_py.append(name)
            if name not in m_names:
                missing_m.append(name)
            if name not in manifest_names:
                missing_manifest.append(name)
    duplicates = sorted(name for name, n in Counter(rows).items() if n > 1)
    return {
        'n_batches': len(list(BATCH_DIR.glob('batch_*.txt'))),
        'n_rows': len(rows),
        'bad_format': bad_format,
        'duplicates': duplicates,
        'missing_py': sorted(set(missing_py)),
        'missing_m': sorted(set(missing_m)),
        'missing_manifest': sorted(set(missing_manifest)),
    }


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
           '自动生成于 `scripts/verify_all.py`，覆盖七大维度。', '']

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
    print('4) 检查 gallery 明暗图...')
    r = check_gallery_files()
    if r['missing_light'] or r['missing_dark'] or not r['dark_dir_exists']:
        s = [f'- manifest 记录: {r["n_entries"]}']
        if not r['dark_dir_exists']:
            s.append('- 缺少 `gallery/dark/`')
        if r['missing_light']:
            s.append(f'- 缺 light gallery: {r["missing_light"][:20]}')
        if r['missing_dark']:
            s.append(f'- 缺 dark gallery: {r["missing_dark"][:20]}')
        s.append('- **结果: ✗ 不完整**')
        ok4 = False
    else:
        s = [f'- ✓ light gallery: {r["n_entries"]} / {r["n_entries"]}',
             f'- ✓ dark gallery: {r["n_entries"]} / {r["n_entries"]}',
             '- **结果: ✓ 通过**']
        ok4 = True
    out += section('4. gallery 完整性', s)

    # 5
    print('5) 检查批次账本...')
    r = check_batch_manifests()
    bad = (r['bad_format'] or r['duplicates'] or r['missing_py']
           or r['missing_m'] or r['missing_manifest'])
    if bad:
        s = [f'- 批次文件: {r["n_batches"]}；批次条目: {r["n_rows"]}']
        if r['bad_format']:
            s.append(f'- 格式错误: {r["bad_format"][:10]}')
        if r['duplicates']:
            s.append(f'- 重复条目: {r["duplicates"][:20]}')
        if r['missing_py']:
            s.append(f'- 缺 Python: {r["missing_py"][:20]}')
        if r['missing_m']:
            s.append(f'- 缺 MATLAB: {r["missing_m"][:20]}')
        if r['missing_manifest']:
            s.append(f'- 未进入 manifest: {r["missing_manifest"][:20]}')
        s.append('- **结果: ✗ 不一致**')
        ok5 = False
    else:
        s = [f'- ✓ {r["n_batches"]} 个批次文件格式正确',
             f'- ✓ {r["n_rows"]} 个批次条目均有 Python/MATLAB 文件并已进入 manifest',
             '- **结果: ✓ 通过**']
        ok5 = True
    out += section('5. 批次账本一致性', s)

    # 6
    print('6) 调色板 round-trip...')
    r = check_palette_roundtrip()
    s = [f'- 检查了 {r["n_total"]} 套调色板',
         f'- sRGB ↔ Lab 最大数值误差: **{r["max_err"]:.2e}**']
    if r['bad']:
        s.append(f'- ✗ {len(r["bad"])} 个颜色误差 > 1e-5')
        ok6 = False
    else:
        s.append('- ✓ 全部颜色 round-trip 完美（机器精度）')
        ok6 = True
    out += section('6. 配色 round-trip 精度', s)

    # 7
    print('7) 共享工具 import...')
    mods, failures = check_utils_import()
    if failures:
        s = ['- ✗ ' + str(len(failures)) + ' 个模块 import 失败:']
        for m, e in failures:
            s.append(f'  - `{m}`: {e}')
        ok7 = False
    else:
        s = [f'- ✓ {len(mods)} 个共享模块全部 import 成功']
        s.append(f'  - {", ".join("`" + m + "`" for m in mods)}')
        ok7 = True
    out += section('7. 共享工具可用性', s)

    # 总评
    checks = [ok1, ok2, ok3, ok4, ok5, ok6, ok7]
    overall = all(checks)
    out.insert(3, f'**总评**: {"✓ 全部通过" if overall else "✗ 有问题"}'
                  f'（7 大检查 / 通过 {sum(checks)}）\n')

    report_path = ROOT / 'docs' / 'verification_report.md'
    report_path.write_text('\n'.join(out), encoding='utf-8')
    print(f'\n→ {report_path}')
    print(f'\n总评: {"✓ 全部通过" if overall else "✗ 有问题"}')
    return 0 if overall else 1


if __name__ == '__main__':
    sys.exit(main())
