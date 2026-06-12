function fig = insulation_diagnostics_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 3901, 'insulation diagnostics: monitoring band time series', 'insulation diagnostics', 'monitoring band time series');
end
