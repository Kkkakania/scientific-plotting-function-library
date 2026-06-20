# CSV 到论文图工作流示例

这个示例展示如何从一个干净的 CSV 文件生成投稿前可自查的科研图件。它面向研究生、实验室同学和需要把 Excel/CSV 数据转成论文图的人。

示例边界：

- 数据是合成的，不对应真实实验。
- 脚本只演示图件呈现、导出和检查流程。
- 不处理论文内容判断，不修改实验结论，不替代期刊、学校或导师要求。
- 输出图默认写到本地 `out/` 目录；不要把私有数据或本地路径提交进仓库。

## 文件

| 文件 | 用途 |
|---|---|
| `sample_measurements.csv` | 合成测量数据，包含时间、电压、电流、温度 |
| `plot_csv_workflow.py` | Python 版本，从 CSV 生成双面板图并导出 PNG/PDF |
| `plot_csv_workflow.m` | MATLAB 版本，使用同一份 CSV 生成相同结构图 |
| `submission_check_report.md` | 投稿前图件检查报告模板示例 |

## Python 使用

```bash
python examples/csv-workflow/plot_csv_workflow.py \
  --csv examples/csv-workflow/sample_measurements.csv \
  --out-dir /tmp/csv-workflow-out
```

生成：

- `/tmp/csv-workflow-out/csv_workflow_voltage_current.png`
- `/tmp/csv-workflow-out/csv_workflow_voltage_current.pdf`

## MATLAB 使用

```matlab
plot_csv_workflow( ...
    'examples/csv-workflow/sample_measurements.csv', ...
    '/tmp/csv-workflow-out')
```

如果在 Windows 上运行，把输出路径换成自己的临时目录。

## 自查建议

生成图后，按 `submission_check_report.md` 记录：

- 坐标轴单位是否完整。
- 字号、线宽、marker 是否足够清楚。
- PNG 和 PDF 放大后是否清晰。
- 图例是否遮挡数据。
- 导出文件名是否不含本地隐私路径。

这个流程可以反哺 `matlab-figure-ci` 的检查报告，也可以作为“图件投稿前检查资料包”的公开 clean-room 示例。
