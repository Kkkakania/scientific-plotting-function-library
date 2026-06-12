function fig = microgrid_market_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 3819, 'microgrid and market analysis: calendar grid', 'microgrid and market analysis', 'calendar grid');
end
