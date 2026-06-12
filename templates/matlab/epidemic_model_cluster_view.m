function fig = epidemic_model_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 3505, 'epidemic dynamics: state cluster scatter', 'epidemic dynamics', 'state cluster scatter');
end
