function fig = power_system_deep_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 3619, 'power system analysis: calendar grid', 'power system analysis', 'calendar grid');
end
