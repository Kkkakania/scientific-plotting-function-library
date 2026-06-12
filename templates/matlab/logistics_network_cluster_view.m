function fig = logistics_network_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 3405, 'logistics and network analysis: state cluster scatter', 'logistics and network analysis', 'state cluster scatter');
end
