// wind_power_curve: 风机功率曲线 + 实测散点（对照 templates/python/wind_power_curve.go 版）
package main

import (
	"math"
	"math/rand"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
	"gonum.org/v1/plot/vg/draw"
	"sciplot.example/templates/sciplot"
)

func designCurve(v float64) float64 {
	const vin, vrated, vout = 3, 12, 25
	switch {
	case v < vin:
		return 0
	case v < vrated:
		return (v*v*v - vin*vin*vin) / (vrated*vrated*vrated - vin*vin*vin)
	case v < vout:
		return 1
	default:
		return 0
	}
}

func main() {
	rng := rand.New(rand.NewSource(0))
	p := plot.New()
	sciplot.ApplyTheme(p)
	p.Title.Text = "Wind turbine power curve"
	p.X.Label.Text = "wind speed (m/s)"
	p.Y.Label.Text = "power (p.u.)"
	p.Add(plotter.NewGrid())

	scada := make(plotter.XYs, 220)
	for i := range scada {
		v := 0.5 + rng.Float64()*26.5
		scada[i].X = v
		scada[i].Y = math.Max(0, designCurve(v)+rng.NormFloat64()*0.03)
	}
	s, err := plotter.NewScatter(scada)
	if err != nil {
		panic(err)
	}
	s.GlyphStyle = draw.GlyphStyle{Color: sciplot.Cycle(5), Radius: vg.Points(1.6), Shape: draw.CircleGlyph{}}
	p.Add(s)
	p.Legend.Add("SCADA data", s)

	pts := make(plotter.XYs, 400)
	for j := range pts {
		v := float64(j) / 399 * 28
		pts[j].X, pts[j].Y = v, designCurve(v)
	}
	line, err := plotter.NewLine(pts)
	if err != nil {
		panic(err)
	}
	line.Color = sciplot.Cycle(1)
	line.Width = 2
	p.Add(line)
	p.Legend.Add("design curve", line)

	if err := sciplot.SaveDefault(p, "wind_power_curve.png"); err != nil {
		panic(err)
	}
}
