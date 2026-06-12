"""paper_multipanel_monitoring: 论文多面板版式监测带状时序（time-band 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='paper multipanel layout: monitoring band time series'):
    return make_template_figure('band_timeseries', seed=2201, title=title, domain='paper multipanel layout', topic='monitoring band time series')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
