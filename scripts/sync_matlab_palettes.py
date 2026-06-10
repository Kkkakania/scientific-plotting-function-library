"""sync_matlab_palettes: 从 palettes/python/sci_palettes.py 自动生成 MATLAB 镜像.

单一数据源（Python 字典）→ 生成
  palettes/matlab/sci_palettes.m
  palettes/matlab/sci_palettes_list.m

以后新增色板只改 Python 端，跑一次本脚本即可同步，不会再出现双语漂移。

用法::

    python scripts/sync_matlab_palettes.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'palettes', 'python'))

from sci_palettes import (PALETTES_CAT, PALETTES_SEQ,            # noqa: E402
                          PALETTES_DIV, PALETTES_CYC)


def _stops_matrix(stops):
    """[(r,g,b), ...] → MATLAB 矩阵字面量（自动换行）."""
    rows = ['%g %g %g' % tuple(s) for s in stops]
    if len(rows) <= 3:
        return '[' + '; '.join(rows) + ']'
    body = '; ...\n                                 '.join('; '.join(rows[i:i+2])
            for i in range(0, len(rows), 2))
    return '[' + body + ']'


def _hex_cells(colors):
    return '{' + ','.join("'%s'" % c for c in colors) + '}'


def build():
    lines = []
    total = (len(PALETTES_CAT) + len(PALETTES_SEQ)
             + len(PALETTES_DIV) + len(PALETTES_CYC))
    lines.append('function out = sci_palettes(name, n)')
    lines.append('%%SCI_PALETTES  科研配色库（%d 套，自动生成勿手改）' % total)
    lines.append("%   colors  = sci_palettes('wong')              % 分类色，N×3")
    lines.append("%   cmap    = sci_palettes('blues', 256)        % 顺序/发散/周期色，n×3")
    lines.append("%   sci_palettes_list()                         % 列出所有名字")
    lines.append('%')
    lines.append('% 本文件由 scripts/sync_matlab_palettes.py 从 Python 源生成。')
    lines.append('    if nargin < 2, n = 256; end')
    lines.append('')
    lines.append('    switch lower(name)')
    lines.append('        % ---------- 分类 ----------')
    for k, v in PALETTES_CAT.items():
        lines.append("        case '%s'" % k)
        lines.append('            out = h2r(%s);' % _hex_cells(v))
    for header, d in (('顺序', PALETTES_SEQ), ('发散', PALETTES_DIV),
                      ('周期', PALETTES_CYC)):
        lines.append('')
        lines.append('        %% ---------- %s ----------' % header)
        for k, v in d.items():
            lines.append("        case '%s'" % k)
            lines.append('            out = stops_to_cmap(%s, n);' % _stops_matrix(v))
    lines.append('')
    lines.append('        otherwise')
    lines.append("            error('unknown palette: %s', name);")
    lines.append('    end')
    lines.append('end')
    lines.append('')
    lines.append('% -------- helpers --------')
    lines.append('function rgb = h2r(hex_cells)')
    lines.append('    rgb = zeros(numel(hex_cells), 3);')
    lines.append('    for i = 1:numel(hex_cells)')
    lines.append('        h = hex_cells{i};')
    lines.append("        if h(1) == '#', h = h(2:end); end")
    lines.append('        rgb(i, :) = [hex2dec(h(1:2)) hex2dec(h(3:4)) hex2dec(h(5:6))] / 255;')
    lines.append('    end')
    lines.append('end')
    lines.append('')
    lines.append('function cmap = stops_to_cmap(stops, n)')
    lines.append('    t = linspace(0, 1, size(stops, 1));')
    lines.append('    ti = linspace(0, 1, n);')
    lines.append("    cmap = [interp1(t, stops(:,1), ti)' interp1(t, stops(:,2), ti)' interp1(t, stops(:,3), ti)'];")
    lines.append('end')

    list_lines = ['function out = sci_palettes_list()',
                  '%%SCI_PALETTES_LIST  所有调色板名称（自动生成勿手改）']
    for field, d in (('categorical', PALETTES_CAT), ('sequential', PALETTES_SEQ),
                     ('diverging', PALETTES_DIV), ('cyclic', PALETTES_CYC)):
        names = ', ...\n                       '.join(
            ','.join("'%s'" % k for k in list(d)[i:i+4])
            for i in range(0, len(d), 4))
        list_lines.append('    out.%s = {%s};' % (field.ljust(11), names))
    list_lines.append('end')

    mdir = os.path.join(ROOT, 'palettes', 'matlab')
    with open(os.path.join(mdir, 'sci_palettes.m'), 'w') as f:
        f.write('\n'.join(lines) + '\n')
    with open(os.path.join(mdir, 'sci_palettes_list.m'), 'w') as f:
        f.write('\n'.join(list_lines) + '\n')
    print('synced %d palettes -> palettes/matlab/' % total)


if __name__ == '__main__':
    build()
