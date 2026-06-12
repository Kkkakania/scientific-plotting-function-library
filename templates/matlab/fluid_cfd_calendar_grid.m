function fig = fluid_cfd_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 2619, 'fluid and CFD analysis: calendar grid', 'fluid and CFD analysis', 'calendar grid');
end
