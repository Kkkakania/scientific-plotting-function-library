"""bayes_uq_polar_signature: 贝叶斯与不确定性量化极坐标指纹（polar 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='Bayesian uncertainty quantification: polar signature'):
    return make_template_figure('polar_profile', seed=4310, title=title, domain='Bayesian uncertainty quantification', topic='polar signature')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
