function fig = bayes_uq_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 4318, 'Bayesian uncertainty quantification: 3D response surface', 'Bayesian uncertainty quantification', '3D response surface');
end
