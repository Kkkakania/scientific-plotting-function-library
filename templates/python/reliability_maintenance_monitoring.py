"""reliability_maintenance_monitoring: 可靠性与维修监测带状时序（time-band 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='reliability and maintenance: monitoring band time series'):
    return make_template_figure('band_timeseries', seed=3301, title=title, domain='reliability and maintenance', topic='monitoring band time series')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
