function fig = radar_advanced_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 4105, 'advanced radar analysis: state cluster scatter', 'advanced radar analysis', 'state cluster scatter');
end
