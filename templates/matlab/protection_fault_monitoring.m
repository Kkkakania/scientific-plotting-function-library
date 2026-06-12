function fig = protection_fault_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 4001, 'protection and fault analysis: monitoring band time series', 'protection and fault analysis', 'monitoring band time series');
end
