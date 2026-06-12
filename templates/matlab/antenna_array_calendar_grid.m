function fig = antenna_array_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 4219, 'antenna array analysis: calendar grid', 'antenna array analysis', 'calendar grid');
end
