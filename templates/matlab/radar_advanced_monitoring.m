function fig = radar_advanced_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 4101, 'advanced radar analysis: monitoring band time series', 'advanced radar analysis', 'monitoring band time series');
end
