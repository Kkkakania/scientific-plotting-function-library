"""所有模板共用的合成数据生成器（确定性 seed）."""
import numpy as np


def _rng(seed=0):
    return np.random.default_rng(seed)


def gen_line(n=100, n_series=1, noise=0.05, seed=0):
    rng = _rng(seed)
    x = np.linspace(0, 10, n)
    Y = np.array([np.sin(x + i*np.pi/4) + noise*rng.standard_normal(n)
                  for i in range(n_series)])
    return x, Y if n_series > 1 else Y[0]


def gen_scatter(n=200, n_groups=1, separation=2.0, seed=0):
    rng = _rng(seed)
    X, Y, G = [], [], []
    for k in range(n_groups):
        X.append(rng.normal(k*separation, 1, n))
        Y.append(rng.normal(k*separation, 1, n))
        G.append(np.full(n, k))
    return np.concatenate(X), np.concatenate(Y), np.concatenate(G)


def gen_groups(n_cat=5, n_series=2, seed=0):
    rng = _rng(seed)
    labels = [f'cat{i+1}' for i in range(n_cat)]
    values = rng.uniform(10, 80, (n_series, n_cat))
    return labels, values


def gen_matrix(rows=8, cols=10, kind='random', seed=0):
    rng = _rng(seed)
    if kind == 'random':
        return rng.uniform(0, 1, (rows, cols))
    if kind == 'correlation':
        n = max(rows, cols)
        A = rng.standard_normal((100, n))
        return np.corrcoef(A.T)
    if kind == 'block':
        M = rng.normal(0, 0.3, (rows, cols))
        for k in range(min(rows, cols)//2):
            M[k*2:(k+1)*2, k*2:(k+1)*2] += 1.0
        return M
    raise ValueError(kind)


def gen_timeseries(n=365, n_series=1, season=30, trend=0.001, seed=0):
    rng = _rng(seed)
    t = np.arange(n)
    Y = []
    for i in range(n_series):
        base = trend*t + np.sin(2*np.pi*t/season + i) + 0.2*rng.standard_normal(n)
        Y.append(base + i*0.5)
    return t, np.array(Y) if n_series > 1 else Y[0]


def gen_signal(fs=1000, T=1.0, components=((50, 1.0), (120, 0.6)), noise=0.3, seed=0):
    rng = _rng(seed)
    N = int(fs*T)
    t = np.arange(N) / fs
    sig = np.zeros(N)
    for f, a in components:
        sig += a*np.sin(2*np.pi*f*t)
    sig += noise*rng.standard_normal(N)
    return t, sig, fs


def gen_3d_surface(n=60, kind='peaks'):
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)
    if kind == 'peaks':
        Z = 3*(1-X)**2*np.exp(-X**2 - (Y+1)**2) \
            - 10*(X/5 - X**3 - Y**5)*np.exp(-X**2 - Y**2) \
            - np.exp(-(X+1)**2 - Y**2)/3
    elif kind == 'sinc':
        R = np.sqrt(X**2 + Y**2) + 1e-9
        Z = np.sin(R)/R
    elif kind == 'gaussian':
        Z = np.exp(-(X**2 + Y**2)/2)
    else:
        raise ValueError(kind)
    return X, Y, Z


def gen_categorical_pairs(n=8, seed=0):
    rng = _rng(seed)
    cats = [f'item{i+1}' for i in range(n)]
    before = rng.uniform(20, 80, n)
    after  = before + rng.normal(5, 8, n)
    return cats, before, after


def gen_distribution(n=500, kind='normal', seed=0):
    rng = _rng(seed)
    if kind == 'normal':   return rng.normal(0, 1, n)
    if kind == 'bimodal':  return np.concatenate([rng.normal(-1.5, 0.6, n//2),
                                                  rng.normal( 1.5, 0.6, n//2)])
    if kind == 'skewed':   return rng.exponential(1.0, n)
    raise ValueError(kind)
