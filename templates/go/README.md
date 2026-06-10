# Go 绘图模板（gonum/plot）

本目录是函数库的 **Go 语言端**：与 Python/MATLAB 模板同源同风格的 gonum/plot 实现。

## 目录

```
go/
├── go.mod                    模块定义（依赖 gonum.org/v1/plot v0.14.0）
├── sciplot/                  共享包：主题 + 配色（hex 与 sci_palettes.py 完全同源）
└── cmd/<name>/main.go        每个模板一个可独立运行的程序
```

已移植 8 个代表性模板：

| 模板 | 对照 Python 版 |
|---|---|
| `line_multi` | 多条折线对比 |
| `scatter_grouped` | 分组散点 |
| `bar_grouped` | 分组柱状 |
| `histogram_basic` | 基础直方图 |
| `three_phase_waveform` | 三相波形（电气） |
| `bode_diagram` | Bode 幅频（log 轴） |
| `step_response` | 二阶阶跃响应族 |
| `wind_power_curve` | 风机功率曲线（v1.5 新增主题） |

## 运行

```bash
cd templates/go
go mod tidy          # 第一次需要联网拉取 gonum/plot
go run ./cmd/line_multi
open line_multi.png
```

## 用 sciplot 包写自己的图

```go
import "sciplot.example/templates/sciplot"

p := plot.New()
sciplot.ApplyTheme(p)              // 论文风格（字号/线宽对齐 Python 端）
line.Color = sciplot.Cycle(0)      // 循环色与 _utils/python/palette.py 一致
pal, _ := sciplot.Get("dark_bright7")  // 68 套色板中的分类板（部分镜像）
cmap := sciplot.Sequential(pal, 256)   // 锚点插值成连续色
```

## ⚠ 验证状态

- 本目录代码在**无 Go 工具链的沙箱**中编写，尚未在本机编译运行。
  API 全部取自 gonum/plot v0.14 的稳定子集（`plot.New` / `plotter.NewLine` /
  `NewScatter` / `NewBarChart` / `NewHist` / `LogScale`），风险低。
- 第一次使用请先 `go mod tidy && go vet ./...`，如有编译错误多半是
  gonum/plot 版本差异，按报错微调即可。
- 验证通过后欢迎把结果记到 `docs/verification_report.md`。
