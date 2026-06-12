function fig = bayes_uq_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 4316, 'Bayesian uncertainty quantification: composition stream', 'Bayesian uncertainty quantification', 'composition stream');
end
