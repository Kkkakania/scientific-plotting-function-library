function fig = synthetic_geo_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 2119, 'synthetic geospatial grid: calendar grid', 'synthetic geospatial grid', 'calendar grid');
end
