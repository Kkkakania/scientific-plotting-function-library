function fig = microgrid_market_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 3805, 'microgrid and market analysis: state cluster scatter', 'microgrid and market analysis', 'state cluster scatter');
end
