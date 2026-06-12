function fig = reliability_maintenance_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 3319, 'reliability and maintenance: calendar grid', 'reliability and maintenance', 'calendar grid');
end
