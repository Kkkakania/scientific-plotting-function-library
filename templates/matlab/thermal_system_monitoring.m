function fig = thermal_system_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 2501, 'thermal system analysis: monitoring band time series', 'thermal system analysis', 'monitoring band time series');
end
