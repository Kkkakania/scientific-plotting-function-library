function fig = control_mpc_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 1601, 'advanced MPC control: monitoring band time series', 'advanced MPC control', 'monitoring band time series');
end
