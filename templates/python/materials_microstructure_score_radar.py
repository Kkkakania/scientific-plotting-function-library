"""materials_microstructure_score_radar: 材料微结构多维评分雷达（radar 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='materials microstructure: multi-metric radar'):
    return make_template_figure('radar', seed=1807, title=title, domain='materials microstructure', topic='multi-metric radar')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
