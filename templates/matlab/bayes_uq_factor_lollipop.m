function fig = bayes_uq_factor_lollipop()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('lollipop', 4314, 'Bayesian uncertainty quantification: factor lollipop', 'Bayesian uncertainty quantification', 'factor lollipop');
end
