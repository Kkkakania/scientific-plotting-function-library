function fig = bayes_uq_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 4317, 'Bayesian uncertainty quantification: stage step curve', 'Bayesian uncertainty quantification', 'stage step curve');
end
