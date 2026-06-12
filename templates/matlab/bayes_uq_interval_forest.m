function fig = bayes_uq_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 4315, 'Bayesian uncertainty quantification: interval forest', 'Bayesian uncertainty quantification', 'interval forest');
end
