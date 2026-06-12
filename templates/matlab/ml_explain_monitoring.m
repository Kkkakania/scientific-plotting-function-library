function fig = ml_explain_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 1401, 'machine learning explainability: monitoring band time series', 'machine learning explainability', 'monitoring band time series');
end
