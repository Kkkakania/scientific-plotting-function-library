# 验证报告

自动生成于 `scripts/verify_all.py`，覆盖五大维度。
**总评**: ✓ 全部通过（5 大检查 / 通过 5）



## 1. manifest 完整性

共 239 条 manifest 记录
- ✓ Python 与 MATLAB 各 239 个模板，一对一齐全
- **结果: ✓ 一致**

## 2. 模板渲染

- 通过: **239** / 失败: **0**
- **结果: ✓ 全过**

## 3. 文档链接

- ✓ 全部相对链接有效
- **结果: ✓ 通过**

## 4. 配色 round-trip 精度

- 检查了 60 套调色板
- sRGB ↔ Lab 最大数值误差: **5.02e-15**
- ✓ 全部颜色 round-trip 完美（机器精度）

## 5. 共享工具可用性

- ✓ 11 个共享模块全部 import 成功
  - `theme`, `palette`, `export`, `demo_data`, `data_loader`, `sci_palettes`, `color_lab`, `palette_generator`, `palette_extractor`, `palette_validator`, `bivariate`