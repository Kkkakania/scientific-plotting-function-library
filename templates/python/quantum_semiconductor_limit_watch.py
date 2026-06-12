"""quantum_semiconductor_limit_watch: 量子与半导体控制限监测（control-limit 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='quantum and semiconductor analysis: control limit watch'):
    return make_template_figure('control_limit', seed=3002, title=title, domain='quantum and semiconductor analysis', topic='control limit watch')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
