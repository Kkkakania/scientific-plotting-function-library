function fig = bayes_uq_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 4302, 'Bayesian uncertainty quantification: control limit watch', 'Bayesian uncertainty quantification', 'control limit watch');
end
