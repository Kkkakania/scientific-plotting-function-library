function fig = bayes_uq_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 4321, 'Bayesian uncertainty quantification: decision boundary', 'Bayesian uncertainty quantification', 'decision boundary');
end
