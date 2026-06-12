function fig = bayes_uq_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 4320, 'Bayesian uncertainty quantification: before-after slope', 'Bayesian uncertainty quantification', 'before-after slope');
end
