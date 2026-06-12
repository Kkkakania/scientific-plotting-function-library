function fig = synthetic_geo_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 2105, 'synthetic geospatial grid: state cluster scatter', 'synthetic geospatial grid', 'state cluster scatter');
end
