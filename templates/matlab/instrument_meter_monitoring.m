function fig = instrument_meter_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 2801, 'instrument and metering: monitoring band time series', 'instrument and metering', 'monitoring band time series');
end
