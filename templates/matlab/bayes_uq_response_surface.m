function fig = bayes_uq_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 4304, 'Bayesian uncertainty quantification: response contour surface', 'Bayesian uncertainty quantification', 'response contour surface');
end
