function fig = bayes_uq_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 4303, 'Bayesian uncertainty quantification: state heatmap', 'Bayesian uncertainty quantification', 'state heatmap');
end
