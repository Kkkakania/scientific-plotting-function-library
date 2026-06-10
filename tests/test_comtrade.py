"""pytest: COMTRADE 读取器（comtrade_loader / data_loader.load_comtrade）.

用代码合成一个迷你 1999 版 COMTRADE 算例：
3 个模拟通道（正弦 + 第 50 点起故障突增 5 倍）+ 2 个开关量通道，
ASCII 与 BINARY(int16) 各写一份到 tmp_path，再读回验证。
"""
import struct
import sys
from pathlib import Path

import numpy as np
import pytest

UTILS = Path(__file__).resolve().parents[1] / '_utils' / 'python'
sys.path.insert(0, str(UTILS))

from comtrade_loader import read_comtrade  # noqa: E402
import data_loader  # noqa: E402


# ============ 合成算例 ============

FS = 1000.0          # 采样率 Hz
N = 100              # 采样点数
FREQ = 50.0          # 系统频率 Hz
FAULT_AT = 50        # 故障起始样本

# (通道名, 相别, 单位, a, b, 正常幅值)
CHANNELS = [
    ('IA', 'A', 'A', 0.05, 0.0, 100.0),
    ('IB', 'B', 'A', 0.05, 0.0, 100.0),
    ('VC', 'C', 'V', 0.10, 1.0, 220.0),
]
DIGITALS = ['FAULT', 'TRIP']


def _physical_signals():
    """生成 3 路物理量：正弦，FAULT_AT 之后幅值突增 5 倍。"""
    t = np.arange(N) / FS
    gain = np.where(np.arange(N) >= FAULT_AT, 5.0, 1.0)
    sigs = {}
    for k, (name, _ph, _u, _a, _b, amp) in enumerate(CHANNELS):
        sigs[name] = amp * gain * np.sin(2 * np.pi * FREQ * t - k * 2 * np.pi / 3)
    return t, sigs


def _raw_counts(sigs):
    """物理量 → int16 原始码值: raw = round((phys - b) / a)。"""
    raws = {}
    for name, _ph, _u, a, b, _amp in CHANNELS:
        raws[name] = np.round((sigs[name] - b) / a).astype(np.int16)
    return raws


def _digital_states():
    fault = (np.arange(N) >= FAULT_AT).astype(int)
    trip = (np.arange(N) >= FAULT_AT + 10).astype(int)
    return {'FAULT': fault, 'TRIP': trip}


def _write_cfg(path, ft):
    lines = ['TEST_STA,DEV1,1999', f'{len(CHANNELS) + len(DIGITALS)},{len(CHANNELS)}A,{len(DIGITALS)}D']
    for i, (name, ph, unit, a, b, _amp) in enumerate(CHANNELS, 1):
        lines.append(f'{i},{name},{ph},,{unit},{a},{b},0,-32767,32767,1,1,P')
    for i, name in enumerate(DIGITALS, 1):
        lines.append(f'{i},{name},,,0')
    lines += [
        f'{FREQ:g}',
        '1',
        f'{FS:g},{N}',
        '01/06/2026,00:00:00.000000',
        '01/06/2026,00:00:00.050000',
        ft,
        '1',
    ]
    path.write_text('\n'.join(lines) + '\n', encoding='latin-1')


def make_case(tmp_path, ft):
    """在 tmp_path 写一组 .cfg/.dat，返回 (cfg_path, t, 物理信号, 开关量)。"""
    t, sigs = _physical_signals()
    raws = _raw_counts(sigs)
    digs = _digital_states()
    names = [c[0] for c in CHANNELS]

    cfg_path = tmp_path / f'mini_{ft.lower()}.cfg'
    dat_path = cfg_path.with_suffix('.dat')
    _write_cfg(cfg_path, ft)

    timestamps_us = np.round(t * 1e6).astype(int)
    if ft == 'ASCII':
        with open(dat_path, 'w', encoding='latin-1') as f:
            for i in range(N):
                fields = [str(i + 1), str(timestamps_us[i])]
                fields += [str(int(raws[n][i])) for n in names]
                fields += [str(int(digs[d][i])) for d in DIGITALS]
                f.write(','.join(fields) + '\n')
    else:  # BINARY: <uint32 n><uint32 ts><int16 × nA><uint16 开关量字>
        with open(dat_path, 'wb') as f:
            for i in range(N):
                word = sum(int(digs[d][i]) << k for k, d in enumerate(DIGITALS))
                f.write(struct.pack('<II', i + 1, int(timestamps_us[i])))
                f.write(struct.pack(f'<{len(names)}h', *(int(raws[n][i]) for n in names)))
                f.write(struct.pack('<H', word))

    return cfg_path, t, sigs, digs


# ============ 测试 ============

@pytest.mark.parametrize('ft', ['ASCII', 'BINARY'])
def test_roundtrip(tmp_path, ft):
    cfg_path, t, sigs, digs = make_case(tmp_path, ft)
    rec = read_comtrade(cfg_path)

    # 元信息
    assert rec['station'] == 'TEST_STA'
    assert rec['freq'] == pytest.approx(FREQ)

    # 通道数
    assert len(rec['analog']) == len(CHANNELS)
    assert len(rec['digital']) == len(DIGITALS)
    assert list(rec['analog']) == [c[0] for c in CHANNELS]
    assert list(rec['digital']) == DIGITALS

    # 采样点数与时间轴（由 cfg 采样率段构造）
    for name in rec['analog']:
        assert rec['analog'][name].shape == (N,)
    np.testing.assert_allclose(rec['t'], t, atol=1e-9)

    # 缩放后幅值: 量化误差 ≤ a/2
    for name, _ph, _u, a, _b, _amp in CHANNELS:
        np.testing.assert_allclose(rec['analog'][name], sigs[name], atol=a * 0.51)

    # 故障突增确实读到了（故障段峰值约为正常段 5 倍）
    ia = rec['analog']['IA']
    assert np.abs(ia[FAULT_AT:]).max() > 3 * np.abs(ia[:FAULT_AT]).max()

    # 开关量
    for d in DIGITALS:
        np.testing.assert_array_equal(rec['digital'][d], digs[d])


@pytest.mark.parametrize('ft', ['ASCII', 'BINARY'])
def test_load_comtrade_wrapper(tmp_path, ft):
    cfg_path, _t, _sigs, _digs = make_case(tmp_path, ft)
    rec = data_loader.load_comtrade(cfg_path)
    assert set(rec) == {'analog', 'digital', 't', 'freq', 'station'}
    assert rec['t'].shape == (N,)


def test_missing_dat(tmp_path):
    cfg_path = tmp_path / 'orphan.cfg'
    _write_cfg(cfg_path, 'ASCII')
    with pytest.raises(FileNotFoundError, match=r'缺少 COMTRADE 数据文件'):
        read_comtrade(cfg_path)


def test_missing_cfg(tmp_path):
    with pytest.raises(FileNotFoundError, match=r'配置文件不存在'):
        read_comtrade(tmp_path / 'nope.cfg')
