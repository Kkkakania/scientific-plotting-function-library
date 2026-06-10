// bar_grouped: 分组柱状（对照 templates/python/bar_grouped.py）
package main

import (
	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
	"sciplot.example/templates/sciplot"
)

func main() {
	p := plot.New()
	sciplot.ApplyTheme(p)
	p.Title.Text = "Grouped bars"
	p.Y.Label.Text = "value"

	groups := [][]float64{
		{20, 35, 30, 27},
		{25, 32, 34, 20},
		{12, 26, 31, 17},
	}
	w := vg.Points(14)
	for i, vals := range groups {
		bars, err := plotter.NewBarChart(plotter.Values(vals), w)
		if err != nil {
			panic(err)
		}
		bars.Color = sciplot.Cycle(i)
		bars.LineStyle.Width = 0
		bars.Offset = w * vg.Length(i-1)
		p.Add(bars)
		p.Legend.Add("series "+string(rune('A'+i)), bars)
	}
	p.NominalX("Q1", "Q2", "Q3", "Q4")
	if err := sciplot.SaveDefault(p, "bar_grouped.png"); err != nil {
		panic(err)
	}
}
