function fig = epidemic_model_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 3501, 'epidemic dynamics: monitoring band time series', 'epidemic dynamics', 'monitoring band time series');
end
