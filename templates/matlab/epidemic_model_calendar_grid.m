function fig = epidemic_model_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 3519, 'epidemic dynamics: calendar grid', 'epidemic dynamics', 'calendar grid');
end
