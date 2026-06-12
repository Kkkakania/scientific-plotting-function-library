"""bayes_uq_contribution_bridge: 贝叶斯与不确定性量化贡献瀑布桥（waterfall 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='Bayesian uncertainty quantification: contribution waterfall'):
    return make_template_figure('waterfall', seed=4308, title=title, domain='Bayesian uncertainty quantification', topic='contribution waterfall')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
