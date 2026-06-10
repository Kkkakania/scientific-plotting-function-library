"""palette_extractor: 从图片榨出代表色.

用 k-means 在 CIE Lab 空间聚类（比 RGB 空间更符合人眼感知）。
还能按 L 通道排序、按彩度过滤背景灰。

用法::

    from palette_extractor import extract_from_image
    palette = extract_from_image('logo.png', n=6, sort='L')
    # 返回 list of hex
"""
import numpy as np
from color_lab import srgb_to_lab, lab_to_srgb, rgb_to_hex


def _kmeans_lab(samples_lab, k, n_iter=30, seed=0):
    """简易 k-means（无第三方依赖），返回聚类中心 (k, 3)."""
    rng = np.random.default_rng(seed)
    # k-means++ 初始化
    n = len(samples_lab)
    centers = [samples_lab[rng.integers(n)]]
    for _ in range(k - 1):
        d2 = np.min(
            np.sum((samples_lab[:, None] - np.array(centers)[None]) ** 2, axis=-1),
            axis=-1,
        )
        probs = d2 / d2.sum()
        centers.append(samples_lab[rng.choice(n, p=probs)])
    centers = np.array(centers)
    # 迭代
    for _ in range(n_iter):
        d2 = np.sum((samples_lab[:, None] - centers[None]) ** 2, axis=-1)
        labels = d2.argmin(axis=-1)
        new_centers = np.array([samples_lab[labels == j].mean(axis=0)
                                if (labels == j).any() else centers[j]
                                for j in range(k)])
        if np.allclose(new_centers, centers, atol=0.5):
            break
        centers = new_centers
    return centers, labels


def extract_from_image(path, n=6, sort='L', filter_bg=True,
                        max_samples=20000, seed=0):
    """从图片文件提取 n 种代表色.

    sort:
        'L'        - 按亮度排序（从亮到暗）
        'h'        - 按色相排序
        'dominant' - 按占比排序（从多到少）
        None       - 不排序

    filter_bg : 是否过滤近灰色（C < 5）防止背景吃掉一个槽
    """
    from PIL import Image
    img = Image.open(path).convert('RGB')
    # 下采样
    arr = np.array(img) / 255.0
    H, W, _ = arr.shape
    flat = arr.reshape(-1, 3)
    if len(flat) > max_samples:
        rng = np.random.default_rng(seed)
        idx = rng.choice(len(flat), max_samples, replace=False)
        flat = flat[idx]
    # 转 Lab
    labs = srgb_to_lab(flat)

    if filter_bg:
        # 过滤掉彩度极低的（背景白/灰/黑）
        C = np.hypot(labs[:, 1], labs[:, 2])
        keep = C > 5
        labs_f = labs[keep] if keep.sum() > n * 50 else labs
    else:
        labs_f = labs

    centers, labels = _kmeans_lab(labs_f, n, seed=seed)

    # 占比
    counts = np.bincount(labels, minlength=n)
    order = None
    if sort == 'L':
        order = np.argsort(-centers[:, 0])             # 亮到暗
    elif sort == 'h':
        h = np.degrees(np.arctan2(centers[:, 2], centers[:, 1])) % 360
        order = np.argsort(h)
    elif sort == 'dominant':
        order = np.argsort(-counts)
    if order is not None:
        centers = centers[order]
        counts = counts[order]

    rgbs = lab_to_srgb(centers)
    return [rgb_to_hex(c) for c in rgbs]


def extract_from_array(rgb_array, n=6, **kw):
    """从 numpy RGB 数组（H×W×3，[0,1] 或 [0,255]）提取."""
    arr = np.asarray(rgb_array, dtype=float)
    if arr.max() > 1.5: arr = arr / 255.0
    flat = arr.reshape(-1, 3)
    labs = srgb_to_lab(flat)
    centers, _ = _kmeans_lab(labs, n, seed=kw.get('seed', 0))
    rgbs = lab_to_srgb(centers)
    return [rgb_to_hex(c) for c in rgbs]


if __name__ == '__main__':
    # 自检：用合成"图片"测试
    import matplotlib.pyplot as plt
    H, W = 50, 100
    img = np.zeros((H, W, 3))
    img[:, :30] = [0.85, 0.20, 0.20]    # 红
    img[:, 30:60] = [0.20, 0.50, 0.85]  # 蓝
    img[:, 60:] = [0.20, 0.75, 0.30]    # 绿
    pal = extract_from_array(img, n=3, sort='dominant')
    print('extracted:', pal)
