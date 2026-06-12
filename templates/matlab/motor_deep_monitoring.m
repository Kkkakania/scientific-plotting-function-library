function fig = motor_deep_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 2301, 'electric motor analysis: monitoring band time series', 'electric motor analysis', 'monitoring band time series');
end
