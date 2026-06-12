"""logistics_network_monitoring: 物流与网络监测带状时序（time-band 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='logistics and network analysis: monitoring band time series'):
    return make_template_figure('band_timeseries', seed=3401, title=title, domain='logistics and network analysis', topic='monitoring band time series')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
