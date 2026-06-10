// step_response: 二阶系统阶跃响应族（对照 templates/python/step_response.py）
package main

import (
	"fmt"
	"math"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"sciplot.example/templates/sciplot"
)

func main() {
	p := plot.New()
	sciplot.ApplyTheme(p)
	p.Title.Text = "Second-order step response"
	p.X.Label.Text = "time (s)"
	p.Y.Label.Text = "output"
	p.Add(plotter.NewGrid())

	wn := 2.0
	for i, zeta := range []float64{0.2, 0.5, 0.8, 1.2} {
		pts := make(plotter.XYs, 400)
		for j := range pts {
			t := float64(j) / 399 * 8
			var y float64
			if zeta < 1 {
				wd := wn * math.Sqrt(1-zeta*zeta)
				phi := math.Acos(zeta)
				y = 1 - math.Exp(-zeta*wn*t)/math.Sqrt(1-zeta*zeta)*math.Sin(wd*t+phi)
			} else {
				s1 := -wn * (zeta - math.Sqrt(zeta*zeta-1))
				s2 := -wn * (zeta + math.Sqrt(zeta*zeta-1))
				y = 1 + (s2*math.Exp(s1*t)-s1*math.Exp(s2*t))/(s1-s2)
			}
			pts[j].X, pts[j].Y = t, y
		}
		line, err := plotter.NewLine(pts)
		if err != nil {
			panic(err)
		}
		line.Color = sciplot.Cycle(i)
		line.Width = 1.5
		p.Add(line)
		p.Legend.Add(fmt.Sprintf("ζ = %.1f", zeta), line)
	}
	if err := sciplot.SaveDefault(p, "step_response.png"); err != nil {
		panic(err)
	}
}
