function fig = geoscience_grid_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 4505, 'geoscience grid analysis: state cluster scatter', 'geoscience grid analysis', 'state cluster scatter');
end
