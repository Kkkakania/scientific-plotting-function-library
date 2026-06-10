// Package sciplot 提供与本库 Python/MATLAB 端一致的科研绘图主题与配色。
//
// 配色数据与 palettes/python/sci_palettes.py 完全同源（hex 一致），
// 主题参数对齐 _utils/python/theme.py（无顶/右边框、点状网格、Arial 字体族）。
package sciplot

import (
	"fmt"
	"image/color"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/vg"
	"gonum.org/v1/plot/vg/draw"
)

// Hex 把 "#RRGGBB" 转成 color.RGBA。非法输入会 panic（配色是常量，应在开发期暴露）。
func Hex(s string) color.RGBA {
	var r, g, b uint8
	if _, err := fmt.Sscanf(s, "#%02x%02x%02x", &r, &g, &b); err != nil {
		panic("sciplot: bad hex color " + s)
	}
	return color.RGBA{R: r, G: g, B: b, A: 255}
}

// 分类调色板（与 sci_palettes.py 同源）
var Palettes = map[string][]string{
	"wong":         {"#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"},
	"okabe_ito":    {"#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#999999"},
	"muted5":       {"#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3"},
	"deep6":        {"#003049", "#D62828", "#F77F00", "#FCBF49", "#06A77D", "#7251B5"},
	"ieee_tech":    {"#003F7F", "#5E81AC", "#88C0D0", "#4C566A", "#D08770"},
	"dark_bright7": {"#E6CF65", "#00CFDD", "#F58A4A", "#77D3A6", "#8190E6", "#FF7B80", "#E1D4D7"},
	"vivid6":       {"#005AAB", "#DE1655", "#379F3D", "#F28D1F", "#00CFE5", "#A5439D"},
	"safe10":       {"#004C85", "#AC2B59", "#37804F", "#D75E43", "#00A1CC", "#B98DEC", "#D8AA30", "#6AD3C0", "#FEC6A7", "#D0DFEB"},
	"mono_blue4":   {"#B5C9D7", "#00A4DE", "#0077AD", "#324550"},
	"mono_warm4":   {"#DAC1BB", "#E27E65", "#B0533D", "#56423D"},
}

// 默认循环色（与 _utils/python/palette.py 的 CATEGORICAL 一致）
var categorical = []string{
	"#0072B2", "#D55E00", "#009E73", "#CC79A7",
	"#F0E442", "#56B4E9", "#E69F00", "#999999",
}

// Cycle 返回第 i 个循环色（自动取模）。
func Cycle(i int) color.RGBA { return Hex(categorical[i%len(categorical)]) }

// Get 按名称取分类调色板；不存在返回 (nil, false)。
func Get(name string) ([]color.RGBA, bool) {
	hexes, ok := Palettes[name]
	if !ok {
		return nil, false
	}
	out := make([]color.RGBA, len(hexes))
	for i, h := range hexes {
		out[i] = Hex(h)
	}
	return out, true
}

// Sequential 在锚点色之间线性插值出 n 个颜色（顺序色板用）。
func Sequential(anchors []color.RGBA, n int) []color.RGBA {
	if n < 2 || len(anchors) < 2 {
		return anchors
	}
	out := make([]color.RGBA, n)
	for i := 0; i < n; i++ {
		t := float64(i) / float64(n-1) * float64(len(anchors)-1)
		k := int(t)
		if k >= len(anchors)-1 {
			out[i] = anchors[len(anchors)-1]
			continue
		}
		f := t - float64(k)
		a, b := anchors[k], anchors[k+1]
		lerp := func(x, y uint8) uint8 { return uint8(float64(x) + (float64(y)-float64(x))*f) }
		out[i] = color.RGBA{lerp(a.R, b.R), lerp(a.G, b.G), lerp(a.B, b.B), 255}
	}
	return out
}

// ApplyTheme 套用与 Python 端 apply_theme() 对齐的论文风格。
func ApplyTheme(p *plot.Plot) {
	gray := color.RGBA{120, 120, 120, 255}
	p.BackgroundColor = color.White
	p.Title.TextStyle.Font.Size = vg.Points(10)
	for _, ax := range []*plot.Axis{&p.X, &p.Y} {
		ax.Label.TextStyle.Font.Size = vg.Points(9)
		ax.Tick.Label.Font.Size = vg.Points(8)
		ax.LineStyle.Width = vg.Points(0.8)
		ax.Tick.LineStyle.Width = vg.Points(0.8)
	}
	p.Legend.TextStyle.Font.Size = vg.Points(8)
	p.Legend.Top = true
	_ = gray
}

// GridStyle 返回点状浅网格（对齐 grid.linestyle=':' alpha=0.5）。
func GridStyle() draw.LineStyle {
	return draw.LineStyle{
		Color:  color.RGBA{0, 0, 0, 70},
		Width:  vg.Points(0.5),
		Dashes: []vg.Length{vg.Points(1), vg.Points(3)},
	}
}

// SaveDefault 以 6x4 英寸保存（对齐 figure.figsize=(6,4)）。
func SaveDefault(p *plot.Plot, path string) error {
	return p.Save(6*vg.Inch, 4*vg.Inch, path)
}
