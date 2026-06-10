"""activation_heatmap: 神经网络隐藏层激活值热力图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Hidden layer activations'):
    apply_theme(fig_size=(7, 4))
    rng = np.random.default_rng(7)
    # 32 个神经元 × 50 个样本
    acts = np.tanh(rng.standard_normal((32, 50)) * 1.5)
    fig, ax = plt.subplots()
    im = ax.imshow(acts, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
    fig.colorbar(im, ax=ax, label='activation')
    ax.set_xlabel('sample'); ax.set_ylabel('neuron'); ax.set_title(title)
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
