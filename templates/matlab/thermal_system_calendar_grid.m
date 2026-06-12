function fig = thermal_system_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 2519, 'thermal system analysis: calendar grid', 'thermal system analysis', 'calendar grid');
end
