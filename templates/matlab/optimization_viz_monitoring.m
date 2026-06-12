function fig = optimization_viz_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 2901, 'optimization visualization: monitoring band time series', 'optimization visualization', 'monitoring band time series');
end
