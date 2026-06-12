function fig = paper_multipanel_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 2201, 'paper multipanel layout: monitoring band time series', 'paper multipanel layout', 'monitoring band time series');
end
