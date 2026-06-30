# Local Resource Intake

This repository can use local study folders only as a requirements source. The
public project should publish clean-room templates, synthetic data, and selected
gallery previews, not raw course packs or private exports.

## Useful Signals

Local folders can safely suggest missing public work when they are reduced to a
plain chart or workflow need:

- signal-processing plots: spectrum, filter response, modulation, matched
  filtering, time-frequency views;
- modelling algorithms: optimization traces, clustering maps, graph paths,
  forecast and evaluation summaries;
- simulation views: scalar fields, vector fields, streamlines, residuals, modal
  shapes;
- paper layout patterns: multipanel grids, shared colorbars, insets, marginal
  distributions, broken axes;
- project-management charts: Gantt, PERT/CPM, WBS, burndown, resource load,
  earned-value curves;
- cross-platform plotting gaps: Origin-like chart families rebuilt in Python
  from synthetic data.

Write these as backlog notes or clean-room templates. Do not copy the source
file that exposed the need.

## Keep Out

Do not commit or quote from:

- paid-course files, book companion files, videos, slides, screenshots, or
  tutorial PDFs;
- `.opj`, `.opju`, `.fig`, `.mat`, `.p`, Office documents, archives, solver
  project files, or binary caches;
- raw ANSYS, Origin, MATLAB, Project, or drawing-tool exports;
- local absolute paths, personal names, emails, student IDs, lab names,
  watermarks, or delivery-pack metadata;
- full local render folders or bulk image dumps.

## Public Conversion Rule

Before adding anything inspired by a local folder, reduce it to one sentence:

```text
Users need a clean synthetic example of <chart/task> for <public workflow>.
```

Then add the smallest public artifact that satisfies that sentence: one
template, one synthetic demo, one selected preview image if needed, and one test
or release check. If the idea needs private files to make sense, keep it out.
