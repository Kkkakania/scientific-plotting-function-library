function fig = fluid_cfd_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 2601, 'fluid and CFD analysis: monitoring band time series', 'fluid and CFD analysis', 'monitoring band time series');
end
