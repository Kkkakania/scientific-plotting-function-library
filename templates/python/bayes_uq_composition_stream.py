"""bayes_uq_composition_stream: 贝叶斯与不确定性量化组成流面积（stacked-area 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='Bayesian uncertainty quantification: composition stream'):
    return make_template_figure('stacked_area', seed=4316, title=title, domain='Bayesian uncertainty quantification', topic='composition stream')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
