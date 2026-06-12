function fig = bayes_uq_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 4310, 'Bayesian uncertainty quantification: polar signature', 'Bayesian uncertainty quantification', 'polar signature');
end
