// scatter_grouped: 按类别着色散点（对照 templates/python/scatter_grouped.py）
package main

import (
	"math/rand"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
	"gonum.org/v1/plot/vg/draw"
	"sciplot.example/templates/sciplot"
)

func main() {
	rng := rand.New(rand.NewSource(0))
	p := plot.New()
	sciplot.ApplyTheme(p)
	p.Title.Text = "Grouped scatter"
	p.X.Label.Text = "feature 1"
	p.Y.Label.Text = "feature 2"
	p.Add(plotter.NewGrid())

	centers := [][2]float64{{0, 0}, {3, 2}, {1.2, 3.5}}
	for i, c := range centers {
		pts := make(plotter.XYs, 60)
		for j := range pts {
			pts[j].X = c[0] + rng.NormFloat64()*0.8
			pts[j].Y = c[1] + rng.NormFloat64()*0.8
		}
		s, err := plotter.NewScatter(pts)
		if err != nil {
			panic(err)
		}
		s.GlyphStyle = draw.GlyphStyle{
			Color:  sciplot.Cycle(i),
			Radius: vg.Points(2.2),
			Shape:  draw.CircleGlyph{},
		}
		p.Add(s)
		p.Legend.Add("group "+string(rune('1'+i)), s)
	}
	if err := sciplot.SaveDefault(p, "scatter_grouped.png"); err != nil {
		panic(err)
	}
}
