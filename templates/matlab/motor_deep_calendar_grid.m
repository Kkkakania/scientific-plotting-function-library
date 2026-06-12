function fig = motor_deep_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 2319, 'electric motor analysis: calendar grid', 'electric motor analysis', 'calendar grid');
end
