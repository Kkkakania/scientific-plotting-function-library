"""microgrid_market_limit_watch: 微电网与市场控制限监测（control-limit 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='microgrid and market analysis: control limit watch'):
    return make_template_figure('control_limit', seed=3802, title=title, domain='microgrid and market analysis', topic='control limit watch')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
