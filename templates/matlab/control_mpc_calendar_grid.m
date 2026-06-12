function fig = control_mpc_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 1619, 'advanced MPC control: calendar grid', 'advanced MPC control', 'calendar grid');
end
