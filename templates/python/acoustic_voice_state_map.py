"""acoustic_voice_state_map: 声学与声纹状态热力图（heatmap 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='acoustic and voice analysis: state heatmap'):
    return make_template_figure('heatmap', seed=3103, title=title, domain='acoustic and voice analysis', topic='state heatmap')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
