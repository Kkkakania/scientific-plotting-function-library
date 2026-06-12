# 千图计划 v2.0 扩产账本

> 原则：宁可慢，不可水。允许同族变体，但每个模板必须有独立表达价值：
> 新图型、新领域语义或新组合方式至少满足一项。全部保持 Python + MATLAB 双语入口。

本文件记录 v2.0 从 274 个模板扩展到 1000 个模板的公开账本。批次只是内部质量控制单位，
不是对外分阶段发布；最终交付面统一为 v2.0 / 1000。

## 完成范围

| 阶段 | 内容 | 模板数 |
|---|---|---:|
| v1.8 基线 | akun 资料全集精读后形成的稳定库 | 274 |
| S1-S3 | 高级时序、金融/SPC、关系网络、统计推断、电能质量、通信/雷达等手写模板 | 328 |
| S4-S35 | 领域包 × 表达方式的 clean-room 扩产模板 | 1000 |
| v2.0 发布面 | manifest、catalog、Python、MATLAB、gallery、release gate 统一口径 | 1000 |

## 批次账本

所有扩产条目先写入 `_batch_manifests/batch_S*.txt`，每行格式为：

```text
name|category|tag1,tag2|description
```

合并流程：

```bash
python scripts/merge_batch_manifests.py
python scripts/build_manifest.py
```

`merge_batch_manifests.py` 会检查：

- 批次文件格式；
- 模板名重复；
- Python 文件是否存在；
- MATLAB 文件是否存在；
- 同一条目是否已经进入 `_manifest_source.txt`。

## 质量门

v2.0 发布前必须通过：

- `python render_all.py`
- `python render_all.py --dark`
- `python scripts/check_publication_ready.py`
- `python scripts/check_release_state.py`
- `python scripts/verify_all.py`
- `python -m pytest tests/`
- `python scripts/check_matlab_syntax.py`
- `git diff --check`

## Clean-room 边界

公开仓库只包含原创模板、合成数据、共享渲染内核、文档和可审计脚本。
本地 `17 akun` 资料库只作为只读参考，不复制原始源码、截图、二进制素材、商业工具包、
课程资料、论文图片或难以确认来源的配色数据。
