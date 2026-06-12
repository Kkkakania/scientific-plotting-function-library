"""geoscience_grid_factor_lollipop: 地学栅格场因子棒棒糖（lollipop 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='geoscience grid analysis: factor lollipop'):
    return make_template_figure('lollipop', seed=4514, title=title, domain='geoscience grid analysis', topic='factor lollipop')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
