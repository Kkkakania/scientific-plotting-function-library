function fig = reliability_maintenance_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 3305, 'reliability and maintenance: state cluster scatter', 'reliability and maintenance', 'state cluster scatter');
end
