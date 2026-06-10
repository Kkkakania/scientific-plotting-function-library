#!/usr/bin/env python3
"""一键渲染全部 Python 模板到 gallery/ 目录.

用法:
    python render_all.py                       # 渲染全部
    python render_all.py line_basic bar_basic  # 只渲染指定模板
    python render_all.py --tag heatmap         # 按 tag 过滤
    python render_all.py --dark                # 深色主题, 输出到 gallery/dark/
"""
import sys
import json
import importlib.util
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
TPL_DIR = ROOT / 'templates' / 'python'
OUT_DIR = ROOT / 'gallery'
OUT_DIR.mkdir(exist_ok=True)


def load_manifest():
    return json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))


def load_module(name):
    spec = importlib.util.spec_from_file_location(name, TPL_DIR / f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    args = sys.argv[1:]
    dark = '--dark' in args
    if dark:
        args = [a for a in args if a != '--dark']
        # monkeypatch: 强制所有模板的 apply_theme() 走深色模式
        sys.path.insert(0, str(ROOT / '_utils' / 'python'))
        import theme
        _orig = theme.apply_theme
        theme.apply_theme = lambda *a, **k: _orig(*a, **{**k, 'dark': True})

    out_dir = (OUT_DIR / 'dark') if dark else OUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    names = [t['name'] for t in manifest['templates']]

    if args and args[0] == '--tag':
        tag = args[1]
        names = [t['name'] for t in manifest['templates'] if tag in t['tags']]
    elif args:
        names = args

    print(f'Rendering {len(names)} template(s) to {out_dir} ...')
    ok, fail = 0, []
    for name in names:
        try:
            mod = load_module(name)
            fig = mod.make_figure()
            save_kw = {'facecolor': fig.get_facecolor()} if dark else {}
            fig.savefig(out_dir / f'{name}.png', dpi=150, **save_kw)
            plt.close(fig)
            ok += 1
            print(f'  OK    {name}')
        except Exception as e:
            fail.append((name, str(e)))
            print(f'  FAIL  {name}: {e}')

    print(f'\nDone: {ok} ok, {len(fail)} failed')
    return 0 if not fail else 1


if __name__ == '__main__':
    sys.exit(main())
