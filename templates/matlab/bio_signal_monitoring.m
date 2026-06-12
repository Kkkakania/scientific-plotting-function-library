function fig = bio_signal_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 2701, 'biomedical signal analysis: monitoring band time series', 'biomedical signal analysis', 'monitoring band time series');
end
