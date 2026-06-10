"""COMTRADE 读取器：IEEE C37.111-1999 电力故障录波标准（纯 numpy 实现）.

支持 1999 版 .cfg + .dat（ASCII 与 BINARY/int16 两种数据格式）。

用法::

    from comtrade_loader import read_comtrade

    rec = read_comtrade('fault.cfg')
    rec['analog']['IA']     # 缩放后的物理量 (ndarray)
    rec['digital']['TRIP']  # 0/1 开关量 (ndarray)
    rec['t']                # 时间轴 (s)
    rec['freq']             # 系统频率 (Hz)
    rec['station']          # 站名

物理值换算: value = a * raw + b （a/b 取自 .cfg 各模拟通道行）。
"""
from pathlib import Path
import numpy as np


# ============ 公共入口 ============

def read_comtrade(cfg_path):
    """读取一组 COMTRADE 文件（.cfg + .dat）。

    参数
    ----
    cfg_path : str | Path
        .cfg 配置文件路径；同名 .dat 数据文件须在同目录。

    返回
    ----
    dict::

        {
            'analog':  {通道名: ndarray (物理值)},
            'digital': {通道名: ndarray (0/1)},
            't':       ndarray (s),
            'freq':    float (Hz),
            'station': str,
        }
    """
    cfg_path = Path(cfg_path)
    if not cfg_path.exists():
        raise FileNotFoundError(f'COMTRADE 配置文件不存在: {cfg_path}')

    cfg = _parse_cfg(cfg_path)
    dat_path = _find_dat(cfg_path)

    if cfg['ft'] == 'ASCII':
        raw_analog, raw_digital, timestamps = _read_dat_ascii(dat_path, cfg)
    elif cfg['ft'] == 'BINARY':
        raw_analog, raw_digital, timestamps = _read_dat_binary(dat_path, cfg)
    else:
        raise ValueError(f"不支持的数据文件类型: {cfg['ft']!r} (仅支持 ASCII / BINARY)")

    n_samples = raw_analog.shape[0] if cfg['n_analog'] else raw_digital.shape[0]

    # 物理值 = a * raw + b
    analog = {}
    for i, ch in enumerate(cfg['analog_channels']):
        analog[ch['name']] = ch['a'] * raw_analog[:, i].astype(float) + ch['b']

    digital = {}
    for i, ch in enumerate(cfg['digital_channels']):
        digital[ch['name']] = raw_digital[:, i].astype(int)

    t = _build_time_axis(cfg, timestamps, n_samples)

    return {
        'analog': analog,
        'digital': digital,
        't': t,
        'freq': cfg['freq'],
        'station': cfg['station'],
    }


# ============ .cfg 解析 ============

def _parse_cfg(cfg_path):
    """解析 1999 版 .cfg（latin-1 容错读取）。"""
    with open(cfg_path, encoding='latin-1') as f:
        lines = [ln.rstrip('\r\n') for ln in f if ln.strip() != '']

    it = iter(lines)

    # 第 1 行: station_name, rec_dev_id[, rev_year]
    head = next(it).split(',')
    station = head[0].strip()
    rev_year = head[2].strip() if len(head) >= 3 else '1991'

    # 第 2 行: TT, ##A, ##D  （如 "6,4A,2D"）
    counts = next(it).split(',')
    n_analog = int(counts[1].strip().upper().rstrip('A'))
    n_digital = int(counts[2].strip().upper().rstrip('D'))

    # 模拟通道: An,ch_id,ph,ccbm,uu,a,b,skew,min,max[,primary,secondary,PS]
    analog_channels = []
    for _ in range(n_analog):
        parts = next(it).split(',')
        analog_channels.append({
            'name': parts[1].strip(),
            'phase': parts[2].strip() if len(parts) > 2 else '',
            'unit': parts[4].strip() if len(parts) > 4 else '',
            'a': float(parts[5]) if len(parts) > 5 and parts[5].strip() else 1.0,
            'b': float(parts[6]) if len(parts) > 6 and parts[6].strip() else 0.0,
        })

    # 开关量通道: Dn,ch_id[,ph,ccbm,y]
    digital_channels = []
    for _ in range(n_digital):
        parts = next(it).split(',')
        digital_channels.append({'name': parts[1].strip()})

    # 系统频率
    freq = float(next(it).strip())

    # 采样率段: nrates 行数 + 每行 "samp,endsamp"
    nrates = int(float(next(it).strip()))
    rates = []
    for _ in range(max(nrates, 1)):
        parts = next(it).split(',')
        rates.append((float(parts[0]), int(float(parts[1]))))

    # 起始 / 触发时间戳
    start_time = next(it).strip()
    trigger_time = next(it).strip()

    # 数据文件类型
    ft = next(it).strip().upper()

    # 1999 版: 时间倍乘因子（可缺省）
    try:
        timemult = float(next(it).strip())
    except (StopIteration, ValueError):
        timemult = 1.0

    return {
        'station': station,
        'rev_year': rev_year,
        'n_analog': n_analog,
        'n_digital': n_digital,
        'analog_channels': analog_channels,
        'digital_channels': digital_channels,
        'freq': freq,
        'nrates': nrates,
        'rates': rates,
        'start_time': start_time,
        'trigger_time': trigger_time,
        'ft': ft,
        'timemult': timemult,
    }


