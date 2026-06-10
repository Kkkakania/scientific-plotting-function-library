"""render_all_origin: 在装有 Origin 的 Windows 机器上一键跑全部脚本并导出 PNG.

为什么需要这个脚本：
- Origin 只有 Windows 版，originpro 必须连接本机已安装的 Origin（无独立 CLI）
- macOS / Linux 上无法渲染 Origin 图——所以画廊里的 Origin 徽章目前只标
  "有脚本"，PNG 需要在 Windows 上跑本脚本生成后拷回 gallery/origin/

用法（Windows + Origin 2021 以上 + pip install originpro）::

    python render_all_origin.py            # 跑全部，导出到 ./out/
    python render_all_origin.py 16 17      # 只跑 16、17 号

导出后把 out/*.png 拷到库的 gallery/origin/ 即可。
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).parent / 'python'
OUT = Path(__file__).parent / 'out'


def run_one(script: Path, op):
    """import 单个脚本并调用其第一个 make_*/setup_* 函数，导出 PNG."""
    spec = importlib.util.spec_from_file_location(script.stem, script)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fn = next((getattr(mod, n) for n in dir(mod)
               if n.startswith(('make_', 'setup_', 'apply_'))
               and callable(getattr(mod, n))), None)
    if fn is None:
        print(f'  skip {script.name}（没有 make_*/setup_*/apply_* 入口）')
        return
    obj = fn()
    # 导出当前 graph
    try:
        gp = obj if hasattr(obj, 'save_fig') else op.find_graph()
        if gp is not None:
            OUT.mkdir(exist_ok=True)
            gp.save_fig(str(OUT / f'{script.stem}.png'), width=1200)
            print(f'  OK   {script.stem}.png')
    except Exception as e:        # noqa: BLE001
        print(f'  WARN {script.name}: 导出失败 {e}')


def main():
    try:
        import originpro as op
    except ImportError:
        sys.exit('需要在 Windows + Origin 环境运行：pip install originpro')

    wanted = sys.argv[1:]
    scripts = sorted(HERE.glob('[0-9][0-9]_*.py'))
    if wanted:
        scripts = [s for s in scripts
                   if any(s.name.startswith(w.zfill(2)) for w in wanted)]
    # 00_setup_data 先跑（部分脚本依赖 Demo 工作簿）
    setup = HERE / '00_setup_data.py'
    if setup.exists() and setup not in scripts:
        scripts.insert(0, setup)

    print(f'运行 {len(scripts)} 个 Origin 脚本…')
    if op.oext:
        op.set_show(True)
    for s in scripts:
        run_one(s, op)
    print(f'完成。输出目录: {OUT}')


if __name__ == '__main__':
    main()
