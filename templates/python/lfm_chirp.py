"""lfm_chirp: 线性调频（LFM/chirp）信号——实部波形 + 瞬时频率 + STFT 时频图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
from theme import apply_theme
from palette import cycle, sequential

def make_figure(title='Linear FM chirp'):
    apply_theme(fig_size=(7.5, 5))
    B = 6e6                     # 带宽 (Hz)
    T = 8e-6                    # 脉宽 (s)
    K = B / T                   # 调频斜率 (Hz/s)
    fs = 5 * B                  # 过采样
    t = np.arange(-T / 2, T / 2, 1 / fs)
    phase = np.pi * K * t ** 2
    st = np.exp(1j * phase)     # 复包络
    f_inst = K * t              # 瞬时频率
    fig, axs = plt.subplots(2, 2, figsize=(7.5, 5))
    axs[0, 0].plot(t * 1e6, st.real, color=cycle(0), lw=1)
    axs[0, 0].set_title('real part'); axs[0, 0].set_xlabel('t (us)'); axs[0, 0].set_ylabel('amplitude')
    axs[0, 1].plot(t * 1e6, st.imag, color=cycle(1), lw=1)
    axs[0, 1].set_title('imag part'); axs[0, 1].set_xlabel('t (us)'); axs[0, 1].set_ylabel('amplitude')
    axs[1, 0].plot(t * 1e6, f_inst * 1e-6, color=cycle(2), lw=2)
    axs[1, 0].set_title('instantaneous freq'); axs[1, 0].set_xlabel('t (us)'); axs[1, 0].set_ylabel('f (MHz)')
    f, tt, Sxx = spectrogram(st.real, fs=fs, nperseg=64, noverlap=56)
    pcm = axs[1, 1].pcolormesh(tt * 1e6, f * 1e-6, 10 * np.log10(Sxx + 1e-12),
                               cmap=sequential('blue'), shading='auto')
    axs[1, 1].set_title('STFT (dB)'); axs[1, 1].set_xlabel('t (us)'); axs[1, 1].set_ylabel('f (MHz)')
    fig.colorbar(pcm, ax=axs[1, 1])
    for ax in axs.flat:
        ax.grid(True, linestyle=':', alpha=0.4)
    fig.suptitle(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
