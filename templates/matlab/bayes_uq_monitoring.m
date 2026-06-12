function fig = bayes_uq_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 4301, 'Bayesian uncertainty quantification: monitoring band time series', 'Bayesian uncertainty quantification', 'monitoring band time series');
end
