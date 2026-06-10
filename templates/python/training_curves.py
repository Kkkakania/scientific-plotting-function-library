"""training_curves: 神经网络训练曲线（loss + accuracy 双轴）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Training curves'):
    apply_theme(fig_size=(8, 4.5))
    epochs = np.arange(1, 101); rng = np.random.default_rng(5)
    tr_loss = 2.5 * np.exp(-epochs/30) + 0.1 + 0.04*rng.standard_normal(100)
    va_loss = 2.5 * np.exp(-epochs/30) + 0.25 + 0.08*rng.standard_normal(100)
    tr_acc = 1 - tr_loss/3
    va_acc = 1 - va_loss/3
    fig, (a1, a2) = plt.subplots(1, 2)
    a1.plot(epochs, tr_loss, color=cycle(0), label='train')
    a1.plot(epochs, va_loss, color=cycle(1), label='validation')
    a1.set_xlabel('epoch'); a1.set_ylabel('loss'); a1.legend()
    a1.grid(True, linestyle=':', alpha=0.5)
    a2.plot(epochs, tr_acc, color=cycle(0))
    a2.plot(epochs, va_acc, color=cycle(1))
    a2.set_xlabel('epoch'); a2.set_ylabel('accuracy')
    a2.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(title); fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
