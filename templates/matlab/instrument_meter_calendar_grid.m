function fig = instrument_meter_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 2819, 'instrument and metering: calendar grid', 'instrument and metering', 'calendar grid');
end
