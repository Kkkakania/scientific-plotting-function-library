"""model_diagnostics_polar_signature: 模型诊断极坐标指纹（polar 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='model diagnostics: polar signature'):
    return make_template_figure('polar_profile', seed=1510, title=title, domain='model diagnostics', topic='polar signature')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
