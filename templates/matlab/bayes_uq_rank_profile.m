function fig = bayes_uq_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 4306, 'Bayesian uncertainty quantification: ranked metric profile', 'Bayesian uncertainty quantification', 'ranked metric profile');
end
