function fig = power_system_deep_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 3605, 'power system analysis: state cluster scatter', 'power system analysis', 'state cluster scatter');
end
