function fig = bayes_uq_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 4307, 'Bayesian uncertainty quantification: multi-metric radar', 'Bayesian uncertainty quantification', 'multi-metric radar');
end
