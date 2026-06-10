#!/usr/bin/env python3
"""palette_cli: 命令行调色板工具.

用法
----
    # 列出所有预设
    python palette_cli.py list

    # 取一套预设
    python palette_cli.py get wong

    # 生成自定义分类色（OKLab）
    python palette_cli.py gen qualitative --n 8 --L 0.6 --C 0.15

    # 生成自定义顺序色
    python palette_cli.py gen sequential --n 256 --hue 220

    # 体检一套配色
    python palette_cli.py audit wong

    # 体检自定义颜色
    python palette_cli.py audit "#0072B2,#D55E00,#009E73"

    # 导出
    python palette_cli.py get wong --format css > my.css
    python palette_cli.py get wong --format latex --output colors.tex

    # 从图片榨色
    python palette_cli.py extract logo.png --n 6 --format json

    # 转白点（屏幕→印刷）
    python palette_cli.py adapt "#0072B2" --to D50
"""
import argparse
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def cmd_list(args):
    from sci_palettes import list_palettes
    d = list_palettes()
    for kind, names in d.items():
        print(f'\n[{kind}] ({len(names)})')
        for i, n in enumerate(names):
            print(f'  {n}', end='\n' if (i+1) % 4 == 0 else '  ')
        if len(names) % 4 != 0:
            print()


def cmd_get(args):
    from sci_palettes import get_palette
    from color_lab import rgb_to_hex
    pal = get_palette(args.name)
    if isinstance(pal, list):
        colors = pal
    else:
        import numpy as np
        # colormap → 采样 N 点
        n = args.n_samples or 10
        colors = [rgb_to_hex(pal(t)[:3]) for t in np.linspace(0, 1, n)]
    _output(colors, args)


def cmd_gen(args):
    if args.kind == 'qualitative':
        if args.model == 'oklab':
            from palette_generator import oklch_qualitative
            colors = oklch_qualitative(n=args.n, L=args.L, C=args.C)
        else:
            from palette_generator import hcl_qualitative
            colors = hcl_qualitative(n=args.n, L=args.L*100 if args.L < 1 else args.L,
                                      C=args.C*100 if args.C < 1 else args.C)
    elif args.kind == 'sequential':
        from palette_generator import oklch_sequential, hcl_sequential
        from color_lab import rgb_to_hex
        if args.model == 'oklab':
            arr = oklch_sequential(n=args.n, hue=args.hue)
        else:
            arr = hcl_sequential(n=args.n, hue=args.hue)
        colors = [rgb_to_hex(c) for c in arr]
    elif args.kind == 'diverging':
        from palette_generator import oklch_diverging, hcl_diverging
        from color_lab import rgb_to_hex
        if args.model == 'oklab':
            arr = oklch_diverging(n=args.n, hue_neg=args.hue_neg, hue_pos=args.hue_pos)
        else:
            arr = hcl_diverging(n=args.n, hue_neg=args.hue_neg, hue_pos=args.hue_pos)
        colors = [rgb_to_hex(c) for c in arr]
    else:
        sys.exit(f'未知 kind: {args.kind}')
    _output(colors, args)


def cmd_audit(args):
    from palette_validator import validate_report
    if args.name in _list_presets():
        from sci_palettes import get_palette
        pal = get_palette(args.name)
        colors = pal if isinstance(pal, list) else None
        if colors is None:
            sys.exit(f'{args.name} 是连续色板，不适合分类体检')
    else:
        colors = [c.strip() for c in args.name.split(',')]
    print(validate_report(colors))


def cmd_extract(args):
    from palette_extractor import extract_from_image
    colors = extract_from_image(args.path, n=args.n,
                                 sort=args.sort or 'L')
    _output(colors, args)


def cmd_adapt(args):
    from color_lab import hex_to_rgb, rgb_to_hex
    from white_point import adapt_rgb_for_print
    import numpy as np
    rgb = np.array(hex_to_rgb(args.color))
    out = adapt_rgb_for_print(rgb)
    print(rgb_to_hex(out))


def _list_presets():
    from sci_palettes import (PALETTES_CAT, PALETTES_SEQ,
                               PALETTES_DIV, PALETTES_CYC)
    return set(PALETTES_CAT) | set(PALETTES_SEQ) | set(PALETTES_DIV) | set(PALETTES_CYC)


def _output(colors, args):
    if args.format == 'hex':
        text = '\n'.join(colors)
    else:
        from palette_export import export_palette
        text = export_palette(colors, args.format, name=args.varname or 'palette')

    if args.output:
        if isinstance(text, bytes):
            open(args.output, 'wb').write(text)
        else:
            open(args.output, 'w', encoding='utf-8').write(text)
        print(f'→ {args.output}', file=sys.stderr)
    else:
        if isinstance(text, bytes):
            sys.stdout.buffer.write(text)
        else:
            print(text)


def main():
    p = argparse.ArgumentParser(prog='palette-cli',
                                description='科研配色 CLI')
    sub = p.add_subparsers(dest='cmd', required=True)

    def add_output_args(sp):
        sp.add_argument('--format', default='hex',
                        choices=['hex', 'css', 'scss', 'json', 'latex',
                                  'tex', 'tikz', 'matlab', 'm',
                                  'python', 'py', 'gimp', 'gpl', 'ase'])
        sp.add_argument('--output', '-o', help='保存到文件')
        sp.add_argument('--varname', help='变量名（导出时用）')

    sp = sub.add_parser('list',   help='列出所有预设调色板')
    sp.set_defaults(func=cmd_list)

    sp = sub.add_parser('get',    help='取一套预设')
    sp.add_argument('name')
    sp.add_argument('--n-samples', type=int, help='连续色板时采样多少点')
    add_output_args(sp); sp.set_defaults(func=cmd_get)

    sp = sub.add_parser('gen',    help='程序化生成')
    sp.add_argument('kind', choices=['qualitative', 'sequential', 'diverging'])
    sp.add_argument('--model', default='oklab', choices=['oklab', 'cielab'])
    sp.add_argument('--n', type=int, default=8)
    sp.add_argument('--L', type=float, default=0.65)
    sp.add_argument('--C', type=float, default=0.15)
    sp.add_argument('--hue', type=float, default=240)
    sp.add_argument('--hue-neg', type=float, default=240)
    sp.add_argument('--hue-pos', type=float, default=30)
    add_output_args(sp); sp.set_defaults(func=cmd_gen)

    sp = sub.add_parser('audit',  help='调色板自动体检')
    sp.add_argument('name', help='预设名 或 逗号分隔的 hex')
    sp.set_defaults(func=cmd_audit)

    sp = sub.add_parser('extract', help='从图片榨色')
    sp.add_argument('path')
    sp.add_argument('--n', type=int, default=6)
    sp.add_argument('--sort', choices=['L', 'h', 'dominant', 'none'])
    add_output_args(sp); sp.set_defaults(func=cmd_extract)

    sp = sub.add_parser('adapt',  help='白点适应（屏幕 → 印刷）')
    sp.add_argument('color', help='HEX 颜色')
    sp.add_argument('--to', default='D50',
                    choices=['D50', 'D55', 'D65', 'D75'])
    sp.set_defaults(func=cmd_adapt)

    args = p.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
