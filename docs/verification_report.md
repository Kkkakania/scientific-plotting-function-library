# 验证报告

自动生成于 `scripts/verify_all.py`，覆盖七大维度。
**总评**: ✓ 全部通过（7 大检查 / 通过 7）



## 1. manifest 完整性

共 1000 条 manifest 记录
- ✓ Python 与 MATLAB 各 1000 个模板，一对一齐全
- **结果: ✓ 一致**

## 2. 模板渲染

- 通过: **1000** / 失败: **0**
- **结果: ✓ 全过**

## 3. 文档链接

- ✓ 全部相对链接有效
- **结果: ✓ 通过**

## 4. gallery 完整性

- ✓ light gallery: 1000 / 1000
- ✓ dark gallery: 1000 / 1000
- **结果: ✓ 通过**

## 5. 批次账本一致性

- ✓ 35 个批次文件格式正确
- ✓ 726 个批次条目均有 Python/MATLAB 文件并已进入 manifest
- **结果: ✓ 通过**

## 6. 配色 round-trip 精度

- 检查了 79 套调色板
- sRGB ↔ Lab 最大数值误差: **5.02e-15**
- ✓ 全部颜色 round-trip 完美（机器精度）

## 7. 共享工具可用性

- ✓ 11 个共享模块全部 import 成功
  - `theme`, `palette`, `export`, `demo_data`, `data_loader`, `sci_palettes`, `color_lab`, `palette_generator`, `palette_extractor`, `palette_validator`, `bivariate`