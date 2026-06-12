"""microgrid_market_factor_lollipop: 微电网与市场因子棒棒糖（lollipop 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='microgrid and market analysis: factor lollipop'):
    return make_template_figure('lollipop', seed=3814, title=title, domain='microgrid and market analysis', topic='factor lollipop')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
