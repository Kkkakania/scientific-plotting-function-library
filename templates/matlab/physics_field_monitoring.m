function fig = physics_field_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 2001, 'physics field analysis: monitoring band time series', 'physics field analysis', 'monitoring band time series');
end
