// histogram_basic: 基础直方图（对照 templates/python/histogram_basic.py）
package main

import (
	"image/color"
	"math/rand"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"sciplot.example/templates/sciplot"
)

func main() {
	rng := rand.New(rand.NewSource(0))
	vals := make(plotter.Values, 500)
	for i := range vals {
		vals[i] = rng.NormFloat64()*1.2 + 5
	}
	p := plot.New()
	sciplot.ApplyTheme(p)
	p.Title.Text = "Histogram"
	p.X.Label.Text = "value"
	p.Y.Label.Text = "count"

	h, err := plotter.NewHist(vals, 24)
	if err != nil {
		panic(err)
	}
	c := sciplot.Cycle(0)
	h.FillColor = color.RGBA{c.R, c.G, c.B, 200}
	h.LineStyle.Color = color.White
	p.Add(h)
	if err := sciplot.SaveDefault(p, "histogram_basic.png"); err != nil {
		panic(err)
	}
}
