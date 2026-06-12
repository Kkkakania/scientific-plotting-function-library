function fig = optimization_viz_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 2905, 'optimization visualization: state cluster scatter', 'optimization visualization', 'state cluster scatter');
end
