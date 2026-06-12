function fig = model_diagnostics_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 1519, 'model diagnostics: calendar grid', 'model diagnostics', 'calendar grid');
end
