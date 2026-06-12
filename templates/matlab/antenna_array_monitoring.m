function fig = antenna_array_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 4201, 'antenna array analysis: monitoring band time series', 'antenna array analysis', 'monitoring band time series');
end
