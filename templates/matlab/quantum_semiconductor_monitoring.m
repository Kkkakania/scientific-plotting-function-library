function fig = quantum_semiconductor_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 3001, 'quantum and semiconductor analysis: monitoring band time series', 'quantum and semiconductor analysis', 'monitoring band time series');
end
