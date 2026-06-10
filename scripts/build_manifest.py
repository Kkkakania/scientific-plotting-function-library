#!/usr/bin/env python3
"""从 _manifest_source.txt 重生成 manifest.json 和 catalog.md.

格式（每行）::

    <name>|<category>|tag1,tag2|描述
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC  = ROOT / '_manifest_source.txt'
JSON = ROOT / 'manifest.json'
CAT  = ROOT / 'catalog.md'

CAT_CN = {
    'basic': '基础', 'categorical': '分类/柱状', 'distribution': '分布',
    'statistical': '统计推断', 'relation': '关系', 'matrix': '矩阵/热力图',
    'field': '场/等高线', 'ranking': '排名/多维', 'time': '时间序列',
    'composite': '复合布局', 'flow': '流图', 'polar': '极坐标',
    '3d': '三维', 'signal': '信号处理', 'electrical': '电气专题',
    'control': '控制理论', 'rf': 'RF/通信', 'ml': '机器学习/统计',
    'multivar': '多变量', 'specialty': '特殊可视化',
    'cfd': 'CFD/流体', 'optimization': '优化算法', 'nn': '神经网络',
    'power': '电力系统', 'energy': '新能源/储能',
    'diagram': '流程图/框图',
}

ORDER = list(CAT_CN)


def main():
    entries = []
    for ln, line in enumerate(SRC.read_text(encoding='utf-8').strip().splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) != 4:
            sys.exit(f'line {ln} bad format: {line!r}')
        name, cat, tags, desc = parts
        entries.append({
            'name': name.strip(),
            'category': cat.strip(),
            'tags': [t.strip() for t in tags.split(',')],
            'description': desc.strip(),
        })

    # manifest.json
    JSON.write_text(json.dumps({
        'version': '1.7', 'count': len(entries), 'templates': entries
    }, ensure_ascii=False, indent=2), encoding='utf-8')

    # catalog.md
    grouped = {}
    for e in entries:
        grouped.setdefault(e['category'], []).append(e)

    md = [f'# 模板目录（{len(entries)} 个）\n',
          f'共 {len(entries)} 个模板，覆盖 {len(grouped)} 大类。\n',
          '每个在 `templates/python/<name>.py` 和 `templates/matlab/<name>.m` 各有一份对照实现。\n']
    for cat in ORDER:
        if cat not in grouped:
            continue
        md.append(f'\n## {CAT_CN.get(cat, cat)} ({cat})\n')
        md.append('| 名称 | 标签 | 说明 |')
        md.append('|---|---|---|')
        for e in grouped[cat]:
            md.append(f"| `{e['name']}` | {' / '.join(e['tags'])} | {e['description']} |")
    CAT.write_text('\n'.join(md), encoding='utf-8')

    print(f'wrote {len(entries)} entries into manifest.json and catalog.md')


if __name__ == '__main__':
    main()
