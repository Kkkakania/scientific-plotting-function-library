function fig = bayes_uq_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 4312, 'Bayesian uncertainty quantification: distribution shift', 'Bayesian uncertainty quantification', 'distribution shift');
end
