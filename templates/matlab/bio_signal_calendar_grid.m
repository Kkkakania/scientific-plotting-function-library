function fig = bio_signal_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 2719, 'biomedical signal analysis: calendar grid', 'biomedical signal analysis', 'calendar grid');
end
