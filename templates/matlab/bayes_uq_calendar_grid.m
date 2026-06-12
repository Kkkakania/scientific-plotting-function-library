function fig = bayes_uq_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 4319, 'Bayesian uncertainty quantification: calendar grid', 'Bayesian uncertainty quantification', 'calendar grid');
end
