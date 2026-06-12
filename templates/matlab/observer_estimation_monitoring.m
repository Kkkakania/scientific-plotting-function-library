function fig = observer_estimation_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 1701, 'observer and state estimation: monitoring band time series', 'observer and state estimation', 'monitoring band time series');
end
