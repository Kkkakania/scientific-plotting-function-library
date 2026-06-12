function fig = chemistry_spectra_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 1919, 'chemistry spectra: calendar grid', 'chemistry spectra', 'calendar grid');
end
