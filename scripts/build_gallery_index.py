#!/usr/bin/env python3
"""从 manifest.json 重生成 gallery/index.html（v2：搜索 + 分类 + 语言筛选）.

语言徽章数据来源：
- python / matlab : 双语模板，全部都有
- origin          : templates/origin/origin_map.json 里有映射的
- go              : templates/go/cmd/<name>/ 存在的
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
M = json.load(open(ROOT / 'manifest.json', encoding='utf-8'))
entries = M['templates']

# ---- 语言可用性 ----
origin_map_file = ROOT / 'templates' / 'origin' / 'origin_map.json'
origin_names = set()
if origin_map_file.exists():
    omap = json.load(open(origin_map_file, encoding='utf-8'))
    origin_names = {v for k, v in omap.items() if not k.startswith('_')}
go_dir = ROOT / 'templates' / 'go' / 'cmd'
go_names = {p.name for p in go_dir.iterdir() if p.is_dir()} if go_dir.exists() else set()
plotly_dir = ROOT / 'templates' / 'plotly'
plotly_names = ({p.stem for p in plotly_dir.glob('*.py')}
                if plotly_dir.exists() else set())


def langs_of(name):
    out = ['py', 'm']
    if name in origin_names:
        out.append('origin')
    if name in go_names:
        out.append('go')
    if name in plotly_names:
        out.append('plotly')
    return out


cat_label = {
    'basic': '基础', 'categorical': '柱状', 'distribution': '分布',
    'statistical': '统计', 'relation': '关系', 'matrix': '矩阵',
    'field': '场', 'ranking': '排名', 'time': '时间序列',
    'composite': '复合', 'flow': '流图', 'polar': '极坐标',
    '3d': '三维', 'signal': '信号', 'electrical': '电气',
    'control': '控制', 'rf': 'RF/通信', 'ml': '机器学习',
    'multivar': '多变量', 'specialty': '专题',
    'cfd': 'CFD', 'optimization': '优化', 'nn': '神经网络',
    'power': '电力系统', 'energy': '新能源', 'diagram': '流程/框图',
}
lang_label = {'py': 'Python', 'm': 'MATLAB', 'origin': 'Origin', 'go': 'Go', 'plotly': 'Plotly'}

all_cats = sorted({e['category'] for e in entries})

cards = []
for e in entries:
    langs = langs_of(e['name'])
    badge = ' '.join(f'<span class="lang lang-{l}">{lang_label[l]}</span>' for l in langs)
    cards.append(f'''<div class="card" data-name="{e['name']}" data-cat="{e['category']}" data-langs="{' '.join(langs)}" data-tags="{' '.join(e['tags'])}" data-desc="{e['description']}">
  <a href="{e['name']}.png" target="_blank"><img src="{e['name']}.png" loading="lazy" alt="{e['name']}"></a>
  <div class="meta">
    <div class="name">{e['name']} {badge}</div>
    <div class="desc">{e['description']}</div>
    <div class="tags"><span class="cat">{cat_label.get(e['category'], e['category'])}</span> {' '.join(f'<span class="tag">{t}</span>' for t in e['tags'])}</div>
  </div>
</div>''')

cat_options = '\n'.join(f'<option value="{c}">{cat_label.get(c, c)}</option>'
                        for c in all_cats)

n_o, n_g, n_p = len(origin_names), len(go_names), len(plotly_names)
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
  input {{ width: 260px; }}
  .stats {{ color: #666; font-size: 13px; }}
  .langbtn {{ padding: 5px 12px; border: 1px solid #ccc; border-radius: 16px;
              background: white; font-size: 13px; cursor: pointer; user-select: none; }}
  .langbtn.on {{ color: white; border-color: transparent; }}
  #b-py.on {{ background: #2E5077; }} #b-m.on {{ background: #C45508; }}
  #b-origin.on {{ background: #2E7D32; }} #b-go.on {{ background: #00838F; }}
  #b-plotly.on {{ background: #7B3FA0; }}
  #darkbtn {{ margin-left: auto; }}
  body.dark {{ background: #15171C; color: #D8D6D3; }}
  body.dark header {{ background: #1E2128; box-shadow: 0 1px 3px rgba(0,0,0,0.5); }}
  body.dark .card {{ background: #1E2128; }}
  body.dark .card img {{ background: #15171C; }}
  body.dark .desc {{ color: #9aa0a8; }}
  body.dark .tag {{ background: #2A2E37; color: #c8ccd2; }}
  body.dark input, body.dark select, body.dark .langbtn {{ background: #2A2E37; color: #D8D6D3; border-color: #444; }}
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
  .lang {{ display: inline-block; font-size: 9px; padding: 1px 5px; border-radius: 3px;
           color: white; vertical-align: 2px; margin-left: 2px; }}
  .lang-py {{ background: #2E5077; }} .lang-m {{ background: #C45508; }}
  .lang-origin {{ background: #2E7D32; }} .lang-go {{ background: #00838F; }} .lang-plotly {{ background: #7B3FA0; }}
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
    <span class="stats">语言:</span>
    <span class="langbtn" id="b-py" onclick="toggle('py')">Python {len(entries)}</span>
    <span class="langbtn" id="b-m" onclick="toggle('m')">MATLAB {len(entries)}</span>
    <span class="langbtn" id="b-origin" onclick="toggle('origin')">Origin {n_o}</span>
    <span class="langbtn" id="b-go" onclick="toggle('go')">Go {n_g}</span>
    <span class="langbtn" id="b-plotly" onclick="toggle('plotly')">Plotly {n_p}</span>
    <span class="langbtn" id="darkbtn" onclick="toggleDark()">🌙 暗色预览</span>
  </div>
</header>
<main id="grid">
{chr(10).join(cards)}
</main>
<script>
const active = new Set();
let darkMode = false;
function toggleDark() {{
  darkMode = !darkMode;
  document.body.classList.toggle('dark', darkMode);
  document.getElementById('darkbtn').textContent = darkMode ? '☀️ 亮色预览' : '🌙 暗色预览';
  document.querySelectorAll('.card img').forEach(img => {{
    const name = img.alt;
    img.src = (darkMode ? 'dark/' : '') + name + '.png';
  }});
}}
function toggle(l) {{
  if (active.has(l)) {{ active.delete(l); }} else {{ active.add(l); }}
  document.getElementById('b-' + l).classList.toggle('on', active.has(l));
  filter();
}}
function filter() {{
  const q = document.getElementById('search').value.toLowerCase().trim();
  const c = document.getElementById('catSel').value;
  const cards = document.querySelectorAll('.card');
  let n = 0;
  cards.forEach(card => {{
    const text = [card.dataset.name, card.dataset.desc, card.dataset.tags].join(' ').toLowerCase();
    const langs = card.dataset.langs.split(' ');
    const okText = !q || text.includes(q);
    const okCat = !c || card.dataset.cat === c;
    const okLang = active.size === 0 || [...active].every(l => langs.includes(l));
    if (okText && okCat && okLang) {{ card.classList.remove('hide'); n++; }}
    else {{ card.classList.add('hide'); }}
  }});
  document.getElementById('count').textContent = '(' + n + ' / {len(entries)})';
}}
</script>
</body>
</html>'''

(ROOT / 'gallery' / 'index.html').write_text(html, encoding='utf-8')
print(f'gallery/index.html written: {len(entries)} cards, '
      f'origin={n_o}, go={n_g}, plotly={n_p}')
