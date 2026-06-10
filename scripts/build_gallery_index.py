#!/usr/bin/env python3
"""从 manifest.json 重生成 gallery/index.html.

只需要 manifest.json 和 gallery/*.png 都在位即可。
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
M = json.load(open(ROOT / 'manifest.json', encoding='utf-8'))
entries = M['templates']

cat_label = {
    'basic':'基础', 'categorical':'柱状', 'distribution':'分布',
    'statistical':'统计', 'relation':'关系', 'matrix':'矩阵',
    'field':'场', 'ranking':'排名', 'time':'时间序列',
    'composite':'复合', 'flow':'流图', 'polar':'极坐标',
    '3d':'三维', 'signal':'信号', 'electrical':'电气',
    'control':'控制', 'rf':'RF/通信', 'ml':'机器学习',
    'multivar':'多变量', 'specialty':'专题',
    'cfd':'CFD', 'optimization':'优化', 'nn':'神经网络',
}

all_cats = sorted({e['category'] for e in entries})

cards = []
for e in entries:
    cards.append(f'''<div class="card" data-name="{e['name']}" data-cat="{e['category']}" data-tags="{' '.join(e['tags'])}" data-desc="{e['description']}">
  <a href="{e['name']}.png" target="_blank"><img src="{e['name']}.png" loading="lazy" alt="{e['name']}"></a>
  <div class="meta">
    <div class="name">{e['name']}</div>
    <div class="desc">{e['description']}</div>
    <div class="tags"><span class="cat">{cat_label.get(e['category'], e['category'])}</span> {' '.join(f'<span class="tag">{t}</span>' for t in e['tags'])}</div>
  </div>
</div>''')

cat_options = '\n'.join(f'<option value="{c}">{cat_label.get(c, c)}</option>' for c in all_cats)

html = f'''<!doctype html>
<html lang="zh-cn">
<head>
<meta charset="utf-8">
<title>科研绘图函数库 · 画廊 ({len(entries)})</title>
<style>
  body {{ font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
         margin: 0; background: #f6f7f9; color: #222; }}
  header {{ position: sticky; top: 0; background: white; padding: 16px 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08); z-index: 10; }}
  h1 {{ margin: 0 0 8px; font-size: 18px; }}
  .controls {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
  input, select {{ padding: 6px 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; }}
  input {{ width: 280px; }}
  .stats {{ color: #666; font-size: 13px; }}
  main {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
          gap: 16px; padding: 24px; }}
  .card {{ background: white; border-radius: 10px; overflow: hidden;
           box-shadow: 0 1px 4px rgba(0,0,0,0.08); transition: transform .15s; }}
  .card:hover {{ transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.10); }}
  .card.hide {{ display: none; }}
  .card img {{ width: 100%; height: 180px; object-fit: contain; background: #fafafa; display: block; }}
  .meta {{ padding: 10px 12px 12px; }}
  .name {{ font-family: ui-monospace, Menlo, monospace; font-size: 13px; font-weight: 600; }}
  .desc {{ font-size: 12px; color: #555; margin: 4px 0 8px; }}
  .tag, .cat {{ display: inline-block; font-size: 10px; padding: 1px 6px; border-radius: 4px;
                background: #eef1f5; color: #444; margin: 1px 2px 1px 0; }}
  .cat {{ background: #2E5077; color: white; font-weight: 600; }}
</style>
</head>
<body>
<header>
  <h1>科研绘图函数库 · 画廊 <span class="stats" id="count">({len(entries)} 个)</span></h1>
  <div class="controls">
    <input id="search" placeholder="搜索名称、描述、标签…" oninput="filter()">
    <select id="catSel" onchange="filter()">
      <option value="">全部分类</option>
      {cat_options}
    </select>
  </div>
</header>
<main id="grid">
{chr(10).join(cards)}
</main>
<script>
function filter() {{
  const q = document.getElementById('search').value.toLowerCase().trim();
  const c = document.getElementById('catSel').value;
  const cards = document.querySelectorAll('.card');
  let n = 0;
  cards.forEach(card => {{
    const text = [card.dataset.name, card.dataset.desc, card.dataset.tags].join(' ').toLowerCase();
    const okText = !q || text.includes(q);
    const okCat = !c || card.dataset.cat === c;
    if (okText && okCat) {{ card.classList.remove('hide'); n++; }}
    else {{ card.classList.add('hide'); }}
  }});
  document.getElementById('count').textContent = '(' + n + ' / {len(entries)})';
}}
</script>
</body>
</html>'''

(ROOT / 'gallery' / 'index.html').write_text(html, encoding='utf-8')
print(f'gallery/index.html written: {len(entries)} cards')
