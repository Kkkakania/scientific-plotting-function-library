function fig = storage_battery_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 2419, 'storage and battery analysis: calendar grid', 'storage and battery analysis', 'calendar grid');
end
