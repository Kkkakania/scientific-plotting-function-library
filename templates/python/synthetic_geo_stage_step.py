"""synthetic_geo_stage_step: 合成地理栅格阶段阶梯曲线（step 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='synthetic geospatial grid: stage step curve'):
    return make_template_figure('step_curve', seed=2117, title=title, domain='synthetic geospatial grid', topic='stage step curve')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
