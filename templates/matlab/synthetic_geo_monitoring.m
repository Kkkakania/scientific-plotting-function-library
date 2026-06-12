function fig = synthetic_geo_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 2101, 'synthetic geospatial grid: monitoring band time series', 'synthetic geospatial grid', 'monitoring band time series');
end
