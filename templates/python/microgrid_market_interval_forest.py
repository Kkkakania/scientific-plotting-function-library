"""microgrid_market_interval_forest: 微电网与市场区间森林图（interval 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='microgrid and market analysis: interval forest'):
    return make_template_figure('interval_forest', seed=3815, title=title, domain='microgrid and market analysis', topic='interval forest')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
