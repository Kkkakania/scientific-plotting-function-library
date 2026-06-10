"""所有 Python 模板的自动渲染测试.

跑法::

    python -m pytest tests/                  # 全跑
    python -m pytest tests/ -k bode          # 只跑名字含 bode 的
    python -m pytest tests/ --collect-only   # 只列出，不跑
"""
import importlib.util
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pytest

ROOT = Path(__file__).parent.parent
TPL_DIR = ROOT / 'templates' / 'python'
MANIFEST = ROOT / 'manifest.json'


def _load_template(name):
    spec = importlib.util.spec_from_file_location(name, TPL_DIR / f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _all_names():
    if MANIFEST.exists():
        return [t['name'] for t in json.loads(MANIFEST.read_text())['templates']]
    return [p.stem for p in TPL_DIR.glob('*.py')]


@pytest.fixture(autouse=True)
def _close_figs():
    yield
    plt.close('all')


@pytest.mark.parametrize('name', _all_names())
def test_template_runs(name):
    """每个模板都应该能用合成数据跑通."""
    mod = _load_template(name)
    assert hasattr(mod, 'make_figure'), f'{name} 没有 make_figure'
    fig = mod.make_figure()
    assert fig is not None
    assert hasattr(fig, 'savefig'), f'{name} 没返回 Figure'


def test_manifest_consistency():
    """manifest 里登记的每个模板都要有对应文件."""
    assert MANIFEST.exists(), 'manifest.json 缺失'
    entries = json.loads(MANIFEST.read_text())['templates']
    for e in entries:
        py_path = TPL_DIR / f"{e['name']}.py"
        m_path  = ROOT / 'templates' / 'matlab' / f"{e['name']}.m"
        assert py_path.exists(), f"缺失 Python 模板: {e['name']}"
        assert m_path.exists(),  f"缺失 MATLAB 模板: {e['name']}"


def test_manifest_required_fields():
    """每条 manifest 都要有 name/category/tags/description."""
    entries = json.loads(MANIFEST.read_text())['templates']
    for e in entries:
        for k in ('name', 'category', 'tags', 'description'):
            assert k in e, f"{e.get('name')} 缺字段 {k}"
        assert isinstance(e['tags'], list)
        assert e['name'] == e['name'].lower(), f'{e["name"]} 应该全小写'
