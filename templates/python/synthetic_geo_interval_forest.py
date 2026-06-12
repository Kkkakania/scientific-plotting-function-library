"""synthetic_geo_interval_forest: 合成地理栅格区间森林图（interval 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='synthetic geospatial grid: interval forest'):
    return make_template_figure('interval_forest', seed=2115, title=title, domain='synthetic geospatial grid', topic='interval forest')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