def _find_dat(cfg_path):
    """在 .cfg 同目录寻找同名 .dat（大小写均试），找不到给出清晰报错。"""
    for suffix in ('.dat', '.DAT', '.Dat'):
        candidate = cfg_path.with_suffix(suffix)
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        f'缺少 COMTRADE 数据文件: {cfg_path.with_suffix(".dat")}\n'
        f'(.cfg 与 .dat 必须同名同目录，请检查数据文件是否存在)'
    )


# ============ .dat 读取 ============

def _read_dat_ascii(dat_path, cfg):
    """ASCII .dat: 每行 n,timestamp,a1..aA,d1..dD（逗号分隔）。"""
    nA, nD = cfg['n_analog'], cfg['n_digital']
    rows = []
    with open(dat_path, encoding='latin-1') as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            fields = ln.split(',')
            rows.append([float(v) if v.strip() else np.nan for v in fields])
    data = np.array(rows, dtype=float)
    if data.shape[1] < 2 + nA + nD:
        raise ValueError(
            f'ASCII .dat 列数不足: 期望 {2 + nA + nD} 列, 实得 {data.shape[1]} 列'
        )
    timestamps = data[:, 1]
    raw_analog = data[:, 2:2 + nA]
    raw_digital = data[:, 2 + nA:2 + nA + nD]
    return raw_analog, raw_digital, timestamps


def _read_dat_binary(dat_path, cfg):
    """BINARY .dat (1999, int16):

    每个样本记录 = uint32 序号 + uint32 时间戳
                 + nA × int16 模拟量 + ceil(nD/16) × uint16 开关量字
    全部小端。
    """
    nA, nD = cfg['n_analog'], cfg['n_digital']
    n_words = (nD + 15) // 16
    rec_bytes = 4 + 4 + 2 * nA + 2 * n_words

    raw = np.fromfile(dat_path, dtype=np.uint8)
    if raw.size == 0:
        raise ValueError(f'BINARY .dat 为空文件: {dat_path}')
    if raw.size % rec_bytes != 0:
        raise ValueError(
            f'BINARY .dat 长度异常: 文件 {raw.size} 字节不是单记录 '
            f'{rec_bytes} 字节的整数倍 (nA={nA}, nD={nD})'
        )
    n_samples = raw.size // rec_bytes
    rec = raw.reshape(n_samples, rec_bytes)

    timestamps = rec[:, 4:8].copy().view('<u4').reshape(n_samples).astype(float)
    analog_bytes = rec[:, 8:8 + 2 * nA].copy()
    raw_analog = analog_bytes.view('<i2').reshape(n_samples, nA).astype(float)

    raw_digital = np.zeros((n_samples, nD), dtype=int)
    if nD:
        word_bytes = rec[:, 8 + 2 * nA:].copy()
        words = word_bytes.view('<u2').reshape(n_samples, n_words)
        for d in range(nD):
            raw_digital[:, d] = (words[:, d // 16] >> (d % 16)) & 1
    return raw_analog, raw_digital, timestamps


# ============ 时间轴 ============

def _build_time_axis(cfg, timestamps, n_samples):
    """优先按 .cfg 采样率段构造时间轴；采样率未知(<=0)时退回时间戳列。

    时间戳单位为微秒，乘 timemult（1999 版）换算为秒。
    """
    rates = cfg['rates']
    if rates and rates[0][0] > 0:
        t = np.empty(n_samples, dtype=float)
        idx = 0
        t_prev = 0.0
        for samp, endsamp in rates:
            end = min(endsamp, n_samples)
            n_seg = end - idx
            if n_seg <= 0:
                continue
            t[idx:end] = t_prev + np.arange(n_seg) / samp
            t_prev = t[end - 1] + 1.0 / samp
            idx = end
        if idx < n_samples:  # cfg 申报样本数少于实际样本，按最后一段速率外推
            samp = rates[-1][0]
            t[idx:] = t_prev + np.arange(n_samples - idx) / samp
        return t
    return timestamps * cfg['timemult'] * 1e-6
