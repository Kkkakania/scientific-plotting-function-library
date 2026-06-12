function fig = paper_multipanel_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 2219, 'paper multipanel layout: calendar grid', 'paper multipanel layout', 'calendar grid');
end
