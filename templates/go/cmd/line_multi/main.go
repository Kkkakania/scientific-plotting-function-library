// line_multi: 多条折线对比（对照 templates/python/line_multi.py）
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
	p.Title.Text = "Multi-series comparison"
	p.X.Label.Text = "x"
	p.Y.Label.Text = "y"
	p.Add(plotter.NewGrid())

	phases := []float64{0, 0.7, 1.4}
	for i, ph := range phases {
		pts := make(plotter.XYs, 200)
		for j := range pts {
			x := float64(j) / 199 * 10
			pts[j].X = x
			pts[j].Y = math.Sin(x+ph) * math.Exp(-x/12)
		}
		line, err := plotter.NewLine(pts)
		if err != nil {
			panic(err)
		}
		line.Color = sciplot.Cycle(i)
		line.Width = 1.5
		p.Add(line)
		p.Legend.Add("series "+string(rune('A'+i)), line)
	}
	if err := sciplot.SaveDefault(p, "line_multi.png"); err != nil {
		panic(err)
	}
}
