// bode_diagram: 二阶系统幅频特性（log 轴，对照 templates/python/bode_diagram.py）
package main

import (
	"math"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"sciplot.example/templates/sciplot"
)

func main() {
	p := plot.New()
	sciplot.ApplyTheme(p)
	p.Title.Text = "Bode magnitude (2nd-order system)"
	p.X.Label.Text = "frequency (rad/s)"
	p.Y.Label.Text = "magnitude (dB)"
	p.X.Scale = plot.LogScale{}
	p.X.Tick.Marker = plot.LogTicks{Prec: -1}
	p.Add(plotter.NewGrid())

	wn := 10.0
	for i, zeta := range []float64{0.1, 0.3, 0.7} {
		pts := make(plotter.XYs, 300)
		for j := range pts {
			w := math.Pow(10, -1+3*float64(j)/299) // 0.1 ~ 100
			re := 1 - (w/wn)*(w/wn)
			im := 2 * zeta * w / wn
			mag := 1 / math.Hypot(re, im)
			pts[j].X = w
			pts[j].Y = 20 * math.Log10(mag)
		}
		line, err := plotter.NewLine(pts)
		if err != nil {
			panic(err)
		}
		line.Color = sciplot.Cycle(i)
		line.Width = 1.5
		p.Add(line)
		p.Legend.Add("ζ = "+map[float64]string{0.1: "0.1", 0.3: "0.3", 0.7: "0.7"}[zeta], line)
	}
	if err := sciplot.SaveDefault(p, "bode_diagram.png"); err != nil {
		panic(err)
	}
}
