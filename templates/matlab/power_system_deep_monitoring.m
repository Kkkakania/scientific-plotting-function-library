function fig = power_system_deep_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 3601, 'power system analysis: monitoring band time series', 'power system analysis', 'monitoring band time series');
end
