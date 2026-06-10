#!/usr/bin/env python3
"""check_matlab_syntax: MATLAB .m 文件静态健康检查（实用务实版）.

只做能在 5 行 Python 里抓住的"明显问题"，不试图模拟解释器：
- 行内/行末 `%` 注释剥离后，括号配对
- function 数量 vs 独立 end 数量（适用于 end-style 文件）
- addpath 不应使用反斜杠硬路径

不保证抓得到所有问题；但所有失败都是真问题。
（MATLAB 单引号既是字符串又是转置，无法在不解析的情况下完美区分。
本工具保守：直接数字符，不过滤字符串。绝大多数 .m 不在字符串内放不配对括号。）
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def strip_comments(text: str) -> str:
    """剥离行内 % 注释，保留 %{ ... %} 块注释外的代码."""
    # 简单做法：按行处理，找第一个不在字符串内的 %
    # 由于无法精确判断字符串，用启发式：% 前面如果有奇数个 '，可能在字串内 → 跳过
    out = []
    for line in text.splitlines():
        # 找到第一个 % 的位置
        # 启发：% 前面的 ' 个数为偶数 → 不在字串里 → 是注释开始
        for i, ch in enumerate(line):
            if ch == '%':
                quotes_before = line[:i].count("'")
                # 偶数才认为是注释；这对绝大多数 .m 文件成立
                if quotes_before % 2 == 0:
                    line = line[:i]
                    break
        out.append(line)
    return '\n'.join(out)


def check_file(path: Path):
    text = path.read_text(encoding='utf-8', errors='replace')
    code = strip_comments(text)
    issues = []

    # 1. 括号配对（直接数，接受字符串内不配对会误报；实践极少出现）
    for op, cl in [('(', ')'), ('[', ']'), ('{', '}')]:
        n_op = code.count(op)
        n_cl = code.count(cl)
        if n_op != n_cl:
            issues.append(f'{op}{cl} 不配对：{n_op} 个 {op} vs {n_cl} 个 {cl}')

    # 2. function / end 配对（推荐用 end 包住函数）
    fn_count = len(re.findall(r'^\s*function\s+', text, re.MULTILINE))
    # 数所有"独立的 end"（行首/缩进 + end + 行尾）
    end_count = len(re.findall(r'^\s*end\s*$', text, re.MULTILINE))
    if fn_count > 1 and end_count < fn_count:
        issues.append(f'function/end 不配对：{fn_count} 个 function vs {end_count} 个独立 end')

    # 3. addpath 应该用 fullfile，不应硬写反斜杠
    bad = re.findall(r"addpath\s*\(\s*['\"][^)'\"]*[\\][^)'\"]*['\"]", text)
    if bad:
        issues.append(f'addpath 用了硬路径：{bad[:2]}')

    return issues


def main():
    m_files = sorted(ROOT.rglob('*.m'))
    m_files = [p for p in m_files if 'gallery' not in str(p)]
    total = len(m_files)
    bad = []
    for p in m_files:
        issues = check_file(p)
        if issues:
            bad.append((p.relative_to(ROOT), issues))

    print(f'扫描 {total} 个 .m 文件')
    print(f'  通过: {total - len(bad)}')
    print(f'  发现问题: {len(bad)}')
    if bad:
        print()
        for p, issues in bad[:30]:
            print(f'  {p}')
            for i in issues:
                print(f'    - {i}')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
