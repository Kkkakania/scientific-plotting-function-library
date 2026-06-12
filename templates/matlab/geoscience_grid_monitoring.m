function fig = geoscience_grid_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 4501, 'geoscience grid analysis: monitoring band time series', 'geoscience grid analysis', 'monitoring band time series');
end
