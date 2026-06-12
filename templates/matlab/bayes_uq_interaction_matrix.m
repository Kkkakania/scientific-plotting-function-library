function fig = bayes_uq_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 4313, 'Bayesian uncertainty quantification: interaction bubble matrix', 'Bayesian uncertainty quantification', 'interaction bubble matrix');
end
