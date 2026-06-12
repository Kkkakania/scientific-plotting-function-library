function fig = bayes_uq_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 4305, 'Bayesian uncertainty quantification: state cluster scatter', 'Bayesian uncertainty quantification', 'state cluster scatter');
end
