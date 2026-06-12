function fig = model_diagnostics_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 1501, 'model diagnostics: monitoring band time series', 'model diagnostics', 'monitoring band time series');
end
