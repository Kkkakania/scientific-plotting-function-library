function fig = physics_field_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 2019, 'physics field analysis: calendar grid', 'physics field analysis', 'calendar grid');
end
