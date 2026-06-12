"""acoustic_voice_phase_portrait: 声学与声纹相平面画像（phase-plane 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='acoustic and voice analysis: phase portrait'):
    return make_template_figure('phase_plane', seed=3111, title=title, domain='acoustic and voice analysis', topic='phase portrait')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
