function fig = reliability_maintenance_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 3301, 'reliability and maintenance: monitoring band time series', 'reliability and maintenance', 'monitoring band time series');
end
