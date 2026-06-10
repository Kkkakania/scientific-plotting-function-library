#!/usr/bin/env python3
"""从 sci_palettes.py 生成 palettes/palette_picker.html 交互式选择器.

功能：搜索 / 按类别筛 / 点色块复制 hex / 一键复制四语调用代码
（Python · MATLAB · Go · Origin）。数据直接读 Python 源，永不漂移。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / 'palettes' / 'python'))
from sci_palettes import (PALETTES_CAT, PALETTES_SEQ,        # noqa: E402
                          PALETTES_DIV, PALETTES_CYC)


def to_hex(c):
    if isinstance(c, str):
        return c.upper()
    return '#%02X%02X%02X' % tuple(int(round(v*255)) for v in c)


data = []
for kind, d in (('categorical', PALETTES_CAT), ('sequential', PALETTES_SEQ),
                ('diverging', PALETTES_DIV), ('cyclic', PALETTES_CYC)):
    for name, colors in d.items():
        data.append({'name': name, 'kind': kind,
                     'colors': [to_hex(c) for c in colors]})

payload = json.dumps(data, ensure_ascii=False)

html = '''<!doctype html>
<html lang="zh-cn">
<head>
<meta charset="utf-8">
<title>科研配色选择器</title>
<style>
  body { font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
         margin: 0; background: #f6f7f9; color: #222; }
  header { position: sticky; top: 0; background: white; padding: 14px 24px;
           box-shadow: 0 1px 3px rgba(0,0,0,0.08); z-index: 10;
           display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }
  h1 { margin: 0; font-size: 17px; }
  input, select { padding: 6px 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; }
  main { padding: 20px 24px; display: grid; gap: 14px;
         grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); }
  .pal { background: white; border-radius: 10px; padding: 12px 14px;
         box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .pal.hide { display: none; }
  .pname { font-family: ui-monospace, Menlo, monospace; font-weight: 600; font-size: 14px; }
  .kind { font-size: 10px; padding: 1px 7px; border-radius: 4px; color: white; margin-left: 6px;
          vertical-align: 2px; }
  .k-categorical { background: #2E5077; } .k-sequential { background: #2E7D32; }
  .k-diverging { background: #C45508; } .k-cyclic { background: #6B3A78; }
  .swatches { display: flex; height: 44px; margin: 10px 0 8px; border-radius: 6px;
              overflow: hidden; cursor: pointer; }
  .sw { flex: 1; transition: flex .12s; position: relative; }
  .sw:hover { flex: 2.2; }
  .sw:hover::after { content: attr(data-hex); position: absolute; left: 50%; top: 50%;
                     transform: translate(-50%,-50%); font-size: 9px; color: white;
                     text-shadow: 0 0 3px rgba(0,0,0,0.9); font-family: monospace; }
  .grad { height: 44px; margin: 10px 0 8px; border-radius: 6px; }
  .btns { display: flex; gap: 6px; flex-wrap: wrap; }
  button { padding: 4px 10px; font-size: 11px; border: 1px solid #ddd; background: #fafafa;
           border-radius: 5px; cursor: pointer; }
  button:hover { background: #eef1f5; }
  #toast { position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%);
           background: #222; color: white; padding: 8px 18px; border-radius: 20px;
           font-size: 13px; opacity: 0; transition: opacity .25s; pointer-events: none; }
</style>
</head>
<body>
<header>
  <h1>科研配色选择器 <span id="count" style="color:#888;font-size:13px"></span></h1>
  <input id="q" placeholder="搜索名称…" oninput="render()">
  <select id="k" onchange="render()">
    <option value="">全部类型</option>
    <option value="categorical">分类</option>
    <option value="sequential">顺序</option>
    <option value="diverging">发散</option>
    <option value="cyclic">周期</option>
  </select>
  <span style="color:#888;font-size:12px">点色块复制 hex · 按钮复制各语言调用代码</span>
</header>
<main id="grid"></main>
<div id="toast"></div>
<script>
const PALS = __DATA__;
function copy(text, msg) {
  navigator.clipboard.writeText(text).then(() => {
    const t = document.getElementById('toast');
    t.textContent = msg; t.style.opacity = 1;
    setTimeout(() => t.style.opacity = 0, 1400);
  });
}
function code(p, lang) {
  if (lang === 'py')     return "from sci_palettes import get_palette\\ncolors = get_palette('" + p.name + "')";
  if (lang === 'm')      return "colors = sci_palettes('" + p.name + "');";
  if (lang === 'go')     return 'pal, _ := sciplot.Get("' + p.name + '")';
  if (lang === 'origin') return "# originpro：参照 templates/origin/python/18_apply_v15_palette.py\\nV = " + JSON.stringify(p.colors);
  if (lang === 'hex')    return p.colors.join(', ');
}
function render() {
  const q = document.getElementById('q').value.toLowerCase().trim();
  const k = document.getElementById('k').value;
  const grid = document.getElementById('grid');
  grid.innerHTML = '';
  let n = 0;
  PALS.forEach(p => {
    if (q && !p.name.includes(q)) return;
    if (k && p.kind !== k) return;
    n++;
    const div = document.createElement('div');
    div.className = 'pal';
    let body;
    if (p.kind === 'categorical') {
      body = '<div class="swatches">' + p.colors.map(c =>
        '<div class="sw" style="background:' + c + '" data-hex="' + c +
        '" onclick="copy(\\'' + c + '\\', \\'已复制 ' + c + '\\')"></div>').join('') + '</div>';
    } else {
      body = '<div class="grad" style="background:linear-gradient(90deg,' + p.colors.join(',') + ')"></div>';
    }
    div.innerHTML = '<span class="pname">' + p.name + '</span>' +
      '<span class="kind k-' + p.kind + '">' + p.kind + '</span>' + body +
      '<div class="btns">' +
      ['py:Python', 'm:MATLAB', 'go:Go', 'origin:Origin', 'hex:HEX'].map(s => {
        const [l, label] = s.split(':');
        return '<button onclick=\\'copy(code(' + JSON.stringify(p) + ', "' + l +
               '"), "已复制 ' + label + ' 代码")\\'>' + label + '</button>';
      }).join('') + '</div>';
    grid.appendChild(div);
  });
  document.getElementById('count').textContent = '(' + n + ' / ' + PALS.length + ' 套)';
}
render();
</script>
</body>
</html>'''

html = html.replace('__DATA__', payload)
out = ROOT / 'palettes' / 'palette_picker.html'
out.write_text(html, encoding='utf-8')
print(f'palette_picker.html written: {len(data)} palettes')
