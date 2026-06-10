// three_phase_waveform: 三相正弦波形（对照 templates/python/three_phase_waveform.py）
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
	p.Title.Text = "Three-phase waveform"
	p.X.Label.Text = "time (ms)"
	p.Y.Label.Text = "voltage (p.u.)"
	p.Add(plotter.NewGrid())

	const f = 50.0
	for i := 0; i < 3; i++ {
		ph := -2 * math.Pi * float64(i) / 3
		pts := make(plotter.XYs, 400)
		for j := range pts {
			t := float64(j) / 399 * 0.04 // 两个周期
			pts[j].X = t * 1000
			pts[j].Y = math.Sin(2*math.Pi*f*t + ph)
		}
		line, err := plotter.NewLine(pts)
		if err != nil {
			panic(err)
		}
		line.Color = sciplot.Cycle(i)
		line.Width = 1.5
		p.Add(line)
		p.Legend.Add(fmt.Sprintf("phase %c", 'a'+i), line)
	}
	if err := sciplot.SaveDefault(p, "three_phase_waveform.png"); err != nil {
		panic(err)
	}
}
