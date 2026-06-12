function fig = logistics_network_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 3401, 'logistics and network analysis: monitoring band time series', 'logistics and network analysis', 'monitoring band time series');
end
