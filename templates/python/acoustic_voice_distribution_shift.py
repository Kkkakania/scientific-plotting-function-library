"""acoustic_voice_distribution_shift: 声学与声纹分布漂移（distribution 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='acoustic and voice analysis: distribution shift'):
    return make_template_figure('distribution', seed=3112, title=title, domain='acoustic and voice analysis', topic='distribution shift')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
