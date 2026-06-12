function fig = bayes_uq_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 4308, 'Bayesian uncertainty quantification: contribution waterfall', 'Bayesian uncertainty quantification', 'contribution waterfall');
end
