function fig = protection_fault_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 4019, 'protection and fault analysis: calendar grid', 'protection and fault analysis', 'calendar grid');
end
