function fig = storage_battery_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 2401, 'storage and battery analysis: monitoring band time series', 'storage and battery analysis', 'monitoring band time series');
end
